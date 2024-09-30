# Encuentra los números pares
# Escribe una función que reciba un número y retorne todos los números pares
# desde 0 hasta ese número.



def ever_num(num):
    newnum = []
    for num in range(num + 1):
        if num % 2 == 0:
            newnum.append(num)
    return newnum

print(ever_num(1000))