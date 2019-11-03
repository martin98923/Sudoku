from api import api
from Sudoku import Sudoku 

##############################################


class Interfaz():

    def ingresar_tamaño_tablero(self):#se ingresa el tamaño del tablero
        self.tamaño = 0
        while self.tamaño != "9" and self.tamaño != "4":
            self.tamaño = input("Ingrese el tamaño del tablero (4/9)\n")
            if self.tamaño != "9" and self.tamaño != "4":
                print("Ingrese el tamaño del tablero nuevamente\n")

        self.tamaño = int(self.tamaño)      
        self.board = api(int(self.tamaño))
        self.game = Sudoku(self.board)

    def ingresar_posicion(self, fila, columna, valor):  #se verifica que exista la posicion en la que la persona va a ingresar el valor

        if (fila > 0 and fila <= self.tamaño and columna > 0 and columna <= self.tamaño and valor > 0 and valor <= self.tamaño):
            return True
        else:
            return False
        
    def ingresar_valor(self, numero, x, y): 
        try:
            if int(x) > self.tamaño:
                return False
            elif int(y) > self.tamaño:
                return False
            elif numero != "x":
                if int(numero) > 0 and int(numero) < self.tamaño+1:
                    return True
            return True
        except Exception as w: 
            print(w)
            return False

    def pedir_valores(self):
        self.numero = input("Ingrese el valor")
        self.fila = input("Escoja fila")
        self.columna = input("Escoja columna")
        print("")

    def jugar(self):
        self.ingresar_tamaño_tablero()    
        print("")
        print(self.game.imprimir_tablero())
        while not self.game.win():
            self.pedir_valores()
            if self.ingresar_valor(self.fila, self.columna, self.numero):
                self.game.ingresar_valor(int(self.fila)-1, int(self.columna)-1, self.numero)
                print(self.game.imprimir_tablero())
            else:
                print("INGRESE UN VALOR CORRECTO")


if __name__ == '__main__':    
    game = Interfaz()
    game.jugar()