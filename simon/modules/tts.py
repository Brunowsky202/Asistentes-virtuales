import gtts
import playsound
def talk(text:str):
    model = gtts.gTTS(text,lang='es')
    model.save("audio.mp3")
    print('todo chevere')
    playsound.playsound('audio.mp3')
    