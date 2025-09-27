#números enteros desde 0 hasta 100

for i in range(101):
    print(i)

#contar digitos de un numero

numero = int(input("Ingrese un número entero: "))
cantidad = len(str(abs(numero)))  # abs para manejar negativos
print("Cantidad de dígitos:", cantidad)

#suma entre dos valores (excluyéndolos)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(a+1, b):
    suma += i

print("La suma de los números entre", a, "y", b, "es:", suma)

#adivinar número aleatorio

import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print("¡Correcto!", intentos, "intentos.")
        break

#Pares del 100 al 0 en orden decreciente

for i in range(100, -1, -2):
    print(i)

#suma de números desde 0 hasta N

n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n+1):
    suma += i
print("La suma de los números desde 0 hasta", n, "es:", suma)

#contador de pares, impares, positivos y negativos

n = 100  # cambiar a un número menor para probar
pares = impares = positivos = negativos = 0

for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#media de 100 números

n = 100  # cambiar a un número menor para probar
suma = 0

for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / n
print("La media es:", media)

#invertir los dígitos de un número

numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
