import streamlit as st
import requests

# Accede a la clave de API de OpenRouter desde los secretos
OPENROUTER_API_KEY = st.secrets["openrouter"]["api_key"]

def obtener_respuesta_openrouter(mensaje):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    }
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": mensaje}]
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

# Interfaz de usuario
st.title("Asistente de OpenRouter")

mensaje_usuario = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if mensaje_usuario:
        respuesta = obtener_respuesta_openrouter(mensaje_usuario)
        
        if 'choices' in respuesta and len(respuesta['choices']) > 0:
            contenido_respuesta = respuesta['choices'][0]['message']['content']
            st.subheader("Respuesta del Asistente:")
            st.write(contenido_respuesta)
        else:
            st.error("No se pudo obtener una respuesta válida.")
    else:
        st.warning("Por favor, introduce un mensaje para enviar.")
