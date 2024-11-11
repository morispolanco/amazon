import streamlit as st
import requests

# Accede a la clave de API de Perplexity desde los secretos
API_KEY = st.secrets["perplexity"]["api_key"]

def obtener_datos_titulo(titulo):
    # Aquí haces la solicitud a la API de Perplexity
    url = f"https://api.perplexity.ai/v1/search?query={titulo}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def analizar_datos(datos):
    # Procesar los datos obtenidos de la API
    indice_competencia = datos.get('competencia', 0)
    ganancias_estimadas = datos.get('ganancias', 0)
    numero_competidores = datos.get('competidores', 0)
    return indice_competencia, ganancias_estimadas, numero_competidores

# Interfaz de usuario
st.title("Buscador de Nichos para Libros en Amazon")

titulo = st.text_input("Introduce un título o palabra clave:")
if st.button("Buscar"):
    if titulo:
        datos = obtener_datos_titulo(titulo)
        indice_competencia, ganancias_estimadas, numero_competidores = analizar_datos(datos)
        
        st.subheader("Resultados:")
        st.write(f"Índice de Competencia: {indice_competencia}")
        st.write(f"Ganancias Mensuales Estimadas: ${ganancias_estimadas}")
        st.write(f"Número de Competidores: {numero_competidores}")
    else:
        st.warning("Por favor, introduce un título o palabra clave para buscar.")
