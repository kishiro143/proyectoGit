# Leer un entero y decir si es capicúa (se lee igual al derecho y al revés)

numero = input("Ingrese un número entero: ")

if numero == numero[::-1]:
    print(f"El número {numero} SÍ es capicúa")
else:
    print(f"El número {numero} NO es capicúa")
