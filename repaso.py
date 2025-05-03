# variables

# Variables
# Variables son espacios de memoria que almacenan datos

# Ejemplo de variables
nombre = "Juan" # Variable de tipo string (cadena de texto)
edad = 25 # Variable de tipo entero (número entero)
altura = 1.75 # Variable de tipo float (número decimal)

# Tipos de datos

# int: número entero
numero_entero = 10 # Ejemplo de variable de tipo entero
# float: número decimal
numero_decimal = 10.5 # Ejemplo de variable de tipo decimal
# str: cadena de texto
texto = "Hola, mundo!" # Ejemplo de variable de tipo string
# bool: verdadero o falso (True o False)
booleano = True # Ejemplo de variable de tipo booleano

# Operadores aritméticos
# +: suma   
# -: resta
# *: multiplicación
# /: división
# %: módulo (resto de la división)
# **: potencia (exponente)
# //: división entera (sin decimales)

# Ejemplo de operadores aritméticos
suma = 10 + 5 # Suma de 10 y 5
print(suma) # Imprime el resultado de la suma
resta = 10 - 5 # Resta de 10 y 5
print(resta) # Imprime el resultado de la resta
multiplicacion = 10 * 5 # Multiplicación de 10 y 5
print(multiplicacion) # Imprime el resultado de la multiplicación
division = 10 / 5 # División de 10 entre 5
print(division) # Imprime el resultado de la división
modulo = 10 % 3 # Módulo de 10 entre 3 (resto de la división)
print(modulo) # Imprime el resultado del módulo
potencia = 10 ** 2 # Potencia de 10 elevado a 2 (10 al cuadrado)
print(potencia) # Imprime el resultado de la potencia
division_entera = 10 // 5 # División entera de 10 entre 3 (sin decimales)
print(division_entera) # Imprime el resultado de la división entera

# Operadores de comparación
# ==: igual
# !=: diferente
# >: mayor que
# <: menor que
# >=: mayor o igual que
# <=: menor o igual que

# Ejemplo de operadores de comparación
comparacion_igual = (10 == 10) # True (10 es igual a 10)
comparacion_diferente = (10 != 5) # True (10 es diferente de 5)
comparacion_mayor = (10 > 5) # True (10 es mayor que 5)
comparacion_menor = (10 < 5) # False (10 no es menor que 5)
comparacion_mayor_igual = (10 >= 10) # True (10 es mayor o igual que 10)

# Operadores lógicos
# and: y (ambas condiciones deben ser verdaderas)
# or: o (al menos una condición debe ser verdadera)
# not: no (invierte el valor de verdad de una condición)

# Ejemplo de operadores lógicos
condicion1 = True
# Condición 1
condicion2 = False # Condición 2

# and

# Ejemplo de operador lógico AND
resultado_and = condicion1 and condicion2 # False (ambas condiciones no son verdaderas)

# or
# Ejemplo de operador lógico OR
resultado_or = condicion1 or condicion2 # True (al menos una condición es verdadera)

# not 
# Ejemplo de operador lógico NOT
resultado_not = not condicion1 # False (invierte el valor de verdad de la condición 1)

# operadores de asignación
# =: asignación simple
# +=: suma y asignación (a = a + b)
# -=: resta y asignación (a = a - b)
# *=: multiplicación y asignación (a = a * b)
# /=: división y asignación (a = a / b)
# %= : módulo y asignación (a = a % b)
# **= : potencia y asignación (a = a ** b)
# //= : división entera y asignación (a = a // b)
#

a = 10
a %= 5 # Suma y asignación (a = a + 5)
print(a) # Imprime el resultado de la suma y asignación
# Ejemplo de operadores de asignación
# a = 10 # Asignación simple
# a += 5 # Suma y asignación (a = a + 5)
# a -= 3 # Resta y asignación (a = a - 3)
# a *= 2 # Multiplicación y asignación (a = a * 2)
# a /= 4 # División y asignación (a = a / 4)
# a %= 3 # Módulo y asignación (a = a % 3)
# a **= 2 # Potencia y asignación (a = a ** 2)
# a //= 2 # División entera y asignación (a = a // 2)

# Condicionales
# if: si (condición verdadera)
# else: si no (condición falsa)
# elif: si no, si (otra condición verdadera)
#
# Ejemplo de condicionales
# edad = 18 # Variable de tipo entero (edad del usuario)
# if edad >= 18: # Si la edad es mayor o igual a 18
#     print("Eres mayor de edad.") # Imprime si la condición es verdadera
# else: # Si la condición es falsa
#     print("Eres menor de edad.") # Imprime si la condición es falsa

# Ejemplo de condicionales con elif
# edad = 15 # Variable de tipo entero (edad del usuario)
# if edad < 12: # Si la edad es menor a 12
#     print("Eres un niño.") # Imprime si la condición es verdadera
# elif edad >= 12 and edad < 18: # Si la edad es mayor o igual a 12 y menor a 18
#    print("Eres un adolescente.") # Imprime si la condición es verdadera
# elif edad >= 18 and edad < 65: # Si la edad es mayor o igual a 18 y menor a 65
#     print("Eres un adulto.") # Imprime si la condición es verdadera
# else: # Si la condición es falsa
#     print("Eres un adulto mayor.") # Imprime si la condición es falsa

# for

# El ciclo for se utiliza para iterar sobre una secuencia (lista, tupla, cadena de texto, etc.) o un rango de números.

#
# Ejemplo de ciclo for
# for wicho in range(1, 11): # Iteramos del 1 al 10
#     print("Contador:", wicho) # Imprimimos el valor de i

#
# while
# El ciclo while ejecuta un bloque de código mientras una condición sea verdadera.

#
# Ejemplo de ciclo while
# contador = 1 # Inicializamos el contador en 1
# while contador <= 10: # Mientras el contador sea menor o igual a 10
#     print("Contador:", contador) # Imprimimos el valor del contador
#     contador += 1 # Incrementamos el contador en 1

