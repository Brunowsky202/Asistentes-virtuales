import queue 
import sys
import sounddevice
import json
from vosk import Model, KaldiRecognizer

# Inicializa el maejo de audio
q = queue.Queue()

# Parametros que normalmente se usan
device_id = None
sample_rate = 16000
model_lang = "models/vosk-model-small-es-0.42"

# Modelo de lenguaje que reconocera el audio
model = Model(model_lang)

#define el callback para el audio
def callback(indata, frames, time, status):
    q.put(bytes(indata))

def key_word(word="epa"):
    try:
        with sounddevice.RawInputStream(samplerate=sample_rate, 
                                        blocksize=8000, 
                                        device=device_id, 
                                        dtype='int16', 
                                        channels=1, 
                                        callback=callback):
            
            rec = KaldiRecognizer(model, sample_rate)

            print("Escuchando...")
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    text = json.loads(result)["text"]
                    print(text)
                    if word in text:
                        print("Palabra clave detectada:", word)
                        return True
                else:
                    partial_result = json.loads(rec.PartialResult())['partial']
                    print(partial_result)
                    if word in partial_result.lower():
                        print("Palabra clave detectada:", word)
                        return True
    except KeyboardInterrupt:
        print("\nDeteniendo...")
        sys.exit()
    except Exception as e:
        print("Error:", e)
        sys.exit()
