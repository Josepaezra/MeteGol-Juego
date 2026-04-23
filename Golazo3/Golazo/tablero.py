import pygame
from .constants import VERDE, ANCHO, LARGO, BLANCO,COLUMNAS, FILAS
from .pieza import Pieza

class Tablero:

    def __init__(self):
        self.tablero = []
        self.seleccionar_pieza= None
        self.pieza_cuadrada = 4
        self.pieza_rectangular_vertical = 4
        self.pieza_rectangular_horizontal = 1
        self.balon = 1

        self.crear_tablero()

    def dibujar_tablero(self,win):
        win.fill(VERDE)
        pygame.draw.line(win, BLANCO, (0,LARGO/2), (ANCHO,LARGO/2), width=5)
        pygame.draw.circle(win, BLANCO, (ANCHO/2,LARGO/2), LARGO/12, 5 )
        pygame.draw.rect(win, BLANCO,[ANCHO/4,0,ANCHO/2,ANCHO/4], width=5 )
        pygame.draw.rect(win, BLANCO,[ANCHO*3/8,0,ANCHO/4,ANCHO/8], width=5 )

    def crear_tablero(self):
        for fila in range(FILAS):
            self.tablero.append([])
            for columna in range(COLUMNAS):
                self.tablero[fila].append(0)
                

        self.tablero[0][0]= Pieza(0, 0, "larga vert1")
        self.tablero[1][0]= Pieza(0, 0, "larga vert1")

        self.tablero[2][0]= Pieza(2, 0, "larga vert2")
        self.tablero[3][0]= Pieza(2, 0, "larga vert2")

        self.tablero[0][3]= Pieza(0, 3, "larga vert3")
        self.tablero[1][3]= Pieza(0, 3, "larga vert3")

        self.tablero[2][3]= Pieza(2, 3, "larga vert4")
        self.tablero[3][3]= Pieza(2, 3, "larga vert4")


        self.tablero[2][1] = Pieza(2,1, "larga horizon")
        self.tablero[2][2] = Pieza(2,1, "larga horizon")

        self.tablero[1][1] = Pieza(1,1,"pequeña")
        #self.tablero[1][2] = Pieza(1,2,"pequeña")
        self.tablero[4][0] = Pieza(4,0,"pequeña")
        self.tablero[4][3] = Pieza(4,3,"pequeña")

        self.tablero[3][1] = Pieza(3,1,"balon")
        self.tablero[3][2] = Pieza(3,1,"balon")
        self.tablero[4][1] = Pieza(3,1,"balon")
        self.tablero[4][2] = Pieza(3,1,"balon")
        print(self.tablero)

    def dibujar(self, win):
        self.dibujar_tablero(win)
        contador_horiz=0
        contador1=0
        contador2=0
        contador3=0
        contador4=0
        contador_balon = 0


        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                pieza= self.tablero[fila][columna]
        
                if pieza != 0:

                    if pieza.tipo == "pequeña":
                        pieza.dibujar(win)
                    
                    elif pieza.tipo == "larga horizon" and contador_horiz==0:
                        pieza.dibujar(win)
                        contador_horiz += 1
                        
                    elif pieza.tipo == "larga vert1" and contador1==0:
                        pieza.dibujar(win)
                        contador1 += 1
                    elif pieza.tipo == "larga vert2" and contador2==0:
                        pieza.dibujar(win)
                        contador2 += 1
                    elif pieza.tipo == "larga vert3" and contador3==0:
                        pieza.dibujar(win)
                        contador3 += 1
                    elif pieza.tipo == "larga vert4" and contador4==0:
                        pieza.dibujar(win)
                        contador4 += 1

                    elif pieza.tipo == "balon" and contador_balon == 0:
                        pieza.dibujar(win)
                        contador_balon +=1



        #print(self.tablero)

    def moverse(self, pieza, fila, columna):
        if pieza == 0:
            pass
        elif pieza.tipo == "pequeña":
            self.tablero[pieza.fila][pieza.columna], self.tablero[fila][columna] = 0, self.tablero[pieza.fila][pieza.columna]             
            pieza.moverse(fila,columna)

        elif pieza.tipo[:10] == "larga vert":
            f=0
        
            for filax in self.tablero:
                end= False
                arriba=(0,0)
                c=0
                for columnax in filax:
                    if columnax !=0:
                        if columnax.tipo == pieza.tipo:
                            arriba = f, c            #Consigo la parte de arriba de la pieza
                            end = True
                            break 
                    c+=1
                if end:
                    break
                f+=1
            print(f,c)
            print(arriba)
            if fila < f:  #Si subo la pieza
                self.tablero[f][c]  = 0 #Muevo parte de arriba pieza
                self.tablero[fila][columna]=self.tablero[f][c]  
                self.tablero[f+1][c], self.tablero[fila+1][columna] = 0, self.tablero[fila][columna] #Muevo parte de abajo pieza
                pieza.moverse(fila,columna)
            
            if fila >f:  #Si bajo la pieza
                self.tablero[f][c], self.tablero[fila][columna] = 0, self.tablero[f][c]  
                try:
                    self.tablero[f-1][c], self.tablero[fila-1][columna] = 0, self.tablero[fila][columna] 
                except:
                    self.tablero[fila-1][columna]= self.tablero[fila][columna]

                pieza.moverse(fila,columna)

            if fila ==f:  #Si muevo lateralmente la pieza (mismo codigo para si subo la pieza)
                self.tablero[f][c], self.tablero[fila][columna] = 0, self.tablero[f][c]  
                self.tablero[f+1][c], self.tablero[fila+1][columna] = 0, self.tablero[fila][columna] 
                pieza.moverse(fila,columna)
     


        elif pieza.tipo == "larga horizon":
            f=0
        
            for filax in self.tablero:
                end= False
                arriba=(0,0)
                c=0
                for columnax in filax:
                    if columnax !=0:
                        if columnax.tipo == pieza.tipo:
                            arriba = f, c            #Consigo la parte de arriba (izquierda en este caso) de la pieza
                            end = True
                            break 
                    c+=1
                if end:
                    break
                f+=1
            print(f,c)
            print(arriba)



            self.tablero[f][c], self.tablero[fila][columna] = 0, self.tablero[f][c]  
            self.tablero[f][c+1], self.tablero[fila][columna+1] = 0, self.tablero[fila][columna] #Muevo parte de abajo pieza           
            pieza.moverse(fila,columna)

        print(self.tablero)


    def obtener_pieza(self,fila, columna):
        return self.tablero[fila][columna]

