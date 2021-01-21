import random


def dado(numero):
    numero = int(numero)
    lados = []

    for x in range(numero):
        lados.append(x+1)

    return random.choice(lados)






