#Juan I. Martinez, Legajo 57018

import unittest
from interfaz_parcial import *

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_1(self):
        result = interfaz(1234)
        self.assertEqual(result, '4D2')

    def test_interfaz_2(self):
        result = interfaz("HOLA")
        self.assertEqual(result, "Disculpe, solo acepto numeros")
        
    def test_interfaz_3(self):
        result = interfaz(4095)
        self.assertEqual(result, "FFF")

if __name__ == '__main__':
    unittest.main()