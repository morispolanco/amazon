import streamlit as st
import requests

# Accede a la clave de API de Serper desde los secretos
API_KEY = st.secrets["serper"]["api_key"]

def obtener_datos_titulo(titulo):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "q": titulo
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP 4xx o 5xx
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"Error HTTP: {http_err}")
        return {}
    except requests.exceptions.RequestException as err:
        st.error(f"Error de solicitud: {err}")
        return {}
    except ValueError as json_err:
        st.error(f"Error al decodificar la respuesta JSON: {json_err}")
        return {}

def analizar_datos(datos):
    if 'organic' in datos:
        competencia = datos['organic'][0].get('competition', 'N/A')  # Ajusta según la estructura de la respuesta
        ganancias_estimadas = datos['organic'][0].get('estimated_earnings', 'N/A')
        numero_competidores = datos['organic'][0].get('competitors', 'N/A')
        return competencia, ganancias_estimadas, numero_competidores
    return 'N/A', 'N/A', 'N/A'

# Interfaz de usuario
st.title("Buscador de Nichos para Libros en Amazon")

titulo = st.text_input("Introduce un título o palabra clave:")
if st.button("Buscar"):
    if titulo:
        datos = obtener_datos_titulo(titulo)
        competencia, ganancias_estimadas, numero_competidores = analizar_datos(datos)
        
        st.subheader("Resultados:")
        st.write(f"Índice de Competencia: {competencia}")
        st.write(f"Ganancias Mensuales Estimadas: ${ganancias_estimadas}")
        st.write(f"Número de Competidores: {numero_competidores}")
    else:
        st.warning("Por favor, introduce un título o palabra clave para buscar.")
