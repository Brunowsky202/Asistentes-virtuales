import os
from urllib.parse import urlparse, urlencode
from urllib.parse import urljoin
import google.generativeai as genai

API_KEY = "AIzaSyCruYmiy38pHNbTkxhBy9q87PQPOZ--vjo"
genai.configure(api_key=API_KEY)
activado = False

def abrir_busqueda_pinterest(busqueda: str):
    """
    Abre la búsqueda en Pinterest en el navegador. Se activa cuando el usuario expresa
    "Quiero ver un..." o "Busca una imagen sobre..."
    
    Args:
        busqueda: Es la consulta que desea buscar el ususario
    """

    url_base = "https://www.pinterest.com/search/pins/"  # URL base para búsquedas

    # Construir los parámetros de la URL usando urlencode
    params = {"q": busqueda}
    query_string = urlencode(params)

    # Construir la URL completa usando urljoin (o concatenación simple)
    url_completa = urljoin(url_base, "?" + query_string)
    print(f"URL construida: {url_completa}")

    try:
        os.system(f"start msedge.exe {url_completa}")
        print("Abriendo la URL en el navegador...")
    except Exception as e:
        print(f"Error al abrir el navegador: {e}")

def answer(text:str):
    global activado
    print("Generando...")
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else : return ""
config = {

    "temperature": 0.8,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

functions = [abrir_busqueda_pinterest]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
    tools=[functions]
)   
model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
)  
chat = model.start_chat(enable_automatic_function_calling=True)

