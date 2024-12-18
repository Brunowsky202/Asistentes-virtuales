import os
import google.generativeai as genai
import urllib
import urllib.parse
from docx import Document

functions = []
API_KEY = "AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0"
genai.configure(api_key=API_KEY)
config = {
    "temperature": 0.8,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens": 8196,
    "response_mime_type":"text/plain"
}

activado = False
def crear_un_archivo_word_y_escribir_en_el_un_trabajo(tema:str):
    """
    Description:
    Es una funcion que va a realizar la accion de crear un archivo en word, y despues escribira en el un trabajo sobre el avance de la tecnologia, 
    cuando el usuario dice "crea un trabajo sobre...", "escribe un documento sobre...", "Escribe sobre..."
    Args:
    tema: Es el tema del trabajo
    """
    global activado
    activado = True
    resultado =model2.generate_content([f"Crea un trabajo de word sobre {tema}","Recuerda que tu resultado sera un script de python que con la libreria docx genere un trabajo, solo devuelve el codigo y recuerda al final abrir dicho archivo docx usando la libreria os y que el archivo", "En las cadenas de textos ni en los comentarios no uses caracteres especiales ni uses acentos como 'ñ' o 'á', tampoco uses componetes como iamgenes ni dada parecido porque provocara errores en el código"])
    codigo =resultado.text.split("```")[1].replace("python", "").replace("¬", "")
    fin = f"# This python file uses the following encoding: utf-8 {codigo}"
    trabajo(fin) 


def trabajo(codigo):
    with open ("trabajo.py", "w") as f:
        f.write(codigo)
    os.system("C:/Users/Ada-Amarillo/AppData/Local/Programs/Python/Python312/python.exe trabajo.py")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=config,
    tools=[crear_un_archivo_word_y_escribir_en_el_un_trabajo]
)

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=config,
)

chat = model.start_chat(enable_automatic_function_calling=True)

def answer(text:str):
    global activado
    print("Generando...")
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else : return ""

#chat.send_message("Crea un trabajo en word sobre el avance de la tecnologia")
##def answer(text):
    ##result = chat.send_message(text)
    ##return result.text.replace("*","").replace("/","")

#llamada a la funcion para crear archivos word