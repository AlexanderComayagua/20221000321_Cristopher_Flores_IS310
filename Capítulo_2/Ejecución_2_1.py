from Ejercicio_2_1 import Array

maxSize = 10
arr = Array(maxSize)

# Insert various data types including numbers, strings, and zeros
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Max number in the array:", arr.getMaxNum())