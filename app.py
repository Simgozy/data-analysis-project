import streamlit as st
import pandas as pd
import plotly.express as px

# Lee el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Añade un encabezado a la aplicación
st.header('Análisis de Datos de Anuncios de Venta de Coches')

# Crea casillas de verificación para histograma y gráfico de dispersión
show_hist = st.checkbox('Mostrar Histograma')
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión')

# Genera los gráficos basados en las casillas de verificación
if show_hist:
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Creando un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)