import random

from Ahorcado import interfaz_juego
from Ahorcado import interfaz_game
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    variable = random.randint(0,10000000000000000000000000000)
    if variable % 2 == 0:
        interfaz_juego()
    else:
        interfaz_game()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
