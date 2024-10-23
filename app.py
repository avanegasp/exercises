# Si listamos todos los números por debajo del 10 que son múltiplos de 3 o 5 obtenemos: 3, 5, 6 y 9.
# La suma de estos múltiplos es 23. Realice un algoritmo para encontrar la suma de todos los múltiplos de 3 o 5 por debajo de 1000.


def num_sum(num):
    new_num = 0

    for i in range(0,num+1):
        if i % 3 == 0 or i % 5 == 0:
            new_num += i
    return new_num

print(num_sum(1000))


# Escriba una rutina que imprima los números del 1 al 100 pero:
# cuando el número sea múltiplo de 3, imprima “Tic”, en lugar del número.
# Cuando el número sea múltiplo de 5, imprima “Toc”, en lugar del número.
# Cuando el número sea múltiplo tanto de 3 como de 5, imprima “TicToc”, en lugar del número.

def fizzbuzz(num):

    for i in range (1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("TicToc")
        elif i % 3 == 0:
            print("Tic")
        elif i % 5 == 0:
            print("Toc")
        else:
            print("Other")

print(fizzbuzz(15))

# Haga un programa que filtre el arreglo y devuelva un arreglo
# con solo el nombre de sus amigos. Si un nombre tiene exactamente
# 4 letras, puedes estar seguro que es amigo tuyo! De lo contrario,
# puede estar seguro de que no…



def friends_mine(friends):
    friends = ["Ryan", "Kieran", "Mark", "Miguel"]

    new_friends = []

    for i in range(1, friends+1):
        if len(i) == 4:
            new_friends.append(i)
    return new_friends

print(friends_mine(["Ryan", "Kieran", "Mark", "Miguel", "Peter", "Ramón"]))


