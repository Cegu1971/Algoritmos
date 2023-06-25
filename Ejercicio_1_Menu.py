import time
import os
sw = True
while sw:
    os.system("cls")
    print("<<< Plantilla de Menú >>>")
    print(" ")
    print("1. Número Par e Impar")
    print("2. Serie Fibonacci de los primeros 10 números")
    print("3. Salir")
    try:
        op = int(input("Ingrese opción\n"))
        if(op > 0 and op < 5):
            if(op == 1):
                os.system("cls")
                print("número par e impar")
                try:
                    num = int(input("Ingrese un número\n"))
                    if (num%2 == 0):
                        print(f"el número {num} es par")
                        time.sleep(2)
                    else:
                        print(f"el número {num} es impar")
                        time.sleep(2)
                except:
                    print("error de tipo de datos")
                    time.sleep(2)
            elif(op == 2):
                os.system("cls")
                print("Serie Fibonacci de los primeros 10 números")
                try:
                    num = int(input("Ingrese un número\n"))
                    if (num%2 == 0):
                        print(f"el número {num} es par")
                        time.sleep(2)
                    else:
                        print(f"el número {num} es impar")
                        time.sleep(2)
                except:
                    print("error de tipo de datos")
                    time.sleep(2)
            elif(op == 3):
                print("Nos vemos")
                time.sleep(2)
                sw = False
        else:
            print("Opción no valida")
            time.sleep(2)
    except:
        print("Opción no valida")
        time.sleep(2)