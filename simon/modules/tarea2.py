import random

def generar_historia():
    personajes = ["un valiente caballero", "una astuta princesa", "un dragón feroz", "un mago sabio"]
    lugares = ["en un oscuro bosque", "en un castillo encantado", "en una montaña nevada", "en un pueblo tranquilo"]
    conflictos = ["luchando contra un monstruo", "buscando un tesoro perdido", "rescatando a un amigo", "descubriendo un secreto antiguo"]
    
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    conflicto = random.choice(conflictos)
    
    historia = f"Había una vez {personaje} {lugar}, {conflicto}. Y así comenzó una gran aventura."
    return historia

def guardar_historia_en_archivo(historia,tarea):
    with open(tarea, 'w') as archivo:
        archivo.write(historia)

# Generar la historia
historia = generar_historia()

# Guardar la historia en un archivo
nombre_archivo = "historia.txt"
guardar_historia_en_archivo(historia,guardar_historia_en_archivo)

print(f"La historia ha sido guardada en {guardar_historia_en_archivo}.")