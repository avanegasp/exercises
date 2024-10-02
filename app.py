# Encuentra los números pares
# Escribe una función que reciba un número y retorne
# todos los números pares desde 0 hasta ese número.


# def ever_num(num):
#     new_ever = []
#     for i in range(0, num, 1):
#         if i % 2 == 0:
#             new_ever.append(i)
#     return new_ever

def ever_num(num):
    new_ever = [i for i in range(0, num, 1) if i % 2 == 0]
    return new_ever

print(ever_num(20))












