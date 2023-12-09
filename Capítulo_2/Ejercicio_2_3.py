from Ejercicio_2_2 import Array

maxSize = 10
arr = Array(maxSize)

# Insert numbers into the array
arr.insert(77)
arr.insert(99)
arr.insert(44)
arr.insert(55)
arr.insert(12)
arr.insert(100)
arr.insert(3)

for i in range(len(arr)):
    elem = arr.get(i)
    if isinstance(elem, (int, float)):
        print(elem)