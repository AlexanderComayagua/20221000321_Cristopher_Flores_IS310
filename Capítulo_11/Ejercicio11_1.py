import random

class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
        self.contador_desplazados = 0

    def hash(self, clave):
        return clave % self.tamaño

    def insertar(self, clave):
        indice = self.hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = clave
        else:
            self.contador_desplazados += 1
            self.insertar_sonda(clave, indice)

    def insertar_sonda(self, clave, indice):
        raise NotImplementedError

class TablaHashSondaLineal(TablaHash):
    def insertar_sonda(self, clave, indice):
        while self.tabla[indice] is not None:
            indice = (indice + 1) % self.tamaño
        self.tabla[indice] = clave

class TablaHashSondaCuadrática(TablaHash):
    def insertar_sonda(self, clave, indice):
        i = 1
        while self.tabla[indice] is not None:
            indice = (indice + i**2) % self.tamaño
            i += 1
        self.tabla[indice] = clave

class TablaHashSondaDoble(TablaHash):
    def __init__(self, tamaño):
        super().__init__(tamaño)
        self.paso = 7

    def hash2(self, clave):
        return self.paso - (clave % self.paso)

    def insertar_sonda(self, clave, indice):
        while self.tabla[indice] is not None:
            indice = (indice + self.hash2(clave)) % self.tamaño
        self.tabla[indice] = clave

def probar_tablas_hash():
    factores_carga = [0.5, 0.7, 0.9]
    sondas = [TablaHashSondaLineal, TablaHashSondaCuadrática, TablaHashSondaDoble]
    for fc in factores_carga:
        for sonda in sondas:
            tamaño = int(200 / fc)
            tabla = sonda(tamaño)
            claves = random.sample(range(1000), 200)
            for clave in claves:
                tabla.insertar(clave)
            print(f"{sonda.__name__} con factor de carga {fc}: {tabla.contador_desplazados} claves desplazadas")

probar_tablas_hash()