import os
import urllib.parse
import urllib
import google.generativeai as genai
from docx import Document


API_KEY = "AIzaSyAKIXenE4WIyx96A9T6WgLCD1feLk-DOYY"
genai.configure( api_key=API_KEY)

config = {
    "temperature" : 0.8,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}


activado = False
def Buscar_en_linea_o_en_la_web(busqueda:str):

    global activado, chat_session

    """
        Es una funcion que hace una busqueda en linea en el navegador
        de algo sobre lo que el usuario dice "hola me podrias brindarme ...."
    
        ARGS:
            a: Es un numero entero
            b: La busqueda....
    """
    url = f"https://www.google.co.ve/search?q={urllib.parse.quote(busqueda)}"
    os.system(f"start msedge {url}")
    activado = True

    Buscar_en_linea_o_en_la_web("hamburguesa")

def escribir_un_documento(tema:str):
    global activado
    """ 
    Description:
        Es una funcion la cual escribe un documento con la herramienta de word 2016
        " hola quiero que me hagas un..."
    Arg:
        a: Es una cadena
        b: El documento...
    
    """
    activado = True
    document = Document()
    result = model2.generate_content([tema, "Redacta un ensayo de 500 palabras sobre el tema empleado"])
    paragraph = document.add_paragraph(result.text)

    document.save('test.docx')
    os.system("start WINWORD.exe test.docx")

def answer(text:str):
    global activado
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else:
        return "Acción realizada"
function = [Buscar_en_linea_o_en_la_web, escribir_un_documento]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
    tools=[function]
)

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
)
chat = model.start_chat(enable_automatic_function_calling=True)

