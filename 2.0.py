import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

# Título de la página
st.title("Goles de Cristiano Ronaldo y Lionel Messi")

#Imagen cr7
image = Image.open("cr7.jpg")
st.image(image, caption='Imagen de CR7', use_column_width=True)

#barra lateral
st.sidebar.title("Barra lateral")
st.sidebar.header("Barra interactiva")
st.sidebar.write("Esto es mi barra lateral")

if st.sidebar.button("Haz cick hay una sorpresa"):
    st.sidebar.write("Cr7 >>>>> Messi")

user_input = st.sidebar.text_input("Escribe algo en la barra: ")
st.sidebar.write(f"Has escrito: {user_input}")


# Título de la aplicación
st.title("Goles de Cristiano Ronaldo y Lionel Messi")

# Crear un DataFrame con los datos
data = {
    "Categoría": ["Goles con la selección", "Goles en la Champions", "Goles históricos"],
    "Cristiano Ronaldo": [123, 140, 850],
    "Lionel Messi": [106, 130, 835]
}

df = pd.DataFrame(data)

# Convertir el DataFrame a un formato largo para Altair
df_long = df.melt(id_vars="Categoría", var_name="Jugador", value_name="Número de Goles")

# Crear el gráfico de barras
chart = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('Categoría:N', title='Categoría', axis=alt.Axis(labelAngle=135), fontdict={'family': 'serif', 'color': 'blue', 'weight': 'bold', 'size': 14}),
    y=alt.Y('Número de Goles:Q', title='Número de Goles'),
    color='Jugador:N',
    column='Jugador:N',  # Mueve cada jugador a una posición en la gráfica
    tooltip=['Jugador:N', 'Número de Goles:Q']
).properties(
    title='Goles de Cristiano Ronaldo y Lionel Messi'
)

# Mostrar el gráfico
st.altair_chart(chart, use_container_width=True)
