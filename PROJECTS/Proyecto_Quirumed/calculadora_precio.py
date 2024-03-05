import streamlit as st
from streamlit_echarts import st_echarts

# Título de la aplicación
# Título de la aplicación centrado
st.markdown("<h1 style='text-align: center;'>Análisis Precios Quirumed</h1>", unsafe_allow_html=True)
#AVISO
st.markdown(
    """
    ⚠️ Esta app es para el análisis del caso Quirumed, ¡léelo antes! 
    [Aquí](https://github.com/stevenallus/Portfolio/blob/main/PROJECTS/Proyecto_Quirumed/Quirumed.ipynb)
    """,
    unsafe_allow_html=True
)

# Mostrar una imagen de un camilla desde una URL en forma de círculo, centrada
st.markdown(
    """
    <style>
    .image-circle {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stSlider > div {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Reemplaza 'URL_DE_TU_IMAGEN' con la URL de la imagen que deseas mostrar
url_imagen = 'https://scontent.fvlc6-1.fna.fbcdn.net/v/t39.30808-1/327311832_873466107109318_4441655141331193662_n.png?stp=dst-png_p200x200&_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_ohc=jv1ggUJhazUAX9881C5&_nc_ht=scontent.fvlc6-1.fna&oh=00_AfCcglN9YpsSz2EEMCabIft_m1M8GVe_77qStjCfANWkbg&oe=65EC2E62'

st.markdown(
    f'<img class="image-circle" src="{url_imagen}">', 
    unsafe_allow_html=True,
)

st.title('Calculadora Precios')

# Entrada de un precio de competidor
precio_competencia = st.number_input('Introduce el precio de la competencia', min_value=0.0, format='%.2f')

# Entrada de altura y ancho
altura = st.number_input('Altura', min_value=0.0, format='%.2f')
ancho = st.number_input('Ancho', min_value=0.0, format='%.2f')

# Botón para realizar cálculo y visualización
if st.button('Calcular'):
    if precio_competencia and altura and ancho:
        # Calcula el precio recomendado como un 5% más barato que la competencia
        precio_recomendado = precio_competencia * 0.95
        st.success(f'El precio recomendado de venta es: {precio_recomendado:.2f} €')
        
        # Preparar los datos para el gráfico de ECharts
        descuentos = [(1 - i / 100) for i in range(11)]  # Rango de descuentos del 0% al 10%
        precios = [precio_competencia * d for d in descuentos]
        
        # Crear el gráfico de ECharts
        options = {
            "title": {
                "text": 'Curva de Demanda en función del Descuento'
            },
            "tooltip": {
                "trigger": 'axis'
            },
            "xAxis": {
                "type": 'category',
                "data": [f"{int(d*100)}%" for d in descuentos]
            },
            "yAxis": {
                "type": 'value',
                "axisLabel": {
                    "formatter": '€{value}'
                }
            },
            "series": [{
                "data": precios,
                "type": 'line',
                "smooth": True,
                "markLine": {
                    "silent": True,
                    "data": [{"yAxis": precio_recomendado}]
                }
            }]
        }

        # Mostrar el gráfico de ECharts en Streamlit
        st_echarts(options=options, height="400px")
    else:
        st.error('Por favor, introduce un precio de la competencia y las dimensiones.')


