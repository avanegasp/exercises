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

def palindromo(nums):
    new_pal = [num for num in nums if str(num) == str(num)[::-1]]
    return new_pal

print(palindromo(pals))













