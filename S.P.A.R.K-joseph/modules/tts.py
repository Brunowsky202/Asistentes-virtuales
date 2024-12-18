import gtts
import playsound
def talk(text):
    model = gtts.gTTS(text, lang="es")
    model.save("audio.mp3")
    print("Todo bien")
    playsound.playsound("audio.mp3")
