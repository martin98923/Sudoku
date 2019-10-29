import math


class Sudoku():

    def __init__(self, tablero): #Metodo inicial
        self.tablero = tablero
        self.no_borrables = []
        self.tamaño = len(self.tablero)
        self.zona = int(math.sqrt(self.tamaño))

        #Valores que no se pueden modificar
        for i in range(self.tamaño):
            for j in range(len(self.tablero[i])):
                if (self.tablero[i][j] != "x"):
                    self.no_borrables.append((i, j))

    #Valida que no se repita ningun valor en la fila y columna
    def repetir(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

        for i in range(len(self.tablero)):#recorro la fila
            for j in range(len(self.tablero)):#recorro la columna
                if  self.valor == self.tablero[i][self.columna]:
                    return False
                elif self.valor == self.tablero[self.fila][j]:
                    return False

    #Valida que no se repita ningun en elemnto en la zona
    def zona_repetida(self, fila, columna, valor):
        for fila in range(0, self.tamaño, self.zona):
            for columna in range(0, self.tamaño, self.zona):
                for x in range(self.zona):
                    for y in range(self.zona):
                        for i in range(self.zona):
                            for j in range(self.zona):
                                if (self.tablero[x + fila][y + fila] != "x" and
                                    self.tablero[fila + i][columna + j] == self.valor and
                                    (x+fila, y+columna) != (i+fila, j+columna)):
                                    return False
        return True

    #Valida que no se repita ningun en elemnto en la zona
    def zona_repetida(self,fila,columna,valor):
        if self.tamaño == 9:
            if (fila < 3):
                fila = 0
            elif (fila >= 3 and fila <=5):
                fila = 3
            else:
                fila = 6
            if (columna < 3):
                columna = 0
            elif (columna >= 3 and columna <=5):
                columna = 3
            else:
                columna = 6
            for i in range(3):
                for j in range(3):
                    if self.tablero[fila + i][columna + j] == str(valor):
                        return False

        if self.tamaño == 4:
            if (int(fila) < 2):
                fila = 0
            elif (fila >= 2 and fila <=3):
                fila = 2
           
            if (columna < 2):
                columna = 0
            elif (columna >= 2 and columna <=3):
                columna = 2          
            for i in range(2):
                for j in range(2):
                    if self.tablero[fila + i][columna + j] == str(valor):
                        return False       
        return True
    
    def nofijo(self,fila, columna):
        for i in range(len(self.no_borrables)):
            if self.no_borrables[i] == (fila, columna):
                return False
            else:
                return True
    
    #valida el ingreso de un valor 
    def ingresar_numero(self, fila, columna, valor):
        if self.repetir(fila, columna, valor) and self.zona_repetida(fila, columna, valor):
            self.tablero[fila][columna] = valor
            return True
        else:
            return False    
            
    #Valida si gano o no el juego
    def gano(self):
        for i in range(9):
            if "x" in self.tablero[i]:
                return False  
        return True

    def imprimir_tablero(self): #Guarda en una variable para poder imprimirlo en la INTERFACE
        #i=fila(lista) 
        self.impreso = ""
        for i in self.tablero:
            for elemento in i:
                self.impreso += elemento + " "
            self.impreso += "\n"
            
        return self.impres