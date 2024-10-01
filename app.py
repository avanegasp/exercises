# Encuentra los números pares
# Escribe una función que reciba un número y retorne todos los
# números pares desde 0 hasta ese número.
from imp import new_module


# def ever_num(num):
#     new_num = []
#
#     for element in range(0, num):
#         if element % 2 == 0:
#             new_num.append(element)
#     return new_num
#
#
# print(ever_num(20))

#
# Factorial de un Número
# Escribe una función que calcule el factorial de un número dado.


# def factorial(num):
#     new_fact = 1
#
#     for element in range(num,0, -1):
#         new_fact *= element
#     return new_fact
#
#
# print(factorial(5))



# Fibonacci
# Escribe un programa que devuelva el n-ésimo número de la serie de Fibonacci.


# def fibonnaci(num):
#     new_fibo = [0, 1]
#
#     for elem in range(2,num):
#         next_fibo = new_fibo[elem - 1] + new_fibo[elem - 2]
#         new_fibo.append(next_fibo)
#
#     return new_fibo[:num]
#
#
# print(fibonnaci(20))
#
# Reverso de una Cadena
# Crea una función que tome una cadena y devuelva su reverso.

def phrase(word):
    return word[::-1]


print(phrase("Hola"))


















