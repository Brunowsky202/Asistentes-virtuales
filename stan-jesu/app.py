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

while(True):
    consulta = input("ingrese su pregunta a gemini")
    try:
        result = chat_session.send_message(consulta)
        print(result.text)
    except Exception as e:
        print("TIENES QUE ESCRIBIR UNA PREGUNTA, SUBNORMAL")
    repeat = input("Otra pregunta y/n?")
    if repeat == "n": break