#Ejercicio 2
#import os
#os.system("cls")
#fact = 1
#i = 1
#num = int(input("Ingrese un número:  "))
#while i <= num:
#    fact = fact * i
#    i = i + 1
#print (f"El factorial de {num} es: {fact}")
#Ejercicio 3
#import os
#os.system("cls")
#i = 1
#suma = 0
#while i <= 5:
#    num = int(input("Ingrese un número:\n"))
#    if num < 0:
#        while num < 0:
#            num = int(input("ingrese numero mayor a 0.\n"))
#        suma = suma + num
#        i = i + 1
#    else:
#        suma = suma + num
#        i = i + 1
#print(f"la suma de los 5 numeros positivos es {suma}")
#Ejercicio 4
#x = 123%10
#aa = 123//10
#xx = aa%10
#bb = 123//100
#print (x)
#print (xx)
#print (bb)
import os
os.system("cls")

num = int(input("Ingrese un número entre 103 y 987\n"))
while num >=103 and num <=987:
    x = num%10
    a1 = num//10
    a2 = a1%10
    a3 = num//100
    uno = (x * 10) + a2
    dos = (uno * 10) + a3
    print(f"\n El número invertido de {num} es {dos}")
    break