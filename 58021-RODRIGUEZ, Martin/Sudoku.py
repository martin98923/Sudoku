import math


class Sudoku():

    def __init__(self, board): #Constructor
        self.board = board
        self.no_borrables = []
        self.tamaño = len(self.board)
        self.zona = int(math.sqrt(self.tamaño))

        for i in range(self.tamaño): #Se verifica si un elemento es fijo
            for j in range(len(self.board[i])):
                if (self.board[i][j] != "x"):
                    self.no_borrables.append((i, j))

    def repetir(self, fila, columna, valor):#Se verifica que no se repita un elemento en la fila y columna
        print(fila)       
        for i in range(self.tamaño):
            if str(valor) == self.board[i][columna]:
                return False
            if str(valor) == self.board[int(fila)][i]:
                return False
        return True

    def zona_repetida(self, fila, columna, valor):#Se verifica que no se repita un elemnto en la zona
        
        if self.tamaño == 9:
            if (fila < 3):
                fila = 0
            elif (fila >= 3 and fila <= 5):
                fila = 3
            else:
                fila = 6
            if (columna < 3):
                columna = 0
            elif (columna >= 3 and columna <= 5):
                columna = 3
            else:
                columna = 6
            for i in range(3):
                for j in range(3):
                    if self.board[fila + i][columna + j] == str(valor):
                        return False

        if self.tamaño == 4:
            if (int(fila) < 2):
                fila = 0
            elif (fila >= 2 and fila <= 3):
                fila = 2
           
            if (columna < 2):
                columna = 0
            elif (columna >= 2 and columna <= 3):
                columna = 2          
            for i in range(2):
                for j in range(2):
                    if self.board[fila + i][columna + j] == str(valor):
                        return False       
        return True
    
    def valor_no_fijo(self, fila, columna):
        for i in range(len(self.no_borrables)):
            if self.no_borrables[i] == (fila, columna):
                return False
            else:
                return True
    
    #valida el ingreso de un valor 
    def ingresar_valor(self, fila, columna, valor):
        if self.repetir(fila, columna, valor) and self.zona_repetida(fila,columna,valor) and self.valor_no_fijo(fila, columna):
            self.board[fila][columna] = valor

    #Valida si gano o no el juego
    def win(self):
        for i in range(self.tamaño):
            if "x" in self.board[i]:
                return False  
        return True

    def imprimir_tablero(self): #Guarda en una variable para poder imprimirlo en la INTERFACE
        #i=fila(lista) 
        self.impreso = ""
        for i in self.board:
            for elemento in i:
                self.impreso += elemento + " "
            self.impreso += "\n"

        return self.impreso