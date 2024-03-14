import streamlit as st
import yfinance as yf
import pandas as pd

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Rentabilidad Fondos ODS</h1>", unsafe_allow_html=True)
st.markdown(
    """
    ⚠️ Esta app es para el análisis de casos de inversión en Fondos Sostenibles, ¡léelo antes! 
    [Aquí](https://github.com/stevenallus/Portfolio/blob/main/PROJECTS/Rentabilidad_Fondos_Sostenibles/Actividad_2_Entrega.pdf)
    """,
    unsafe_allow_html=True
)
# Selector de fondos
selected_funds = st.multiselect('Selecciona fondos', ['ESG', 'SUSA', 'ESGU'], default=['ESG'])

# Selector de rango de fechas
start_date, end_date = st.date_input("Selecciona el rango de fechas", value=[pd.to_datetime('2021-01-01'), pd.to_datetime('today')], min_value=pd.to_datetime('2000-01-01'), max_value=pd.to_datetime('today'))

# Descargar datos y calcular rentabilidad acumulada
def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    closing_prices = data['Adj Close']
    return closing_prices

def calculate_returns(data):
    returns = data.pct_change().dropna().add(1).cumprod().sub(1).mul(100)
    return returns.iloc[-1]

if selected_funds and start_date and end_date:
    data = get_data(selected_funds, start_date, end_date)
    
    # Mostrar gráfico de precios
    st.line_chart(data)

    # Calcular y mostrar la rentabilidad acumulada
    returns = calculate_returns(data)
    st.write("Rentabilidad acumulada (%) en el periodo seleccionado:")
    st.write(returns)

