# utils.py

import grafo

def generar_matriz_adyacencia(grafo):
    # Encontrar el nodo con el valor más alto para determinar el tamaño de la matriz
    nodos = set(grafo.keys()) | set([n for sublist in grafo.values() for n in sublist])
    max_nodo = max(nodos)

    # Crear una matriz de adyacencia cuadrada
    matriz = [[0 for _ in range(max_nodo)] for _ in range(max_nodo)]

    # Llenar la matriz de adyacencia
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            matriz[nodo - 1][vecino - 1] = 1  # Ajuste por indexación en Python

    # Convertir la matriz a una cadena de texto con comas y saltos de línea
    matriz_texto = "\n".join([",".join(map(str, fila)) for fila in matriz])
    return matriz_texto

# Usar la función y obtener la matriz de adyacencia
matriz_adyacencia = generar_matriz_adyacencia(grafo.grafo)
print(matriz_adyacencia)
