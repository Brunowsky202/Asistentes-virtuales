import os 
import google.generativeai as genai
import urllib
import urllib.parse
API_KEY = "AIzaSyCruYmiy38pHNbTkxhBy9q87PQPOZ--vjo"
genai.configure(api_key=API_KEY)

config = {

    "temperature": 0.8,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}
activado = False
def buscar_en_linea_o_en_la_web(busqueda:str):
    global activado
    """
    Esta funcion es para generar una historia en un archivo txt en el bloc de notas
    
    Args:

    """
    url = f"https://www.google.com/search?q={urllib.parce.quote(busqueda)}"
    os.system(f"start msedge {url}")
    activado = True
    # ----CASO AUGUSTO Y GIANFRANCO----
    #os.system(f"google '{url}'")


def escribe_una_historia(tema:str):
    print("Creando...")
    """
        esta funcion es para generar una historia en un archivo txt en el bloc de notas
        cuand el usuario dice cosas como "Escribe una historia... " o "crea una historia sobre..."
    Args:
        tema: el tema que establecio el usuario
    """
    global activado
    activado = True
    result = model2.generate_content([tema, "Escribe una historia con el tema que te dí"])
    with open("historia.txt","w") as archivo:
        archivo.write(result.text)
    os.system("start notepad.exe historia.txt")
    print("Listo")

        
functions = [buscar_en_linea_o_en_la_web, escribe_una_historia]
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

def answer(text:str):
    global activado
    print("Generando...")
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else : return ""
