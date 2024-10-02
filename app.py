# Encuentra los números pares
# Escribe una función que reciba un número y retorne
# todos los números pares desde 0 hasta ese número.


# def ever_num(num):
#     new_ever = []
#     for i in range(0, num, 1):
#         if i % 2 == 0:
#             new_ever.append(i)
#     return new_ever

# def ever_num(num):
#     new_ever = [i for i in range(0, num, 1) if i % 2 == 0]
#     return new_ever
#
# print(ever_num(20))

#
# Número Palíndromo
# Dado un número, crea una función que determine si es un número palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).

pals = [3,55,67,322,1221,7889,565]

# def palindromo(nums):
#     new_pal = []
#
#     for num in nums:
#         if str(num) == str(num)[::-1]:
#             new_pal.append(num)
#     return new_pal
#
# print(palindromo(pals))

# def palindromo(nums):
#     new_pal = [num for num in nums if str(num) == str(num)[::-1]]
#     return new_pal
#
# print(palindromo(pals))

# Máximo y Mínimo en un Arreglo
# Escribe un programa que reciba un arreglo de números
# y retorne el número más grande y el más pequeño.

# list_nums = [2,55,74,26,88,443,89,326]
#
# def max_and_min(nums):
#     max_num = max(nums)
#     min_num = min(nums)
#
#     return max_num, min_num
#
# print(max_and_min(list_nums))

# Suma de Pares en un Arreglo
# Crea una función que sume todos los números pares de un arreglo.

# evers = [2,45,66,22,44,66,85,32,77,8534]
#
# def ever_sum(nums):
#     new_ever_sum = 0
#
#     for num in nums:
#         if num % 2 == 0:
#             new_ever_sum += num
#     return new_ever_sum
#
# print(ever_sum(evers))

# Factorial de un Número
# Escribe una función que calcule el factorial de un número dado.

# def factorial(num):
#     new_factorial = 1
#
#     for i in range(1, num -1):
#         new_factorial *= i
#
#     return new_factorial
#
# print(factorial(5))

# Fibonacci
# Escribe un programa que devuelva el n-ésimo número de la serie de Fibonacci.

def fibonnaci(num):
    if num <= 0:
        return "Ingresa un nuevo número"

    new_fibo = [0, 1]

    for i in range(2, num):
        next_fibo = new_fibo[i-1] + new_fibo[i-2]
        new_fibo.append(next_fibo)
    return new_fibo[:i]

print(fibonnaci(20))










