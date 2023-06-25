import os
import time
tradic, valort, preciot = 0, 0, 12000
pepero, valorp, preciop = 0, 0, 14000
allcar, valora, precioa = 0, 0, 17000
sbtt, descuento, tt, opc, anular, sw = 0, 0, 0, 0, 0, 0
descd, descv = 0.12, 0.1
sw = tradic + pepero + allcar
menu = True
while menu:
    os.system("cls")
    print("Pizzeria << Pizza Duoc >>")
    print("***    MENU  RAPID    ***")
    print("")
    print("1. Tradicional      Precio $  12.000")
    print("2. Peperoni         Precio $  14.000")
    print("3. All carnes       Precio $  17.000")
    print("4. Imprimir Boleta - Salir")
    print("5. Anular Compra")
    print("6. Salir")
    print(" ")
    print("Descuentos --- Estudiantes Diurna un 12% ... Estudiantes Vespertino un 10% ... Administrativos sin descuento")
    print(f"Total de Pizzas reservadas - Tradicional {tradic}- Peperoni {pepero} - All carnes {allcar}")
    try:
        entrada = int(input("\nQue opcion de entrada elige\n"))
        if (entrada > 0 and entrada < 7):
            if (entrada == 1):
                if (tradic > 0):
                    print("Usted ya eligio esta pizza, puede comprar otro tipo o imprimir la boleta y cancelar")
                    time.sleep(3)
                else:
                    tradic = int(input(f"Cuantas pizzas de Tradicional quiere comprar\n"))
                    valort = preciot * tradic
                    sw = tradic + pepero + allcar
            elif (entrada == 2):
                if (pepero > 0):
                    print("Usted ya eligio esta pizza, puede comprar otro tipo o imprimir la boleta y cancelar")
                    time.sleep(3)
                else:
                    pepero = int(input(f"Cuantas pizzas de Peperoni quiere comprar\n"))
                    valorp = preciop * pepero
                    sw = tradic + pepero + allcar
            elif (entrada == 3):
                if (allcar > 0):
                    print("Usted ya eligio esta pizza, puede comprar otro tipo o imprimir la boleta y cancelar")
                    time.sleep(3)
                else:
                    allcar = int(input(f"Cuantas pizzas de All carnes quiere comprar\n"))
                    valora = precioa * allcar
                    sw = tradic + pepero + allcar
            elif (entrada == 4):
                if (sw == 0):
                    print("opción invalida, no hay para comprar")
                    time.sleep(2)
                else:
                    opc = int(input("Elija una opción:\n1. Diurno\n2. Vespertino\n3. Administrativo\n"))
                    if (opc > 0 and opc < 4):
                        if (opc == 1):
                            sbtt = valort + valorp + valora
                            descuento = sbtt * descd
                            tt = sbtt - descuento
                            print(" ")
                            print("*******DETALLE BOLETA*******")
                            print(" ")
                            print(f" {tradic} Pizza Tradicional         $ {valort}")
                            print(f" {pepero} Pizzas Peperoni           $ {valorp}")
                            print(f" {allcar} Pizza All carnes          $ {valora}")
                            print(" ")
                            print(f" Subtotal                    $ {sbtt}")
                            print(f" Descuento del 12%           $ {descuento}")
                            print(" ")
                            print(f" Total a pagar               $ {tt}")
                            print("")
                            print("<<<     ¡Gracias por su compra!     >>>")
                            menu = False
                        elif (opc == 2):
                            sbtt = valort + valorp + valora
                            descuento = sbtt * descv
                            tt = sbtt - descuento
                            print(" ")
                            print("*******DETALLE BOLETA*******")
                            print(" ")
                            print(f" {tradic} Pizza Tradicional         $ {valort}")
                            print(f" {pepero} Pizzas Peperoni           $ {valorp}")
                            print(f" {allcar} Pizza All carnes          $ {valora}")
                            print(" ")
                            print(f" Subtotal                    $ {sbtt}")
                            print(f" Descuento del 10%           $ {descuento}")
                            print(" ")
                            print(f" Total a pagar               $ {tt}")
                            print("")
                            print("<<<     ¡Gracias por su compra!     >>>")
                            menu = False
                        else:
                            tt = valort + valorp + valora
                            print(" ")
                            print("*******DETALLE BOLETA*******")
                            print(" ")
                            print(f" {tradic} Pizza Tradicional         $ {valort}")
                            print(f" {pepero} Pizzas Peperoni           $ {valorp}")
                            print(f" {allcar} Pizza All carnes          $ {valora}")
                            print(" ")
                            print(f" Total a pagar               $ {tt}")
                            print("")
                            print("<<<     ¡Gracias por su compra!     >>>")
                            menu = False
                    else:
                        print("opción invalida")
                        time.sleep(2)
            elif (entrada == 5):
                if (sw == 0):
                    print("opción invalida, no hay nada que anular")
                    time.sleep(2)
                else:    
                    anular = int(input("¿Desea anular la compra?\n1. SI\n2. NO\n"))
                    if (anular > 0 and anular < 3):
                        if (anular == 1):
                            tradic, valort, preciot = 0, 0, 12000
                            pepero, valorp, preciop = 0, 0, 14000
                            allcar, valora, precioa = 0, 0, 17000
                            sbtt, descuento, tt, opc, anular, sw = 0, 0, 0, 0, 0, 0
                            descd, descv = 0.12, 0.1
                            sw = tradic + pepero + allcar
                        elif (anular == 2):
                            print("")
                    else:
                        print("opción invalida")
                        time.sleep(2)
            elif (entrada == 6):
                menu = False
        else:
            print("no existe esa opcion")
            time.sleep(2)
    except:
        print("opcion invalida")
        time.sleep(2)
print("\nGracias por visitar Rapid-Ticket")
print(" ")
time.sleep(2)          