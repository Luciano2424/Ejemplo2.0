import streamlit as st
from PIL import Image

# Título de la página
st.title("Bienvenidos a Universidad San Sebastián")

#Imagen cr7
image = Image.open("cr7.jpg")
st.image(image, caption='Imagen de CR7', use_column_width=True)

#barra lateral
st.sidebar.title("Barra lateral")
st.sidebar.header("Hola")
st.sidebar.write("Esto es mi barra lateral")
