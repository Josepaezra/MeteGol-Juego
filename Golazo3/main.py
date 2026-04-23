import pygame
from Golazo.juego import Juego
from Golazo.tablero import Tablero
from Golazo.constants import ANCHO, LARGO, ANCHO_CUADRO


FPS = 60


WIN = pygame.display.set_mode((ANCHO, LARGO))

def obtener_fila_columna_del_mouse(pos):
    x, y = pos
    fila = y // ANCHO_CUADRO
    columna = x // ANCHO_CUADRO
    return fila, columna


def main():
    run = True
    clock = pygame.time.Clock()
    juego = Juego(WIN)
    #pieza = tablero.obtener_pieza(1,1)
    #tablero.moverse(pieza, 0,1)
    #tablero.moverse(pieza, 0,2)
    #pieza2= tablero.obtener_pieza(0,0)
    #tablero.moverse(pieza2, 0,1)


    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila, columna = obtener_fila_columna_del_mouse(pos)
                pieza = juego.tablero.obtener_pieza(fila, columna)
                #fila, columna = obtener_fila_columna_del_mouse(pos)
                juego.tablero.moverse(pieza, 0,2)
                

        juego.actualiza()


    pygame.quit()

main()