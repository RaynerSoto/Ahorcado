import random

diccionario = {
    0: 'Ganondorf',
    1: 'Zelda',
    2: 'Link',
    3: 'Mario',
    4: 'Luigi',
    5: 'Bowser',
    6: 'Kirby',
    7: 'Koopa',
    8: 'Fox',
    9: 'Wolf',
    10: 'Yoshi',
    11: 'Mark',
    12: 'Ike'
}
def palabras(posicion):
    return diccionario[posicion]

def cantidad_palabras():
    return len(diccionario)