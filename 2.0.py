import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

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


# Cargar el archivo de Excel
uploaded_file = st.file_uploader("Elige un archivo Excel (Base de datos cr7 messi)", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Leer el archivo de Excel
        df = pd.read_excel(uploaded_file)

        # Mostrar el DataFrame
        st.write("Datos de la base de datos:")
        st.dataframe(df)

        # Mostrar el gráfico de barras
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots()
        df.set_index('Categoría').plot(kind='bar', ax=ax)
        ax.set_ylabel("Número de Goles")
        ax.set_title("Goles de Cristiano Ronaldo y Lionel Messi")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
