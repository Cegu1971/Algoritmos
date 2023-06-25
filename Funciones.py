import os
import time
def calcular_iva():
    print("CALCULO DE IVA")
    sw = True
    while sw:
        try:
            os.system('cls')
            precio = int(input("Ingrese el precio del producto:\n$"))
            if (precio > 0):
                iva = round(precio * 0.19)
                total = round(precio + iva)
                print(f" Monto Neto     ${precio}")
                print(f" Iva 19%        ${iva}")
                print("               -----------")
                print(f" Monto Total    ${total}")
                print("")
                time.sleep(5)
                sw = False
        except:
            print("Valor no válido. Favor vuelva a ingresar la cantidad")   
            time.sleep(2)
            os.system('cls') 

def descuento():
    print("CALCULO DE DESCUENTO")
    sw = True
    while sw:
        try:
            os.system('cls')
            precio = int(input("Ingrese el precio del producto:\n$"))
            descuento = int(input("Ingrese el valor del descuento:\n%"))
            if (precio > 0):
                desc  = descuento / 100
                v_descuento = round(precio * desc)
                total = round(precio - v_descuento)
                print(f" Monto Neto     ${precio}")
                print(f" Iva {descuento}%        ${v_descuento}")
                print("               -----------")
                print(f" Monto Total    ${total}")
                print("")
                time.sleep(5)
                sw = False
        except:
            print("Valor no válido. Favor vuelva a ingresar la cantidad")   
            time.sleep(2)
            os.system('cls')

def imc():
    sw = True
    while sw:
        try:
            os.system('cls')
            estatura = float(input("Ingrese su estatura:\n"))
            peso = float(input("Ingrese su peso:\n"))
            if (estatura >= 1 and peso >= 1):
                imc = round(peso / estatura ** 2,2)
                if imc < 18.5:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de BAJO PESO")
                elif imc > 18.6 and imc < 24.9:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de ADECUADO")
                elif imc > 25.0 and imc < 29.9:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de SOBREPESO")
                elif imc > 30.0 and imc < 34.9:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de OBESIDAD GRADO 1")   
                elif imc > 35.0 and imc < 39.9:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de OBESIDAD GRADO 2")
                elif imc > 40.0:
                    print(f"Su IMC es igual a {imc} por ende usted se encuentra en el rango de OBESIDAD GRADO 3")
                print("")
                time.sleep(5)
                sw = False
        except:
            print("Valor no válido. Favor vuelva a ingresar la cantidad")   
            time.sleep(2)
            os.system('cls') 