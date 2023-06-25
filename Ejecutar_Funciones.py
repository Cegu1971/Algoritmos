from Funciones import calcular_iva, descuento, imc
import time
import os
menu = True
while menu:
    os.system("cls")
    print("***    MENU  FUNCIONES    ***")
    print("")
    print("1. Calculo de IVA")
    print("2. Calculo de Descuento")
    print("3. Calculo de IMC")
    print("4. Salir")
    print(" ")
    try:
        entrada = int(input("\nQue opcion desea eliger\n"))
        if (entrada > 0 and entrada < 5):
            if (entrada == 1):
                calcular_iva()
            elif (entrada == 2):
                descuento()
            elif (entrada == 3):
                imc()
            elif (entrada == 4):
                menu = False
        else:
            print("no existe esa opcion")
            time.sleep(2)
    except:
        print("opcion invalida")
        time.sleep(2)
print("\nEsperamos que lo hayamos ayudado, Adios")
print(" ")
time.sleep(2)   