#Ejercicio1
with open("productos.txt", "w") as archivo:
     archivo.write("Lapicera,120,30\n")
     archivo.write("Cuaderno,320,15\n")
     archivo.write("Goma,50,40\n")

#Ejercicio2
#Leer y mostrar productos

with open("productos.txt", "r") as archivo:
    for linea in archivo:
     nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio3
#Agregar productos dese teclado

nombre = input("Ingrese el nombre del nuevo producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
     archivo.write(f"{nombre}, {precio}, {cantidad}\n2")

#Ejercicio4
#Cargar productos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

#Ejercicio5
#Buscar producto por nombre

buscado =input ("Ingrese nombre del producto")

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado.lower():
     print(f"Producto: {p["nombre"]} | Precio: ${p["precio"]} | Cantidad: {p["cantidad"]}")
    encontrado = True
    break

if not encontrado:
    print("Producto no encontrado.")

#Ejercicio6
#Guardar los productos actualizados

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo 'productos.txt' actualizado correctamente.")


