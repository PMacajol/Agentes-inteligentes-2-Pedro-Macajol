# Definir el entorno con recompensas
entorno = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función de utilidad (suma de recompensas)
def calcular_utilidad(ruta):
    return sum(entorno[fila][columna] for fila, columna in ruta)

# Encontrar la mejor ruta (ejemplo: de (0,0) a (2,2))
def mejor_ruta(entorno):
    rutas_posibles = [
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # Ruta 1
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # Ruta 2
        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]   # Ruta 3
    ]
    mejor = max(rutas_posibles, key=calcular_utilidad)
    return mejor

# Obtener y mostrar la mejor ruta
ruta_optima = mejor_ruta(entorno)
print("Ruta óptima:", ruta_optima)
print("Utilidad:", calcular_utilidad(ruta_optima))