import timeit

def fibbR(n):
    x1=0
    x2=1
    if n <= 0:
        return "La entrada debe ser mayor que 0"
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2,n):
        sum=x1+x2
        x1=x2
        x2=sum
    return x2

def medir_tiempo():
    resultado = fibbR(10)
    print("El resultado es:", resultado)

# Medición del tiempo de ejecución
tiempo = timeit.timeit(medir_tiempo, number=10000)
print("Tiempo de ejecución:", tiempo)