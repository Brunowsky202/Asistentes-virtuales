import os
import google.generativeai as genai

# Ajustando gemini para autenticar
API_KEY = "AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0"
genai.configure(api_key=API_KEY)

# Creando la instancia que contendra nuestro modelo
model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(
    history=[]
)
def answer():
    myfile = genai.upload_file("graba.wav")
    result = chat_session.send_message([myfile, "Transcribe el audio"])
    print("pregunta enviada")
    print(result.text)
    print("pregunta contestada")