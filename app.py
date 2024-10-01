# Encuentra los números pares
# Escribe una función que reciba un número y retorne todos los
# números pares desde 0 hasta ese número.


def ever_num(num):
    new_num = []

    for element in range(0, num):
        if element % 2 == 0:
            new_num.append(element)
    return new_num


print(ever_num(20))