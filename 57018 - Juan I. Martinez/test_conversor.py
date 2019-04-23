#Juan I. Martinez, Legajo 57018

import unittest
from conversor import *

class TestConversor(unittest.TestCase):
    def test_conversor_1(self):
        result = completo(1)
        self.assertEqual(result, '1')

    def test_conversor_2(self):
        result = completo(10)
        self.assertEqual(result, "A")

    def test_conversor_3(self):
        result = completo(999)
        self.assertEqual(result, "3E7")

    def test_conversor_4(self):
        result = completo(17)
        self.assertEqual(result, '11')

    def test_conversor_5(self):
        result = completo(16)
        self.assertEqual(result, '10')

    def test_conversor_6(self):
        result = completo(4095)
        self.assertEqual(result, "FFF")
    
    def test_conversor_7(self):
        result = completo(1234)
        self.assertEqual(result, "4D2")

    def test_conversor_8(self):
        result = completo(234)
        self.assertEqual(result, "EA")

        

if __name__ == '__main__':
    unittest.main()