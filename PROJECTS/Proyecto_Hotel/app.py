import streamlit as st
import pandas as pd
import numpy as np


# Título de la aplicación
# Título de la aplicación centrado
st.markdown("<h1 style='text-align: center;'>Calculadora Proyecto Hotel Neolith</h1>", unsafe_allow_html=True)
#AVISO
st.markdown(
    """
    ⚠️ Esta app es para el análisis del caso del Hotel, ¡léelo antes! 
    [Aquí](https://github.com/stevenallus/Portfolio/blob/main/PROJECTS/costes_ceramica/costes_produccion.ipynb)
    """,
    unsafe_allow_html=True
)
# Mostrar una imagen de un hotel desde una URL en forma de círculo, centrada
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
url_imagen = 'https://www.focuspiedra.com/wp-content/uploads/2019/11/ac-marriot-dallas-neolith-e1573715507364-1.jpg'

st.markdown(
    f'<img class="image-circle" src="{url_imagen}">', 
    unsafe_allow_html=True,
)

# Agrega un espacio en blanco para la separación
st.markdown("<br><br>", unsafe_allow_html=True)

st.write('\n\n\n')

# Definición de los datos iniciales
costes = {'Fusion': 22, 'Timber': 22, 'Iron': 21, 'Colorfeel': 28}
m2 = {'Suelo': 5000, 'Encimeras/Mesas': 300, 'Fachada': 1500}
precio_suelo = 20  # Precio fijo para Fusion y Timber

# Inputs del usuario para los precios de Iron y Colorfeel
precio_iron = st.slider('Precio por m2 para Iron:', min_value=20.0, max_value=50.0, value=21.0, step=0.5)
precio_colorfeel = st.slider('Precio por m2 para Colorfeel:', min_value=25.0, max_value=60.0, value=28.0, step=0.5)

# Cálculo de ventas esperadas y beneficios
ventas = {
    'Fusion': precio_suelo * m2['Suelo'] / 2,
    'Timber': precio_suelo * m2['Suelo'] / 2,
    'Iron': precio_iron * m2['Encimeras/Mesas'],
    'Colorfeel': precio_colorfeel * m2['Fachada']
}
coste_total = sum([costes[producto] * m2_area for producto, m2_area in zip(['Fusion', 'Timber', 'Iron', 'Colorfeel'], [m2['Suelo']/2, m2['Suelo']/2, m2['Encimeras/Mesas'], m2['Fachada']])])
venta_total = sum(ventas.values())
beneficio = venta_total - coste_total
margen = beneficio / venta_total * 100

# Mostrando los resultados
st.write(f"Coste Total del Proyecto: {coste_total}€")
st.write(f"Venta Total Esperada: {venta_total}€")
st.write(f"Beneficio Total: {beneficio}€")
st.write(f"Margen de Beneficio: {margen:.2f}%")

if margen < 14:
    st.error("El margen es menor que el objetivo del 14%.")
else:
    st.success("El margen cumple con el objetivo mínimo del 14%.")
