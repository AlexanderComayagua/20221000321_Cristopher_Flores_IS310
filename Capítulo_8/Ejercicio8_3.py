import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierda=None, derecha=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(mensaje):
    frecuencias = defaultdict(int)
    for simbolo in mensaje:
        frecuencias[simbolo] += 1

    heap = []
    for simbolo, frecuencia in frecuencias.items():
        nodo = NodoHuffman(simbolo, frecuencia)
        heapq.heappush(heap, nodo)

    while len(heap) > 1:
        nodo_izquierda = heapq.heappop(heap)
        nodo_derecha = heapq.heappop(heap)
        nodo_padre = NodoHuffman(frecuencia=nodo_izquierda.frecuencia + nodo_derecha.frecuencia,
                                 izquierda=nodo_izquierda, derecha=nodo_derecha)
        heapq.heappush(heap, nodo_padre)

    return heap[0]

def construir_tabla_codigos(nodo, codigo_actual="", tabla_codigos={}):
    if nodo is None:
        return tabla_codigos

    if nodo.simbolo is not None:
        tabla_codigos[nodo.simbolo] = codigo_actual

    tabla_codigos = construir_tabla_codigos(nodo.izquierda, codigo_actual + "0", tabla_codigos)
    tabla_codigos = construir_tabla_codigos(nodo.derecha, codigo_actual + "1", tabla_codigos)

    return tabla_codigos

def codificar_mensaje(mensaje, tabla_codigos):
    mensaje_codificado = ""
    for simbolo in mensaje:
        mensaje_codificado += tabla_codigos[simbolo]
    return mensaje_codificado

def decodificar_mensaje(mensaje_codificado, arbol_huffman):
    mensaje_decodificado = ""
    nodo_actual = arbol_huffman
    for bit in mensaje_codificado:
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.simbolo is not None:
            mensaje_decodificado += nodo_actual.simbolo
            nodo_actual = arbol_huffman

    return mensaje_decodificado

def mostrar_arbol_huffman(nodo, nivel=0):
    if nodo is None:
        return

    mostrar_arbol_huffman(nodo.derecha, nivel + 1)
    print(" " * 4 * nivel + "->", nodo.simbolo, nodo.frecuencia)
    mostrar_arbol_huffman(nodo.izquierda, nivel + 1)

mensaje = "Hola, mundo!"
arbol_huffman = construir_arbol_huffman(mensaje)
tabla_codigos = construir_tabla_codigos(arbol_huffman)
mensaje_codificado = codificar_mensaje(mensaje, tabla_codigos)
mensaje_decodificado = decodificar_mensaje(mensaje_codificado, arbol_huffman)

print("Mensaje original:", mensaje)
print("Mensaje codificado:", mensaje_codificado)
print("Mensaje decodificado:", mensaje_decodificado)
print("Número de bits en el mensaje codificado:", len(mensaje_codificado))
print("Número de caracteres en el mensaje original:", len(mensaje))

if len(mensaje) < 20:
    print("Árbol de Huffman:")
    mostrar_arbol_huffman(arbol_huffman)