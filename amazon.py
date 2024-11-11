import streamlit as st
from perplexipy import PerplexityClient
import os

# Obtener la clave de la API desde los secretos de Streamlit
api_key = st.secrets["perplexity"]["api_key"]

# Inicializar el cliente de Perplexity
client = PerplexityClient(key=api_key)

st.title("Análisis de Nicho para tu Libro en Amazon")

# Entrada del usuario para la palabra clave o título
keyword = st.text_input("Introduce una palabra clave o título:")

if keyword:
    # Realizar la consulta a la API de Perplexity
    query = f"Análisis de mercado para libros en Amazon sobre '{keyword}': " \
            f"índice de competencia, número de búsquedas mensuales, " \
            f"ganancias estimadas y número de competidores."
    response = client.query(query)

    # Mostrar los resultados
    st.subheader("Resultados del Análisis:")
    st.write(response)
