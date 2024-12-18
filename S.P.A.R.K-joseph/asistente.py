from modules.gemini import answer
from modules.key_word import key_word
from modules.tts import talk
import sys
from modules.transcripcion import transcribes

def start():
    try:
        print("Iniciando")
        while True:
            if key_word("spark"):
                try:
                    audio_text = transcribes()
                    print(f"se escucho {audio_text}")
                    respuesta = answer(audio_text)
                    print(respuesta)
                    talk(respuesta)
                    print("Activame de nuevo para seguir hablando")
                except Exception as e:
                    print("vaya ha ocurrido un error, activame de nuevo para continuar")

    except KeyboardInterrupt:
        print("Adiossss....")
    except Exception as e:
        print(e)

start()