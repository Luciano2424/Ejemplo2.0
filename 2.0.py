import streamlit as st
from PIL import Image

# Título de la página
st.title("Bienvenidos a Universidad San Sebastián")

# Cargar y mostrar la imagen
image = Image.open("cr7.jpg")
st.image(image, caption='Imagen de CR7', use_column_width=True)