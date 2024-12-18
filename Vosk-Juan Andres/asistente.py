from modules.gemini import answer 
from modules.key_word import key_word
from modules.tts import talk 
from modules.stt import transcribes
def start ():
    try:
        print( "Iniciando")
        while True:
            if key_word("juan"):
                try:
                    audio_text = transcribes()
                    print (f"Se escucho {audio_text}")
                    respuesta = answer(audio_text)
                    print(respuesta)
                    talk(respuesta)
                    print("Activame de nuevo para seguir hablando")
                except Exception as e:
                    print("Vaya ha ocurrido un error, activame de nuevo")
    except KeyboardInterrupt:
            print("Adiossssss...")
    except Exception as e:
            print(e)
start()