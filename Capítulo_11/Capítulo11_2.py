import random

class HashTable:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
        self.contador_desplazados = 0

    def hash(self, clave):
        raise NotImplementedError

    def insertar(self, clave):
        indice = self.hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = clave
        else:
            self.contador_desplazados += 1
            self.insertar_sonda(clave, indice)

    def insertar_sonda(self, clave, indice):
        while self.tabla[indice] is not None:
            indice = (indice + 1) % self.tamaño
        self.tabla[indice] = clave

class HashTablePlegamiento3(HashTable):
    def hash(self, clave):
        suma = 0
        while clave > 0:
            grupo = clave % 1000
            suma += grupo
            clave //= 1000
        return suma % self.tamaño

class HashTablePlegamiento2(HashTable):
    def hash(self, clave):
        suma = 0
        while clave > 0:
            grupo = clave % 100
            suma += grupo
            clave //= 100
        return suma % self.tamaño

def probar_tablas_hash():
    factores_carga = [0.5, 0.7, 0.9]
    tablas_hash = [HashTablePlegamiento3, HashTablePlegamiento2]
    for fc in factores_carga:
        for tabla_hash in tablas_hash:
            tamaño = int(1000 / fc)
            tabla = tabla_hash(tamaño)
            claves = random.sample(range(10000000000), 1000)
            for clave in claves:
                tabla.insertar(clave)
            print(f"{tabla_hash.__name__} con factor de carga {fc}: {tabla.contador_desplazados} claves desplazadas")

probar_tablas_hash()