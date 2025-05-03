# nombre = "Diangel"
# numero = 5
# numero2 = 3
# resultado = numero + numero2
# print(resultado)
# division = resultado / 2
# print(division)

# usuario = "Diangel_04"
# contrasena = "28742099"

# pregunta1 = input("Ingrese su usuario: ")
# pregunta2 = input("Ingrese su contrasena: ")

# if usuario == pregunta1 and contrasena == pregunta2:
#     print("Usuario y contrasena validos.")
# else:
#     print("Acceso negado.")

# nume = int(input("Ingrese un numero: "))

# if nume < 0:
#     print("El numero es negativo.")
# elif nume > 0:
#     print("El numero es positivo.")
# else:
#     print("El numero es cero.")

# if nume % 2 == 0:
#     print("el numero es par.")
# else:
#     print("El numero es impar.")

# nume1 = int(input("Ingrese un numero: "))
# nume2 = int(input("Ingrese un numero: "))
# nume3 = int(input("Ingrese un numero: "))

# if nume1 > nume2 and nume1 > nume3:
#     print("El primer numero es el mayor.")
# elif nume2 > nume1 and nume2 > nume3:
#     print("El segundo numero es el mayor.")
# else:
#     print("El tercer numero es el mayor.")

# for i in range(0,100+1):
#     print(i)

# for i in range(0,101):
#     if i % 2 == 0:
#         print(i)

# suma = 0

# for i in range(0,251):
#     if i % 2 == 0:
#         suma += i

# print(suma)

# Hacer un programa que me imprima "Fizz" cuando el num sea multiplo de 3, que imprima "buzz" cuando sea multiplo de 5 y que imprima "Fizzbuzz" si el num es multiplo de 3 y 5. Si no es ninguno de los casos, que imprima el numero solamente. Desde 0 al 100.

for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz.")
    elif i % 3 == 0:
        print("Fizz.")
    elif i % 5 == 0:
        print("Buzz.")
    else:
        print(i)

#Crea un programa que convierta una cantidad en bolivares en dolares o euros (según el tipo de cambio de definas en una variable.)

# bolivares = float(input("Ingrese la cantidad de bs que desea cambiar: "))

# dolar = 69.50
# cambio = bolivares / dolar

# print(f'El cambio de bs a dolares es: {cambio}')

# Hacer un programa que pida tres numeros que calcule el promedio y lo muestre en pantalla.

# nume_1 = int(input("Ingrese un numero: "))
# nume_2 = int(input("Ingrese un numero: "))
# nume_3 = int(input("Ingrese un numero: "))

# prome = (nume_1 + nume_2 + nume_3 ) / 3

# print(f'El promedio de los numeros ingresados es: {prome}')



#Escribe un programa que intercambie los valores de dos varibles.

# a = 3
# b = 5

# a, b = b, a
# print(a, b)


# Condicionales

# Escribe un programa que pida la edad de una persona y muestre un mensaje si es un nino (menor de 12 años), adolecente (13-17), adulto (18-64) o adulto mayor (65 o mas anos.)

# edad = int(input("Ingrese su edad: "))

# if edad <= 12:
#     print("Es nino.")
# elif edad >= 13 and edad <= 17:
#     print("Es adolecente.")
# elif edad >= 18 and edad <= 64 :
#     print("Eres adulto.")
# else :
#     print("Eres adulto mayor.")

#crea un programa que le pida al usuario el monto total de una compra y le calcule el descuento segun lo sienguiente: Mas de mil el descuento de 10%, entre 500$ y 1000$ descuento de 5% y si es menor de 500 no hay descuento.

monto = float(input("Ingrese el monto a pagar: "))
descuento1 = monto * 0.10
descuento2 = monto * 0.05


if monto > 1000 :
    resultado = monto - descuento1
    print(f'Tiene un descuento del 10% en su compra y su monto a pagar es : {resultado}')
elif monto >= 500 and monto <= 1000:
    resultado = monto - descuento2
    print(f'Tiene un descuento de 5% en su compra y su monto a pagar es: {resultado}')
else :
    print(f'No tiene descuento, su monto a pagar es el mismo: {monto}')
    
    