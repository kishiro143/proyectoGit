import unittest

def es_par(numero):
    return numero % 2 == 0

class TestPar(unittest.TestCase):
    
    def test_numero_par(self):
        self.assertTrue(es_par(4))
    
    def test_numero_impar(self):
        self.assertFalse(es_par(7))

if __name__ == '__main__':
    unittest.main()
