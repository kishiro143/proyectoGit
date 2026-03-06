import unittest

def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular factorial de número negativo")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

class TestFactorial(unittest.TestCase):
    
    def test_factorial_cero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_cinco(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
