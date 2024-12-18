import gtts
import playsound
def talk(text):
    model = gtts.gTTS(text,lang='es')
    model.save("audio.mp3")
    print('todo chevere')
    try:
        playsound.playsound('C:/Users/Ada-Amarillo/Desktop/jesus/Constructores/proyecto-1/stan-jesu/audio.mp3')
    except Exception as e:
        print("No se pudo reproducir el audio")