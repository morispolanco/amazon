import streamlit as st
import requests
import json

# Obtener la clave de la API desde los secretos de Streamlit
api_key = st.secrets["openrouter"]["api_key"]

# Configuración de la API de OpenRouter
api_url = "https://openrouter.ai/api/v1/chat/completions"

st.title("Análisis de Nicho para tu Libro en Amazon")

# Entrada del usuario para la palabra clave o título
keyword = st.text_input("Introduce una palabra clave o título:")

if keyword:
    # Definir el prompt para la API
    prompt = (
        f"Análisis de mercado para libros en Amazon sobre '{keyword}': "
        "índice de competencia, número de búsquedas mensuales, "
        "ganancias estimadas y número de competidores."
    )
    
    # Estructura de los mensajes según la API de OpenRouter
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    # Configurar los datos para la solicitud
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": messages
    }
    
    # Configurar los encabezados de la solicitud
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Realizar la solicitud a la API de OpenRouter
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        # Procesar la respuesta JSON
        result = response.json()
        # Extraer el contenido generado
        generated_text = result['choices'][0]['message']['content']
        
        # Mostrar los resultados
        st.subheader("Resultados del Análisis:")
        st.write(generated_text)
    else:
        st.error(f"Error en la solicitud a OpenRouter: {response.status_code}")
        st.error(response.text)
