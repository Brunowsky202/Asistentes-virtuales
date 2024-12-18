from gemini import answer
from grabar_audio import record_prompt
from on_talk import listen
import sys
try:
    while True:
        if listen('hello'):
            while True:
                try:
                    record_prompt()
                    answer()
                except Exception as  e:
                    print("Mira pedazo de animal, aprende a hablar primero y depues me activas")
                    break
except KeyboardInterrupt:
    print("Programa finalizado")
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()