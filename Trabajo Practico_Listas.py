#Trabajo Practico - Listas

#Ejercicio 1
#Lista con las notas de 10 estudiantes

notas = [7, 8, 6, 10, 9, 5, 8, 7, 9, 6]

#Mostrar la lista completa
print("Notas de los estudiantes:")
for nota in notas:
    print(nota)

#Calcular el promedio
promedio = sum(notas) / len(notas)
print("\nPromedio de notas:" , promedio)

#Mostrar la nota mas alta y mas baja
nota_max = max(notas)
nota_min = min(notas)
print("Nota mas alta:" , nota_max)
print("Nota mas baja:" , nota_min)

#Ejercicio 2
#Lista dee productos ingresados por el usuario

productos = []

#Pedir al usuario que ingrese 5 productos
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}:")
    productos.append(producto)

#Mostrar la lista original
print("\nLista original de productos:")
for p in productos:
    print("-" , p)    

#Ejercicio 3
#Generar una lista con 15 números enteros al azar entre 1 y 100

import random 

numeros = []
for i in range(15):
    n = random.randint(1,100)
    numeros.append(n)

#Mostrar la lista completa
print=("Lista de numero generados:")
for n in numeros:
    print(n, end="")
print("\n")  

#Crear listas para poner pares e impares
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)    

#Mostrar las listas
print("Numeros pares: ")
for p in pares:
    print(p, end="")

print("\n\nNumeros impares: ")
for i in impares:
    print(i, end="")    

#Mostrar cuantos tiene cada lista
print("\n\nCantidad de numero pares:", len(pares))
print ("Cantidad de numeros impares:", len(pares))

#Crear una nueva lista sin elementos repetidos.
valores = [4, 7, 2, 4, 9, 7, 1, 2, 6, 4, 9]

print("Lista original con repetidos:")
for v in valores:
    print(v, end="")

sin_repetidos= []

for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)

print("\n\nLista sin repetidos:")
for v in sin_repetidos:
    print(v, end="")

#Crear una lista con los nombres de 8 estudiantes presentes en clase
estudiantes = ["Ana", "Bruno", "Camila", "Diego", "Elena", "Facundo", "Gisella", "Hugo"]

print("Lista actual de estudiantes:")
for e in estudiantes:
    print("-", e)

#Preguntar qué desea hacer el usuario
accion = input("\n¿Queres agregar o eliminar un estudiante? (escribir 'agregar' o 'eliminar')")

if accion == "agregar":
   nuevo = input("Ingresa el nombre del nuevo estudiante:") 
   estudiantes.append(nuevo)
   print(f"\n{nuevo} fue agregado a la lista. ")

elif accion == "eliminar":
   borrar = input("Ingresa el nombre del estudiante que quieres eliminar")
   if borrar in estudiantes:
       estudiantes.remove(borrar)
       print(f"\n{borar} fue eliminado de la lista. ")

   else:
       print(f"\n'{borrar}' no se encuentra en la lista")   

else:
    print("\nOpcion invalida. Solo puede escribir 'agregar' o 'eliminar'.")

#Mostrar la lista final actualizada.
print("\nLista final de estudiantes: ")
for e in estudiantes:
    print("-", e )

#Ejercicio 6
#  Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).      

#Lista original

numeros = [3, 7, 9, 2, 8, 5, 1]

print("Lista original:")
for n in numeros:
    print(n, end="")

#Guardar el ultimo elemento
ultimo = numeros[-1]

#Mover los demas elementos hacia la derecha
for i in range(len(numeros) -1, 0, -1):
    numeros[i] = numeros [i - 1]

#Poner el ultimo como el primero
numeros[0] = ultimo

#Mostrar la lista rotada
print("\nLista rotada un lugar hacia la derecha:")
for n in numeros:
    print(n, end="")

#Ejercicio 7
#Matriz de temperaturas mínimas y máximas

temperaturas = [
    [12, 25],  # Día 1
    [10, 22],  # Día 2
    [14, 27],  # Día 3
    [9, 24],   # Día 4
    [11, 21],  # Día 5
    [13, 26],  # Día 6
    [10, 20]   # Día 7
]

# Mostrar las temperaturas día por día
print("Temparaturas minima y maximas de la semana:")
for i in range(7):
    print(f"Dia {i+1}: {temperaturas[i][0]}° / {temperaturas[i][1]}°")

#Calcular los promedios
suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min += dia[0] 
    suma_max += dia[1]

prom_min = suma_min / 7
prom_max = suma_max / 7

print(f"\nPromedio de minimas: {prom_min:.2f}°")
print(f"Promedio de maximas: {prom_max:.2f}°")

#Calcular amplitud térmica (max - min) de cada día
amplitudes = []
for dia in temperaturas:
    amplitud = dia[1] - dia[0]
    amplitudes.append(amplitud)

#Buscar el día con mayor amplitud
mayor_amplitud = max(amplitudes)   
dia_max = amplitudes.index(mayor_amplitud) + 1

print(f"\nLa mayor amplitud térmica fue de {mayor_amplitud}° el día {dia_max}.")


#Ejercicio 8
#Matriz de notas de 5 estudiantes en 3 materias

#Matriz: cada fila representa a un estudiante y cada columna a una materia
notas = [
    [7, 8, 6],  # Estudiante 1
    [9, 5, 8],  # Estudiante 2
    [6, 7, 7],  # Estudiante 3
    [8, 9, 10], # Estudiante 4
    [5, 6, 6]   # Estudiante 5
]

# Mostrar todas las notas
print("Notas de los estudiantes (Materia 1 / Materia 2 / Materia 3):")
for i in range(5):
    print(f"Estudiante {i+1}: {notas[i]}")

# Promedio de cada estudiante (fila)
print("\nPromedio de cada estudiante:")
for i in range(5):
    suma = sum(notas[i])
    promedio = suma / len(notas[i])
    print(f"Estudiante {i+1}: {promedio:.2f}")

# Promedio de cada materia (columna)
print("\nPromedio de cada materia:")
for j in range(3):
    suma_materia = 0
    for i in range(5):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / 5
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#Ejercicio 9
#Tablero de Ta-Te-Ti

#Crear una matriz 3x3 con guiones
tablero = [["-" for _ in range(3)] for _ in range(3)]

#Mostrar el tablero inicial
print("Tablero inicial:")
for fila in tablero:
    print(fila)

#Dos jugadas (una de cada jugador)
for turno in range(2):
    print(f"\nTurno {turno+1}")
    
    if turno % 2 == 0:
        simbolo = "X"  #jugador 1
    else:
        simbolo = "O"  #jugador 2
    
    fila = int(input(f"Ingrese la fila (0, 1 o 2) para {simbolo}: "))
    columna = int(input(f"Ingrese la columna (0, 1 o 2) para {simbolo}: "))

    #Validar que la posición esté libre
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = simbolo
    else:
        print("Esa casilla ya está ocupada. Se pierde el turno.")

    #Mostrar el tablero actualizado
    print("\nTablero actualizado:")
    for fila_tablero in tablero:
        print(fila_tablero)

 
 
#Ejercicio 9 
#Lista de 10 números enteros

#Lista con valores
numeros = [15, 8, 22, 5, 17, 10, 13, 19, 25, 7]

print("Lista de números:")
for n in numeros:
    print(n, end=" ")

#Calcular el mayor y el menor
mayor = max(numeros)
menor = min(numeros)

#Calcular el promedio
promedio = sum(numeros) / len(numeros)

#Mostrar los resultados
print(f"\n\nEl número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"El promedio es: {promedio:.2f}")       