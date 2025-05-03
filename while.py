# while

# El ciclo while ejecuta un bloque de código mientras una condición sea verdadera.

# contador = 1 # Inicializamos el contador en 1
# while contador <= 10: # Mientras el contador sea menor o igual a 5
#     print("Contador:", contador) # Imprimimos el valor del contador
#     contador += 1 # Incrementamos el contador en 1

# Uso de ciclo while cuando no sabes cuantas veces se va a repetir el ciclo

entrada = ''

# while entrada != 'salir': # Mientras la entrada no sea 'salir'
#     entrada = input("Escribe algo (escribe 'salir' para terminar): ") # Pedimos al usuario que escriba algo
#     print("Has escrito:", entrada) # Imprimimos lo que el usuario ha escrito

# Uso de ciclo for cuando sabes cuantas veces se va a repetir el ciclo

# for i in range(1, 11): # Iteramos del 1 al 10
#     print("Contador:", i) # Imprimimos el valor de i

# Ejemplo:

# Suma de dos numeros

# while True:
#     num1 = int(input("Introduce el primer número: ")) # Pedimos al usuario que introduzca el primer número
#     num2 = int(input("Introduce el segundo número: ")) # Pedimos al usuario que introduzca el segundo número

#     suma = num1 + num2 # Sumamos los dos números
#     print("La suma de", num1, "y", num2, "es:", suma) # Imprimimos la suma
#     siguiente = input("¿Quieres hacer otra suma? (si/no): ") # Preguntamos al usuario si quiere hacer otra suma

#     if siguiente != 'si':
#         print("¡Hasta luego!") # Si el usuario no quiere hacer otra suma, salimos del ciclo
#         break

# suma = 0
# numero = int(input("Introduce un número (0 para salir): ")) # Pedimos al usuario que introduzca un número

# while numero != 0: # Mientras el número no sea 0
#     suma += numero # Sumamos el número a la suma total (el operador += es una forma abreviada de escribir suma = suma + numero, donde suma es la variable que almacena la suma total y numero es el número que el usuario ha introducido)
#     numero = int(input("Introduce un número (0 para salir): ")) # Pedimos al usuario que introduzca otro número 

# print("La suma total es:", suma) # Imprimimos la suma total

# Suma de los numeros pares

suma = 0
for i in range(0,251):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares es:", suma) # Imprimimos la suma de los números pares

# suma de los pares desde 100 hasta 0

suma_par = 0
contador = 0 # Inicializamos el contador en 0

while contador <= 251:
    if contador % 2 == 0: # Si el contador es par
        suma_par += contador # Sumamos el contador a la suma de los números pares
    contador += 1 # Incrementamos el contador en 1

print("La suma de los números pares es:", suma_par) # Imprimimos la suma de los números pares

