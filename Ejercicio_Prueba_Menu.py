import os
import time
menores, totalm, totalgm, ttentm, ttdescm = 0, 0, 0, 0, 0
adultos, totala, totalga, ttenta, ttdesca = 0, 0, 0, 0, 0
mayores, totalam, totalgam, ttentam = 0, 0, 0, 0
sbtt, descuento, tt, opc, anular, sw = 0, 0, 0, 0, 0, 0
preciom, descm, precioa, desca, precioam = 2500, 0.1, 5000, 0.05, 1000
sw = ttentm + ttenta + ttentam
menu = True
while menu:
    os.system("cls")
    print("*** MENU ENTRADAS ***")
    print("")
    print("1. Menores            << de  5 a 12 años  >>     Precio $  2.500")
    print("2. Adultos            << de 13 a 64 años  >>     Precio $  5.000")
    print("3. 3ra. Edad          << de 65 y más años >>     Precio $  1.000")
    print("4. Imprimir Boleta - Salir")
    print("5. Anular Compra")
    print("6. Salir")
    print(" ")
    print("Descuentos solo los días Viernes")
    print("Menores un 10% ... Adultos un 5% ... 3ra Edad sin descuento")
    print(f"Total de Entradas reservadas - Menores {ttentm} - Adultos {ttenta} - 3ra. Edad {ttentam}")
    try:
        entrada = int(input("\nQue opcion de entradas elige\n"))
        if (entrada > 0 and entrada < 7):
            if (entrada == 1):
                menores = int(input("Cuantas entradas de Menores quiere comprar\n"))
                totalm = preciom * menores
                totalgm = totalgm + totalm
                ttentm = ttentm + menores
                sw = ttentm + ttenta + ttentam
            elif (entrada == 2):
                adultos = int(input("Cuantas entradas de Adultos quiere comprar\n"))
                totala = precioa * adultos
                totalga =totalga + totala
                ttenta = ttenta + adultos
                sw = ttentm + ttenta + ttentam
            elif (entrada == 3):
                mayores = int(input("Cuantas entradas de Adultos quiere comprar\n"))
                totalam = precioam * mayores
                totalgam =totalgam + totalam
                ttentam = ttentam + mayores
                sw = ttentm + ttenta + ttentam
            elif (entrada == 4):
                if (sw == 0):
                    print("opción invalida")
                    time.sleep(2)
                else:
                    opc = int(input("¿Qué día asistira?\n1. Viernes\n2. Otro día\n"))
                    if (opc == 1):
                        ttdescm = totalgm * descm
                        ttdesca = totalga * desca
                        sbtt = totalgm + totalga + totalgam
                        descuento = ttdescm + ttdesca
                        tt = sbtt - descuento
                        print(" ")
                        print("*******DETALLE BOLETA*******")
                        print(" ")
                        print(f" {ttentm} entradas de Menores         $ {totalgm}")
                        print(f" {ttenta} entradas de Adultos         $ {totalga}")
                        print(f" {ttentam} entradas de Adultos Mayores $ {totalgam}")
                        print(" ")
                        print(f" Subtotal                              $ {sbtt}")
                        print(f" Descuento                             $ {descuento}")
                        print(" ")
                        print(f" Total a pagar                         $ {tt}")
                        print("")
                        print("<<<     ¡Gracias por su compra!     >>>")
                        menu = False
                    else:
                        sbtt = totalgm + totalga + totalgam
                        descuento = ttdescm + ttdesca
                        tt = sbtt - descuento
                        print(" ")
                        print("*******DETALLE BOLETA*******")
                        print(" ")
                        print(f" {ttentm} entradas de Menores         $ {totalgm}")
                        print(f" {ttenta} entradas de Adultos         $ {totalga}")
                        print(f" {ttentam} entradas de Adultos Mayores $ {totalgam}")
                        print(" ")
                        print(f" Subtotal                              $ {sbtt}")
                        print(f" Descuento                             $ {descuento}")
                        print(" ")
                        print(f" Total a pagar                         $ {tt}")
                        print("")
                        print("<<<     ¡Gracias por su compra!     >>>")
                        menu = False
            elif (entrada == 5):
                if (sw == 0):
                    print("opción invalida")
                    time.sleep(2)
                else:    
                    anular = int(input("¿Desea anular la compra?\n1. SI\n2. NO\n"))
                    if (anular == 1):
                        menores, totalm, totalgm, ttentm, ttdescm = 0, 0, 0, 0, 0
                        adultos, totala, totalgm, ttenta, ttdescm = 0, 0, 0, 0, 0
                        mayores, totalam, totalgam, ttentam = 0, 0, 0, 0
                        sbtt, descuento, tt, dia, anular, sw = 0, 0, 0, 0, 0, 0
                        preciom, descm, precioa, desca, precioam = 2500, 0.1, 5000, 0.05, 1000
                        sw = ttentm + ttenta + ttentam
            elif (entrada == 6):
                menu = False
        else:
            print("no existe esa opcion")
            time.sleep(2)
    except:
        print("opcion invalida")
        time.sleep(2)
print("\nGracias por visitar BV-Ticket")
print(" ")
time.sleep(2)          