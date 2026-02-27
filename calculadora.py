# Menú para operaciones matemáticas con ciclo

while True:
    print("\n=== CALCULADORA ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División real")
    print("5. División entera")
    print("6. Módulo (residuo)")
    print("7. Salir")
    
    opcion = int(input("\nSeleccione una opción (1-7): "))
    
    if opcion == 7:
        print("¡Hasta luego!")
        break
    elif opcion == 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero")
    elif opcion == 5:
        if num2 != 0:
            resultado = num1 // num2
            print(f"{num1} // {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero")
    elif opcion == 6:
        if num2 != 0:
            resultado = num1 % num2
            print(f"{num1} % {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero")
    else:
        print("Opción no válida")
    
    input("\nPresione Enter para continuar...")
