import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")
# Título de la aplicación
st.title('Rentabilidad de Fondos Sostenibles ODS')

# Subtítulo
st.markdown("""
Esta aplicación te permite seleccionar fondos sostenibles y visualizar su rentabilidad acumulada
en un rango de fechas específico. ¡Selecciona los fondos y el rango de fechas para comenzar!
""")

# Funciones para descargar datos y calcular rentabilidad
def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    closing_prices = data['Adj Close']
    return closing_prices

def calculate_returns(data):
    # Esta función ahora asume que data es un DataFrame con una columna por fondo.
    # Si es una serie (solo un fondo), convertirla a DataFrame
    if isinstance(data, pd.Series):
        data = data.to_frame()
    returns = data.pct_change().dropna().add(1).cumprod().sub(1).mul(100)
    return returns.iloc[-1]

# Creación de columnas para los widgets de selección
col1, col2, col3, col4 = st.columns([0.5, 0.5, 0.5, 4])

funds = ['ESG', 'SUSA', 'ESGU']
selected_funds = []

with col1:
    st.write("Selecciona fondos:")
    for fund in funds:
        # Agrega una clave única a cada checkbox basada en el nombre del fondo
        if st.checkbox(fund, key=f'checkbox_{fund}'):
            selected_funds.append(fund)

with col2:
    start_date = st.date_input("Fecha de inicio", value=pd.to_datetime('2021-01-01'))

with col3:
    end_date = st.date_input("Fecha de fin", value=pd.to_datetime('today'))

with col4:
    espacio = st.write(" ")

# Si hay al menos un fondo seleccionado y el rango de fechas es válido, mostrar resultados
if selected_funds and start_date <= end_date:
    with st.spinner('Cargando datos...'):
        data = get_data(selected_funds, start_date, end_date)
        st.subheader('Gráfico de Precios')
        st.line_chart(data, use_container_width=True)
        
        returns = calculate_returns(data)
        st.subheader("Rentabilidad acumulada (%) en el periodo seleccionado:")
        
        if isinstance(returns, pd.Series):
            rent_columns = st.columns(len(returns))
            for (ticker, value), column in zip(returns.items(), rent_columns):
                column.metric(label=f"{ticker}", value=f"{value:.2f}%")
        else:
            st.metric(label="Rentabilidad acumulada", value=f"{returns:.2f}%")
elif selected_funds:
    st.error('Por favor, asegúrate de que el rango de fechas es válido.')