#punto 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#punto 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#punto 3 
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#punto 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#punto 5
password = input("Ingrese su contraseña: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#punto 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

    #punto7
    texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

#punto8
nombre = input("Ingrese su nombre: ")
opcion = input("Seleccione opción (1-Mayúsculas, 2-minúsculas, 3-Primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

#punto 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#punto 10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación es: {estacion}")


