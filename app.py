# Si listamos todos los números por debajo del 10
# que son múltiplos de 3 o 5 obtenemos: 3, 5, 6 y 9.
# La suma de estos múltiplos es 23. Realice un algoritmo
# para encontrar la suma de todos los
# múltiplos de 3 o 5 por debajo de 1000.


# def num_sum(num):
#     new_num = 0
#
#     for i in range(0, num +1):
#         if i % 3 == 0 or i % 5 == 0:
#             new_num += i
#     return new_num
#
# print(num_sum(1000))

# Escriba una rutina que imprima los números del 1 al 100 pero:
# cuando el número sea múltiplo de 3, imprima “Tic”, en lugar del número.
# Cuando el número sea múltiplo de 5, imprima “Toc”, en lugar del número.
# Cuando el número sea múltiplo tanto de 3 como de 5, imprima “TicToc”, en lugar del número.

# def tic_toc(num):
#
#     for i in range(1, num +1):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, "TicToc")
#         elif i % 5 == 0:
#             print(i, "Toc")
#         elif i % 3 == 0:
#             print(i, "Tic")
#         else:
#             print(i, "Otro")
#
# print(tic_toc(100))

# Haga un programa que filtre el arreglo y devuelva un arreglo
# con solo el nombre de sus amigos. Si un nombre tiene exactamente
# 4 letras, puedes estar seguro que es amigo tuyo! De lo contrario,
# puede estar seguro de que no…
#
# Amigo = [“Ryan”, “Kieran”, “Mark”, “Miguel”]  Deberia [“Ryan”, “Mark”]

# friends = ["Ryan", "Kieran", "Mark", "Miguel"]
#
# def splitname(names):
#     new_friends = []
#
#     for i in names:
#         if len(i) == 4:
#             new_friends.append(i)
#     return new_friends
#
# print(splitname(friends))

# Escribe una función llamada sumaDigitos que
# retorne la suma de todos los dígitos de un número dado, por ejemplo:
# 5646 => 5+6+4+6 => 21

def retnum(num):
    new_num = 0

    for i in :
        new_num += i
    return new_num

print(retnum(10))