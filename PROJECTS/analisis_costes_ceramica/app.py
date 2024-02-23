import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
import pandas as pd


# Título de la aplicación
st.title('Calculadora Producción Neolith')


# Entradas del usuario
precio_venta = st.number_input('Precio de venta por m² (€)', min_value=0.0, format='%.2f')
margen_ganancia_deseado = st.number_input('Margen deseado (%)', min_value=0.0, format='%.2f')
costo_actual_por_m2 = st.number_input('Coste actual por m² (€)', min_value=0.0, format='%.2f')
produccion_actual_m2 = st.number_input('Producción actual (m² por día)', min_value=0.0, format='%.2f')

# Botón para realizar el cálculo
if st.button('Calcular'):
    
    # Cálculos
    costo_nuevo = precio_venta - (margen_ganancia_deseado / 100) * precio_venta
    reduccion_costo_necesaria = costo_actual_por_m2 - costo_nuevo
    porcentaje_reduccion_costo = (reduccion_costo_necesaria / costo_actual_por_m2) * 100
    mejora_costo_por_aumento_produccion = porcentaje_reduccion_costo / 5
    aumento_produccion_necesario = mejora_costo_por_aumento_produccion * 10
    produccion_adicional = produccion_actual_m2 * (aumento_produccion_necesario / 100)
    nueva_produccion_total_diaria = produccion_actual_m2 + produccion_adicional

    data = {
    'Concepto': ['Coste nuevo por m² (€)', 'Aumento de producción necesario (%)', 'Producción adicional requerida (m²)', 'Nueva producción total diaria (m²)'],
    'Valor': [f"{costo_nuevo:.2f}", f"{aumento_produccion_necesario:.2f}", f"{produccion_adicional:.2f}", f"{nueva_produccion_total_diaria:.2f}"]
}

    # Convertir los datos en un DataFrame de pandas
    results_df = pd.DataFrame(data)
    
    # Mostrar la tabla de resultados
    st.dataframe(results_df.set_index('Concepto'))

    
    # Preparar datos para la gráfica Echart
    max_produccion = produccion_actual_m2
    while True:
        costo_temp = costo_actual_por_m2 - (max_produccion - produccion_actual_m2) / produccion_actual_m2 * 5 / 10 * (costo_actual_por_m2 / 2)
        if costo_temp <= costo_nuevo:
            break
        max_produccion += 1
    
    producciones = np.linspace(produccion_actual_m2, max_produccion).astype(int).tolist()
    costos = (costo_actual_por_m2 - (np.array(producciones) - produccion_actual_m2) / produccion_actual_m2 * 5 / 10 * (costo_actual_por_m2 / 2)).tolist()
    precio_venta_line = [precio_venta for _ in producciones]
    
    # Configuración de Echarts para la gráfica de línea con tema oscuro
    options = {
        "title": {
            "text": 'Curva Costes',
            "textStyle": {
                "color": '#fff'  # Texto del título en blanco
            }
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data":['Coste', 'Precio Venta'],
            "textStyle": {
                "color": '#fff'  # Texto de la leyenda en blanco
            }
        },
        "xAxis": {
            "type": 'category',
            "data": producciones
        },
        "yAxis": {
            "type": 'value',
            "splitLine": { "show": False }
        },
        "series": [
            {
                "name": 'Coste',
                "type": 'line',
                "data": costos,
                "itemStyle": { "color": '#a6c84c' },
                "lineStyle": { "color": '#a6c84c' }
            },
            {
                "name": 'Precio Venta',
                "type": 'line',
                "data": precio_venta_line,
                "itemStyle": { "color": 'red' },
                "lineStyle": { "color": 'red' }
            }
        ],
        "backgroundColor": '#333',
        "textStyle": {
            "color": '#fff'
        }
    }

    
    # Dibujar la gráfica Echart en Streamlit con el tema oscuro
    st_echarts(options=options, height="400px")
