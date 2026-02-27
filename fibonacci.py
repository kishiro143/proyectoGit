# Serie de Fibonacci para un número dado

n = int(input("Ingrese cuántos números de Fibonacci desea ver: "))

a, b = 0, 1
contador = 0

print("Serie de Fibonacci:")
while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1
print()
