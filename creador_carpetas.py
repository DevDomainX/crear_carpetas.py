#!/usr/bin/env python3
# crear carpetas 
#creador: Hans Saldias

import os
from colorama import init, Fore, Back
init()

print(Back.RED+Fore.YELLOW+"Creador de carpetas \n\npara salir solo pon (exit)")

def carpetas():
    try:
        while True:
            carpeta = input("Ingrese nombre de la carpeta: ")
            if carpeta == "exit":
                print("Gracias por usar mi script")
                break
            else:
                pass

            if  not os.path.exists(carpeta):
                os.mkdir(carpeta)
                print("\nla carpeta a sido creada")
            else:
                print("\nLa capeta  ya existe")
                op = input("\nDecea seguir creando carpetas(y/n): ")
                if op == "y":
                    carpetas()
                elif op == "n":
                    print("\nGracias por usar mi script Hans saldias")
                    break
    except:
        print("opcion invalida vurlve a intentarlo")
       
carpetas()