# 1)Función recursiva que calcule el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 2)Función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 3)Función recursiva para calcular la potencia de un número
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# 4)Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    binario = decimal_a_binario(n)
    return binario if binario else '0'

# 5)Función recursiva para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# 6)Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

# 7)Función recursiva para contar los bloques de una pirámide
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# 8)Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
