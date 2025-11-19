import pygame
from Golazo.constants import ANCHO, LARGO
from Golazo.tablero import Tablero

FPS = 60


WIN = pygame.display.set_mode((ANCHO, LARGO))




def main():
    run = True
    clock = pygame.time.Clock()
    tablero = Tablero()


    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        tablero.dibujar_tablero(WIN)
        pygame.display.update()


    pygame.quit()

main()