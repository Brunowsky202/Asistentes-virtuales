import os
import urllib.parse
import google.generativeai as genai
import urllib
from pptx import Presentation
import pptx



function = []
API_KEY = "AIzaSyCo_-pGxWJja-gbNYNq9SVJRgE9AVol1wU"
genai.configure(api_key=API_KEY)

config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

activado = False
def buscar_en_linea_o_en_la_web(busqueda:str):
    global activado
    """ Buscar en linea
    Description: es una funcion y busca en linea cuando el usuario diga "busca en linea..."
    o "que es..." crea un enlace de busqueda en google con lo que el usuario pide

    Args:
        busqueda: es la busqueda en linea que el usuario quiere hacer
    """
    url = f"https://www.google.co.ve/search?q={urllib.parse.quote(busqueda)}"
    os.system(f"start msedge.exe {url}")
    activado = True


def answer(text:str):
    global activado
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*", "").replace("/","")
    else: 
        return "Acción realizada"

def crear_una_pesentacion_de_power_point(tema:str):
    """
    Esta es una funcion que crea una presentacion de power point cuando el usuario dice
    "crea una presentacion" o algo asi

    Arg:
        tema: es el tema de la presentacion
    """
    activado = True
    resultado =model2.generate_content([f"creame una presentacion de power point sobre {tema} en ingles", "Reccuerda que tu resultado sera un script de python que con la libreria pptx genere una presentacion de power point, SOLO DEVUELVE EL CODIGO y recueda al final abrir dicho archivo pptx usando la libreria OS ", "En las cadenas de textos ni en los comentarios no uses caracteres especiales ni uses acentos como 'ñ' o 'á'"])
    codigo = resultado.text.split("```")[1].replace("python", "").replace("�", "")
    fin = f"# This Python file uses the following encoding: utf-8 {codigo}"
    presentation(fin)




# hola()

def presentation(codigo):
    with open("presentacion2.py", "w") as f:
        f.write(codigo)
    os.system(" C:/Users/Ada-Amarillo/AppData/Local/Programs/Python/Python312/python.exe presentacion2.py")
    
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=config,
    tools=[crear_una_pesentacion_de_power_point]
)
model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=config,
)
chat = model.start_chat(enable_automatic_function_calling=True)

#chat.send_message("Crea una presentacion de power point sobre el agua")

# if key_word():
#     crear_una_pesentacion_de_power_point("el agua")
