import pygame
from Golazo.tablero import Tablero
#from constants import 

class Juego():
    def __init__(self, win) :
        self._init()
        self.win = win
        self.hola = 5

    def actualiza(self):
        self.tablero.dibujar(self.win)
        pygame.display.update()
        self.tablero.dibujar(self.win)
        pygame.display.update()

    def _init(self):
        self.seleccionado = None
        self.tablero = Tablero()
        self.movimientos_validos = {}

    def resetear(self):
        self._init()


    def seleccionar(self, fila, columna):
        if self.seleccionado:
            resultado = self._mover(fila, columna)


    def _mover(self, fila, columna):
        pass