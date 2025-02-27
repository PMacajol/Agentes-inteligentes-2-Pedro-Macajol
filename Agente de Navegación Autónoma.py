from collections import deque

# Definir el laberinto (0 = camino, 1 = pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Posición inicial y meta
inicio = (0, 0)
meta = (4, 4)

# Función de búsqueda BFS
def bfs(laberinto, inicio, meta):
    cola = deque([inicio])
    padres = {inicio: None}
    while cola:
        actual = cola.popleft()
        if actual == meta:
            break
        for direccion in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            siguiente = (actual[0] + direccion[0], actual[1] + direccion[1])
            if 0 <= siguiente[0] < 5 and 0 <= siguiente[1] < 5:
                if laberinto[siguiente[0]][siguiente[1]] == 0 and siguiente not in padres:
                    cola.append(siguiente)
                    padres[siguiente] = actual
    # Reconstruir la ruta
    ruta = []
    while actual:
        ruta.append(actual)
        actual = padres[actual]
    ruta.reverse()
    return ruta

# Obtener y mostrar la ruta
ruta = bfs(laberinto, inicio, meta)
print("Ruta encontrada:", ruta)