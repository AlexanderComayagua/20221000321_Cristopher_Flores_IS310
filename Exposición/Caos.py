def gen_combos(word):
    n = len(word)
    combos = []

    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        combo = [word[j] for j in range(n) if binary[j] == '1']
        combos.append(combo)

    return combos, len(combos)

word = input("Ingrese una palabra: ")
combos, num_combos = gen_combos(word)

for combo in combos:
    print(combo)

print("Combinaciones posibles:", num_combos)