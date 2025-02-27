import random

# Definir el entorno como una cuadrícula 5x5
entorno = [[(i, j) for j in range(5)] for i in range(5)]

# Estado interno: celdas visitadas
visitadas = set()

# Función del agente explorador
def agente_explorador(entorno):
    fila, columna = 0, 0  # Empezar en la esquina superior izquierda
    while len(visitadas) < 25:  # Explorar hasta visitar todas las celdas
        if (fila, columna) not in visitadas:
            print(f"Explorando celda: ({fila}, {columna})")
            visitadas.add((fila, columna))
        # Moverse aleatoriamente
        direccion = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        nueva_fila = fila + direccion[0]
        nueva_columna = columna + direccion[1]
        if 0 <= nueva_fila < 5 and 0 <= nueva_columna < 5:  # Verificar límites
            fila, columna = nueva_fila, nueva_columna

# Ejecutar el agente
agente_explorador(entorno)