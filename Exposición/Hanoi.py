def hanoi_iterativo(numero_discos, origen, destino, auxiliar):
    torres = [[], [], []]  # Representación de las 3 torres como listas vacías
    torres[origen - 1] = list(range(numero_discos, 0, -1))  # Colocar los discos en la torre de origen

    # Mostrar las torres inicialmente
    print_torres(torres)

    # Calcular el número total de movimientos
    total_movimientos = 2**numero_discos - 1

    # Realizar los movimientos iterativamente
    for movimiento in range(1, total_movimientos + 1):
        if movimiento % 3 == 1:
            mover_disco(torres, origen, destino)
        elif movimiento % 3 == 2:
            mover_disco(torres, origen, auxiliar)
        elif movimiento % 3 == 0:
            mover_disco(torres, auxiliar, destino)

        # Mostrar las torres después de cada movimiento
        print_torres(torres)

def mover_disco(torres, origen, destino):
    disco = torres[origen - 1].pop()
    torres[destino - 1].append(disco)

def print_torres(torres):
    for torre in torres:
        print(torre)

# Ejemplo de uso con 3 discos
hanoi_iterativo(3, 1, 3, 2)

