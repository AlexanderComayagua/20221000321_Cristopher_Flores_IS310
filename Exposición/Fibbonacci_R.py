import timeit

def fibbR(n):
    if n <= 0:
        return "La entrada debe ser mayor que 0"
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibbR(n-1) + fibbR(n-2)

def medir_tiempo():
    resultado = fibbR(10)
    print("El resultado es:", resultado)

# Medición del tiempo de ejecución
tiempo = timeit.timeit(medir_tiempo, number=10000)
print("Tiempo de ejecución:", tiempo)