#PRIMER EJERCICIO
#import os
#os.system("cls")
#edad = int(input("ingrese su edad:\n"))
#if(edad>=18):
#    print("\neres mayor de edad")
#elif(edad>0 and edad<18):
#    print("\neres menor de edad")
#else:
#    print("\nvalor no correponde para edad")
#SEGUNDO EJERCICIO
import os
os.system("cls")
user_1 = "pedro"
pass_1 = "1234"
user_2 = "angel"
pass_2 = "a4s1"
user = input("Ingrese su usuario:\n")
clave = input("Ingrese su clave:\n")
if(user == user_1 and clave == pass_1 or user == user_2 and clave == pass_2):
    print(f"\nBienvenido {user}\n")
else:
    print("\nUsuario Invalido\n")