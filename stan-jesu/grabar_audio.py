import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
duration = 10 # in second
file = "graba.wav"

audio = pyaudio.PyAudio()

def record_prompt():
    stream = audio.open(format=FORMAT, channels= CHANNELS,
                        rate = RATE, input=True, frames_per_buffer=CHUNK)
    print("Grabando...")
    frames = []

    for i in range(0,int(RATE/CHUNK*duration)):
        data=stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Audio grabado")
    wavefile = wave.open(file, 'wb')
    wavefile.setnchannels(CHANNELS)
    wavefile.setframerate(RATE)
    wavefile.setsampwidth(audio.get_sample_size(FORMAT))
    wavefile.writeframes(b''.join(frames))
    wavefile.close()