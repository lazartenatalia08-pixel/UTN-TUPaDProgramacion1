precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Añadir las siguientes frutas con sus respectivos precios
precios_frutas = ['Naranja'] = 1200
precios_frutas = ['Manzana'] = 1500
precios_frutas = ['Pera'] = 2300

#Actualizar los precios
precios_frutas = ['Banana'] = 1330
precios_frutas = ['Manzana'] = 1700
precios_frutas = ['Melón'] = 2800

#crear una lista que contenga únicamente las frutas sin los precios. 
lista_frutas = list(precios_frutas.keys())

#Almacenar y consultar números telefónicos
#1 Cargar contactos

directorio = {}
print("Ingrese 5 contactos: ")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    numero = input(f"Numero de {nombre}: ")

directorio[nombre] = numero 

#Consultar un numero
nombre_a_consultar = input("\nIngrese el nombre a consultar: ")

#Mostrar el numero
numero_encontrado = directorio.get(nombre_a_consultar)

if numero_encontrado:
    print(f"El numero de {nombre_a_consultar} es {numero_encontrado}")
else:
    print(f"El contacto '{nombre_a_consultar}' no se encuentra en el directorio ") 

#5) Solicita al usuario una frase 

frase = input("Ingrese una frase").lower()

#Separar la frase en palabras
palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

#6)Promedio de alumnos
alumnos = {}
num_alumnos = 3
num_notas = 3

print("Ingrese los nombres y las notas de 3 alumnos: ")
for i in range(num_alumnos):
    nombre = input("Nombre del alumno {i+1}: ")

notas_lista = []
for j in range(num_notas):
    while True:
        try:
            nota = int(input(f"Nota {j+1} para {nombre}: "))
            notas_lista.append(nota)
            break
        except ValueError:
            print("Por favor, ingrese un numero entero")

alumnos[nombre] = tuple(notas_lista)
print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"- {nombre}: {promedio:.2f}")

#Ejercicio 7 
parcial1 = {'Ana', 'Pedro', 'Sofía', 'Luis', 'Juan', 'Marta'}
parcial2 = {'Ana', 'Pedro', 'Carlos', 'Elena', 'Sofía', 'Marta'}

print("Análisis de estudiantes que aprobaron:")

ambos_parciales = parcial1.intersection(parcial2)
print(f"- Aprobaron ambos: {ambos_parciales}")

#Estudiantes que aprobaron solo uno de los dos (Diferencia Simétrica)
solo_uno = parcial1.symmetric_difference(parcial2)
print(f"- Aprobaron solo uno: {solo_uno}")

#Lista total de estudiantes que aprobaron al menos un parcial (Unión)
total_aprobados = parcial1.union(parcial2)
print(f"Total de aprobados (al menos uno): {total_aprobados}")

#Ejercicio 8
stock_productos = {'Teclado': 15, 'Mouse': 20, 'Monitor': 8}

def gestionar_stock():
    global stock_productos
    print("\nGestión de Stock:")
    
    producto = input("Ingrese el nombre del producto: ").capitalize()
    
    if producto in stock_productos:
        print(f"Stock actual de {producto}: {stock_productos[producto]} unidades.") 
        
        accion = input("¿Desea agregar unidades (A) o salir (S)? ").upper()
        if accion == 'A':
            while True:
                try:
                    unidades = int(input(f"¿Cuántas unidades de {producto} desea agregar?: "))
                    if unidades >= 0:
                        stock_productos[producto] += unidades #Agregar unidades al stock existente
                        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades.")
                        break
                    else:
                        print("Ingrese un número positivo.")
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")
    else:
        print(f"El producto '{producto}' no existe en el stock.")
        
        #Agregar nuevo producto
        accion = input("¿Desea agregar este producto (A) o salir (S)? ").upper()
        if accion == 'A':
            while True:
                try:
                    nuevo_stock = int(input(f"Ingrese el stock inicial para {producto}: "))
                    if nuevo_stock >= 0:
                        stock_productos[producto] = nuevo_stock #Agregar nuevo producto
                        print(f"Producto '{producto}' agregado con stock inicial de {nuevo_stock}.")
                        break
                    else:
                        print("Ingrese un número positivo.")
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")
    
#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión de planificación",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Entrenamiento en gimnasio",
    ("viernes", "18:00"): "Cena con amigos"
}

print("Consulta de Agenda:")

dia_consulta = input("Ingrese el día (ej: lunes): ").lower()
hora_consulta = input("Ingrese la hora (ej: 10:00): ")

#Crear la clave de tupla para la consulta
clave_consulta = (dia_consulta, hora_consulta)

#Consultar la actividad (get() devuelve None si no existe la clave)
actividad = agenda.get(clave_consulta)

if actividad:
    print(f"La actividad para el {dia_consulta.capitalize()} a las {hora_consulta} es: '{actividad}'")
else:
    print(f"No hay actividad programada para el {dia_consulta.capitalize()} a las {hora_consulta}.")

#Ejercicio 10 
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo", "Perú": "Lima"}

invertido = {}

for pais, capital in original.items():
    #En el nuevo diccionario, la clave es la capital y el valor es el país
    invertido[capital] = pais

print("10) Diccionario original (País: Capital):")
print(original)
print("\nDiccionario invertido (Capital: País):")
print(invertido)





