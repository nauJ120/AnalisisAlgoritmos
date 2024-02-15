# Problema 1: Multiples of 3 or 5 con un enfoque iterativo en lugar de comprensión de listas
def problem_1(limit):
    total = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

# Problema 2: Even Fibonacci Numbers utilizando una secuencia generada por un generador
def problem_2(limit):
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    total = 0
    for current in fib_gen():
        if current > limit:
            break
        if current % 2 == 0:
            total += current
    return total

# Problema 3: Largest Prime Factor utilizando la búsqueda de factores de manera diferente
def problem_3(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor

# Problema 4: Largest Palindrome Product con un enfoque de búsqueda descendente
def problem_4():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):  # Comenzar desde i reduce la redundancia
            product = i * j
            if product <= max_palindrome:
                break  # Ya no necesitamos seguir en este bucle si el producto es menor que el máximo ya encontrado
            if str(product) == str(product)[::-1]:
                max_palindrome = product
    return max_palindrome

# Problema 5: Smallest Multiple utilizando un enfoque de MCD para calcular el MCM
def problem_5(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    smallest_mult = 1
    for i in range(2, n + 1):
        smallest_mult = lcm(smallest_mult, i)
    return smallest_mult

# Verificamos que las funciones pasen las pruebas básicas
assert problem_1(10) == 23, "La función debería retornar 23 para el límite 10"
assert problem_2(10) == 10, "La función debería retornar 10 como la suma de los primeros términos pares"
assert problem_3(13195) == 29, "La función debería retornar 29 como el mayor factor primo de 13195"
assert 10000 <= problem_4() <= 998001, "El resultado debería estar dentro del rango de productos de dos números de 3 dígitos"
assert problem_5(10) == 2520, "La función debería retornar 2520 como el número divisible por todos los números del 1 al 10"

# Retornamos las funciones para confirmar que todo funciona correctamente
(problem_1(10), problem_2(10), problem_3(13195), problem_4(), problem_5(10))
