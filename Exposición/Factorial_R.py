def factorial(n):
    if n == 0 or n == 1:
        print(f"Factorial de {n} es 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Multiplicar {n} por el factorial de {n-1}, es ahora {result//n}")
        print(f"Factorial de {n} es {result}")
        return result

print(factorial(5))