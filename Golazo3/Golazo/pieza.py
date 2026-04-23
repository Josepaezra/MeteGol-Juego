import pygame
from .constants import ANCHO_CUADRO, MADERA, BALON, FILAS , COLUMNAS
import importlib

class Pieza:

    PADDING = 6
    encuadre = 8
    def __init__(self, fila, columna, tipo):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = ANCHO_CUADRO * self.columna + self.PADDING/2
        self.y = ANCHO_CUADRO * self.fila + self.PADDING/2

    def dibujar(self, win):
        tamaño = ANCHO_CUADRO - self.PADDING
        tamaño2 = ANCHO_CUADRO 
        if self.tipo[0:10] == "larga vert":
            larga_vert =  pygame.transform.scale(MADERA, (tamaño, tamaño*2))
            win.blit(larga_vert, (self.x,self.y))

        if self.tipo[0:13] == "larga horizon":
            larga_horizon = pygame.transform.scale(pygame.transform.rotate(MADERA, 90), (tamaño*2, tamaño) )
            win.blit(larga_horizon, (self.x + self.PADDING/2,self.y))

        if self.tipo == "pequeña":
            pequeña = pygame.transform.scale(MADERA, (tamaño, tamaño))
            win.blit(pequeña, (self.x,self.y)) 
            
        if self.tipo == "balon":
            balon = pygame.transform.scale(BALON, (tamaño2*2, tamaño2*2))  
            win.blit(balon, (self.x -self.PADDING/2, self.y- self.PADDING/2 ))     
        
    def moverse(self, fila, columna):
        """Es necesario este método puesto que actualiza la posicion para dibujar a partir de cierta casilla la pieza"""

        #if self.tipo== "pequeña":
        self.fila= fila
        self.columna= columna
        self.calc_pos()

    """
        if self.tipo[0:10]== "larga vert":
            tablero= importlib.import_module('main').main
            print(tablero)
        
            
            for fila in tablero:
                for columna in fila:
                    if columna == self.tipo:
                        arriba = self.fila, self.columna
                        break
            self.fila, self.columna = arriba
            
                


        if self.tipo== "larga horizon":
            pass           


        if self.tipo== "balon":   
            pass    
    """
    def __repr__(self):
        return str(self.tipo)