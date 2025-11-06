#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Ejercicio 3
def informacion_pesonal(nombre, apellido, edad, residencia): 
    print(f"Soy {nombre}{apellido} , tengo {edad} años y vivo en {residencia}")

#Ejercicio 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Ejercicio 5 
def segundos_a_horas(segundos):
    return segundos / 3600

#Ejercicio 6
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7 
def operaciones_basicas(a, b):
    suma = a + b
    resta = a + b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return (suma, resta, multiplicacion, division)

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Ejercicio 9 
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


#Programa principal para probar las funciones
# 1
imprimir_hola_mundo()

# 2
nombre = input("\nIngrese su nombre: ")
print(saludar_usuario(nombre))

# 3
nombre = input("\nIngrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_pesonal(nombre, apellido, edad, residencia)

# 4
radio = float(input("\nIngrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5
segundos = int(input("\nIngrese la cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas.")

# 6
numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

# 8
peso = float(input("\nIngrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# 9
celsius = float(input("\nIngrese la temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

# 10
a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")


