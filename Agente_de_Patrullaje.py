import random

# Definir la ruta de patrullaje
ruta = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]

# Simular un obstáculo en una posición aleatoria
obstaculo = random.choice(ruta)

# Función del agente reflejo
def agente_reflejo(ruta, obstaculo):
    for posicion in ruta:
        if posicion == obstaculo:
            print(f"¡Obstáculo detectado en {posicion}! Cambiando dirección...")
            nueva_direccion = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # Moverse en una dirección aleatoria
            print(f"Nueva dirección: {nueva_direccion}")
        else:
            print(f"Patrullando en {posicion}")

# Ejecutar el agente
agente_reflejo(ruta, obstaculo)