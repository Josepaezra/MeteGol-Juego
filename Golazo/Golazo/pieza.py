import pygame
from .constants import MARRON, MARRON_CLARO, ANCHO_CUADRO, MADERA

class Pieza:

    PADDING = 5
    BORDE = 2

    def __init__(self, fila, columna, tipo):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = ANCHO_CUADRO * self.columna
        self.y = ANCHO_CUADRO * self.fila

    def dibujar(self, win):
        tamaño = ANCHO_CUADRO - self.PADDING
        #pygame.draw.rect(win, MARRON,)
        larga_vert =  pygame.transform.scale(MADERA, (tamaño, tamaño*2))
        win.blit(larga_vert, (self.x,self.y))