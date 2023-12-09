def factorial(n):
    stack = []
    result = 1
    for i in range(1, n+1):
        stack.append(i)
    while stack:
        num = stack.pop()
        result *= num
        print(f"Multiplicando {num} al resultado, ahora es {result}")
    return result

print(factorial(5))