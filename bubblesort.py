array = [9,4,6,10,23,5,3]


n = len(array)

for i in range(n):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

lista = ["a", "o", "e", "u", "i"]

n = len(lista)

for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)


