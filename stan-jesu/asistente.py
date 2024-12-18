from modules.gemini import answer
from modules.key_word import key_word
from modules.tts import talk
from modules.stt import transcribes
def start():
    try:
        print("Iniciando")
        while True:
            if key_word("hola"):
                print("Palabra reconocida")
                try:
                    audio_text = transcribes()
                    print(f"se escucho{audio_text}")
                    respuesta = answer(audio_text)
                    print(respuesta)
                    talk(respuesta)
                    print("Activame de nuevo para seguir hablando ctm")
                except Exception as e:
                    print("Vaya ha ocurrido un error, activame de nuevo para continuar")
    except KeyboardInterrupt:
        print("Adioooooos...")
    except Exception as e:
        print(e)
start()