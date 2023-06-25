import numpy as np
import time
import os
a1 = 0
a2 = 1
a3 = 2
a4 = 3
a=1
bus=np.zeros((10,4), dtype=object)
for i in range(10):
    for j in range(4):
        bus[i][j] = str(a)
        a = a + 1
cont_asientos = 0
menu = True
while menu:
    os.system('cls')
    for f in range(2):
        print(f" {bus[f][a1]}     {bus[f][a2]}         {bus[f][a3]}     {bus[f][a4]}")
    for f in range(2,4,3):
        print(f" {bus[f][a1]}    {bus[f][a2]}        {bus[f][a3]}    {bus[f][a4]}")
    for f in range(3,10):
        print(f"{bus[f][a1]}    {bus[f][a2]}        {bus[f][a3]}    {bus[f][a4]}")
    print("*** VENTA DE PASAJES - TRANSPORTES EL CIELO ***")
    print("")
    asiento = input("¿Que asiento desea comprar?\n")
    c = 0
    for i in range(10):
        for j in range(4):
            if bus[i][j] == asiento:
                bus[i][j] = "X"
                c = 1
    if c == 0:
        print("Asiento ocupado")
    os.system('cls')
    for f in range(2):
        print(f" {bus[f][a1]}     {bus[f][a2]}         {bus[f][a3]}     {bus[f][a4]}")
    for f in range(2,4,3):
        print(f" {bus[f][a1]}    {bus[f][a2]}        {bus[f][a3]}    {bus[f][a4]}")
    for f in range(3,10):
        print(f"{bus[f][a1]}    {bus[f][a2]}        {bus[f][a3]}    {bus[f][a4]}")
    cont = int(input("Desea seguir comprando?\n 1. SI  2. NO\n"))
    if cont == 2:
        menu = False
print("\nGracias por visitar Cielo-Ticket")
print(" ")
time.sleep(2)