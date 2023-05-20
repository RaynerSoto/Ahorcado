import random
from Jugador import Player
from Palabra import palabras
from Palabras2 import palabra_aleatoria
from Palabra import cantidad_palabras
def rellenador_listado(pos):
    listado = list()
    for i in range(0,pos):
        listado.insert(0,'_')
    return listado
def selector_personaje():
    return palabras(random.randrange(0,cantidad_palabras()))


def juego(jugador,palabra_a_adivinar):
    personaje = ''.join(palabra_a_adivinar)
    print(f'Tienes actualmente: {jugador.vidas} vidas')
    if jugador.vidas == 0:
        print(f'Fin del juego. No has conseguido adivinar el personaje que se trataba de: {personaje}')
        print(f'Más suerte la próxima {jugador.nombre}')
    elif ''.join(jugador.palabra) == ''.join(list(palabra_a_adivinar)):
        print('Has adivinado el personaje')
        print(f'Lo conseguiste: {jugador.nombre}')
    else:
        print(jugador.palabra)
        letra = input('Ingrese una letra: ')
        contador = 0
        verdad = False
        if len(letra) == 1:
            for x in list(palabra_a_adivinar):
                if list(jugador.palabra).count(letra) == 0:
                    if letra.lower() == ''.join(x).lower():
                        jugador.palabra.pop(contador)
                        jugador.palabra.insert(contador, x)
                        verdad = True
                    contador += 1
                else:
                    print('Letra ya ingresada')
                    verdad = True
                    break
        if verdad == False:
            jugador.vidas -= 1
        juego(jugador,palabra_a_adivinar)

def interfaz_juego():
    palabra = list(selector_personaje())
    nombre = input('Ingrese su nombre : ')
    jugador = Player()
    listado = rellenador_listado(len(palabra))
    jugador.__int__(nombre,listado)
    juego(jugador,palabra)
    palabra = input('Desea volver a jugar:\n1-Si\nOtro\n')
    if palabra.isdigit() and int(palabra) == 1:
        interfaz_juego()
    else:
        print('Gracias por jugar mi pequeño videojuego')
#Otra forma para resolver el juego
def interfaz_game():
    palabra = list(palabra_aleatoria())
    nombre = input('Ingrese su nombre : ')
    jugador = Player()
    listado = rellenador_listado(len(palabra))
    jugador.__int__(nombre,listado)
    juego(jugador,palabra)
    palabra = input('Desea volver a jugar:\n1-Si\nOtro\n')
    if palabra.isdigit() and int(palabra) == 1:
        interfaz_juego()
    else:
        print('Gracias por jugar mi pequeño videojuego')
