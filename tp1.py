#Actividad1

print("Hola Mundoo!")

#Actividad2
nombre = input("Ingrese su nombre ")

print(f"Hola {nombre}!")
#Actividad3

import math
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad  ")
lugarResidencia = input("Ingrese lugar de procedencia")
print(f"Hola, Soy {nombre} {apellido}, tengo {edad} y soy de {lugarResidencia}")
#Actividad4
radio = float(input("Ingrese el radio del circulo "))
area = math.pi * (radio **2)
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#Actividad5
segundos = float(input("Ingrese cantidad de segundo"))
horas = segundos/3600
print("Equivale a", horas , "horas")

#Actividad6
numero = int(input("Ingrese un numero"))
print("tabla de multiplicar del" , numero)
print(numero, "x 1 =" , numero * 1)
print(numero, "x 2 =" , numero * 2)
print(numero, "x 3 =" , numero * 3)
print(numero, "x 4 =" , numero * 4)
print(numero, "x 5 =" , numero * 5)
print(numero, "x 6 =" , numero * 6)
print(numero, "x 7 =" , numero * 7)
print(numero, "x 8 =" , numero * 8)
print(numero, "x 9 =" , numero * 9)
print(numero, "x 10 =" , numero * 10)

#Actividad7
numero1 = int(input("Ingrese un numero entero distinto a 0"))
numero2 = int(input("Ingrese otro numero entero distinto a 0"))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print("El resultado de la suma de ambos numero es: ", suma)
print("El resultado de la suma de ambos numero es: ", resta)
print("El resultado de la suma de ambos numero es: ", division)
print("El resultado de la suma de ambos numero es: ", multiplicacion)

#Actividad8
altura = float(input("Ingrese su altura "))
peso = float(input ("Ingrese su peso "))
IMC = peso / (altura**2)
print("Su indice de masa muscular es :", IMC)

#Actividad9
temperatura = float(input("Ingrese temperatura en grados celsius"))
temperatura_fahrenheit = (9/5 * temperatura + 32)
print("Su equivalente en grados fahrenheit es: ", temperatura_fahrenheit)

#Actividad10
numero1 = float(input("Ingrese el primer numero "))
numero2 = float(input("Ingrese el segundo numero "))
numero3 = float(input("Ingrese el tercer numero "))
promedio = (numero1 + numero2 + numero3) / 3
print("El promedio de dichos numeros es: ", promedio)