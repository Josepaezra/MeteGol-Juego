import pygame
from .constants import VERDE, ANCHO, LARGO, BLANCO
from .pieza import Pieza

class Tablero:

    def __init__(self):
        self.tablero = []
        self.seleccionar_pieza= None
        self.pieza_cuadrada = 4
        self.pieza_rectangular_vertical = 4
        self.pieza_rectangular_horizontal = 1
        self.balon = 1

        

    def dibujar_tablero(self,win):
        win.fill(VERDE)
        pygame.draw.line(win, BLANCO, (0,LARGO/2), (ANCHO,LARGO/2), width=5)
        pygame.draw.circle(win, BLANCO, (ANCHO/2,LARGO/2), LARGO/12, 5 )
        pygame.draw.rect(win, BLANCO,[ANCHO/4,0,ANCHO/2,ANCHO/4], width=5 )
        pygame.draw.rect(win, BLANCO,[ANCHO*3/8,0,ANCHO/4,ANCHO/8], width=5 )

    def crear_tablero(self):
        self.tablero[0].append(Pieza(0, 0, "larga vert"))
