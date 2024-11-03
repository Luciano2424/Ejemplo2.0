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

if st.sidebar.button("Haz echo cick pero en la barra lateral"):
    st.sidebar.write("Haz echo click en el botón de la barra lateral")

user_input = st.sidebar.text_input("Escribe algo en la barra: ")
st.sidebar.write(f"Has escrito: {user_input}")
