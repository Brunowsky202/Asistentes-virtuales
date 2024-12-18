import queue
import sys
import sounddevice
from vosk import KaldiRecognizer, Model 
import json

# Inicializa el manejo de audio 
q = queue.Queue()

# Parametros que normalmente se usan
device_id = None
sample_rate = 16000
model_lang = "models/vosk-model-small-es-0.42"

# Modelo de lenguaje que reconocera el audio
model = Model(model_lang)

def callback(indata, framas, time, status):
    q.put(bytes(indata))

def key_word(word = "epa"):
    try:
        with sounddevice.RawInputStream(samplerate=sample_rate,
                                        blocksize=8000,
                                        dtype="int16",
                                        channels=1,
                                        callback=callback):

            rec = KaldiRecognizer(model, sample_rate)
            print(f"Escuchando: {word}")
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    text = json.loads(result)['text']
                    if word in text:
                        print("Palabra clave detectada")
                        return True

                else:
                    partial_result = json.loads(rec.PartialResult())['partial']
                    if word in partial_result.lower():
                        print("Palabra clave detectada")
                        return True
    except KeyboardInterrupt:
        print("Cerrando...")
        sys.exit(0)
    except Exception as e:
        print("Error:", e) 
        sys.exit()                          
