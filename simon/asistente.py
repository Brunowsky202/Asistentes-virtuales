from modules.Gemini import answer
from modules.key_word import key_word
from modules.tts import talk
from modules.stt import transcribes
def start():
    try:
        print("Iniciando")
        while True:
            if key_word("hola"):
                try:
                    print(" En que te ayudo?")
                    audio_text = transcribes()
                    print(f"Se escucho {audio_text}")
                    respuesta = answer(audio_text)
                    print(respuesta)
                    # if (len(respuesta) > 1):
                    talk(respuesta)
                    print("Activame de nuevo para seguir hablado")
                except Exception as e:
                    print(e)
    except Exception as e:
        print("Vaya ha ocurrido un error,activame de nuevo")
    except KeyboardInterrupt:
        print("Adiossssss...")
    except Exception as e:
        print(e)
start()
    
    
    
    
    
    
    
    
