import streamlit as st
from PIL import Image
import pandas as pd

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

# Mostrar el gráfico de barras
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
df.set_index('Categoría').plot(kind='bar', ax=ax)
ax.set_ylabel("Número de Goles")
ax.set_title("Goles de Cristiano Ronaldo y Lionel Messi")
st.pyplot(fig)
