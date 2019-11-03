import unittest
from interfaz import Interfaz


class TestInterface(unittest.TestCase):

    def test_Interfaz_1(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(2, 1, 8))   
    
    def test_Interfaz_2(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(8, 8, 1))
    
    def test_Interfaz_3_columna_no_valida(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresar_valor(4, "b", 2))
    
    def test_Interfaz_4_valor_no_valido(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresar_valor(0, 4, "¿"))

    def test_Interfaz_5_fila_y_valor_no_valido(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresar_valor("d", 4, "a"))

    def test_Interfaz_6_valor_no_valido(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresar_valor(6, 4, "ç"))
    
    def test_Interfaz_7_columna_y_valor_no_valido(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresar_valor(7, "c", "*"))

    def test_Interfaz_8(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(7, 4, 5))
    
    def test_interfaz_9(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(1, 3, 1))
    
    def test_interfaz_10(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(2, 5, 9))

    def test_interfaz_11(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresar_valor(6, 8, 2))

if __name__ == '__main__':    
    unittest.main()