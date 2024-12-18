import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json

# Initialize Vosk model
model = Model(lang="es")
recognizer = KaldiRecognizer(model, 16000)  # 16kHz sample rate

# Queue for audio data
q = queue.Queue()

def callback(indata, frames, time, status):
    """Sounddevice callback to handle real-time audio chunks."""
    q.put(bytes(indata))


# Configure VAD parameters
silence_duration = 1.5  # seconds of silence to assume end of speech

def transcribes():
    """Listen to audio in real-time, process with VAD, and transcribe."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        print("Escuchando...")
        silence_counter = 0
        final_text = ""
        
        while True:
            data = q.get()
            
            # Perform voice activity detection
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())['text']
                silence_counter = 0
                final_text += f" {result}"
            else:
                partial = json.loads(recognizer.PartialResult())['partial']
                if partial == "":
                    silence_counter += 1
            # Check if silence has been detected for enough time
            if silence_counter > silence_duration * (16000 / 8000):  # convert to frames
                print("Silence detected, stopping...")
                break

        # Send the final text to the AI model
        if final_text != "":
            print("Listo!")
            return final_text
        else: 
            print("Listo!")
            return ""