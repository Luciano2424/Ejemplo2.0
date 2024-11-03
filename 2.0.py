import streamlit as st
from PIL import Image

# Título de la página
st.title("Bienvenidos a Universidad San Sebastián")

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

ploaded_file = st.file_uploader("Base.xlsx", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo de Excel
    df = pd.read_excel(uploaded_file)

    # Mostrar el DataFrame
    st.write("Datos de la base de datos:")
    st.dataframe(df)

    # Barra lateral para seleccionar el tipo de gráfico
    chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico:", ("Gráfico de Barras", "Gráfico de Torta"))

    # Mostrar el gráfico según la selección
    if chart_type == "Gráfico de Barras":
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots()
        df.set_index('Categoría').plot(kind='bar', ax=ax)
        ax.set_ylabel("Número de Goles")
        ax.set_title("Goles de Cristiano Ronaldo y Lionel Messi")
        st.pyplot(fig)

    elif chart_type == "Gráfico de Torta":
        st.subheader("Gráfico de Torta")
        # Crear gráficos de torta para cada sección
        for index, row in df.iterrows():
            labels = ['Cristiano Ronaldo', 'Lionel Messi']
            sizes = [row['Cristiano Ronaldo'], row['Lionel Messi']]
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.write(f"Distribución de {row['Categoría']}:")
            st.pyplot(fig)
