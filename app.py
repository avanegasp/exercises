# Encuentra los números pares
# Escribe una función que reciba un número y retorne todos los números pares
# desde 0 hasta ese número.
from asyncio import new_event_loop

# def ever_num(num):
#     newnum = 0
#     for num in range(num + 1):
#         if num % 2 == 0:
#             newnum += num
#     return newnum
#
# print(ever_num(1000))
#
# def ever_num_2(num):
#     new_num = []
#     for num in range(num + 1):
#         if num % 2 == 0:
#             new_num.append(num)
#     return new_num
#
# print(ever_num_2(100))




# Número Palíndromo
# Dado un número, crea una función que determine si es un número palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).

# palindromo = [121, 433, 555, 676, 1221, 2, 787]
#
# def pal_num(nums):
#     new_pal = []
#
#     for num in nums:
#         if str(num) == str(num)[::-1]:
#             new_pal += [num]
#             # new_pal.append(num)
#     return new_pal
#
# print(pal_num(palindromo))



#
# Máximo y Mínimo en un Arreglo
# Escribe un programa que reciba un arreglo de números
# y retorne el número más grande y el más pequeño.


# nums = [12, 444, 32, 67, 66, 3246]
#
# def max_min(numbers):
#     max_num = max(numbers)
#     min_num = min(numbers)
#
#     print("max", max_num)
#     print("min", min_num)
#
# print(max_min(nums))

#
# Suma de Pares en un Arreglo
# Crea una función que sume todos los números pares de un arreglo.

ever_nums = [122, 55, 78, 33, 84, 8325, 7782]

def ever_sum(nums):
    new_ever_nums = 0
    # new_ever_nums = []

    for num in nums:
        if num % 2 == 0:
            new_ever_nums += num
            # new_ever_nums.append(num)
    return new_ever_nums

print(ever_sum(ever_nums))










