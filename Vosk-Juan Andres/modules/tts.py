import gtts
import playsound
def talk(text:str):
    model = gtts.gTTS(text,lang = "es")
    model.save("./audio.mp3")
    print("todo chevere")
    try:
        playsound.playsound("./audio.mp3")
    except Exception as e:
        print("No se puedo reproducir el audio")