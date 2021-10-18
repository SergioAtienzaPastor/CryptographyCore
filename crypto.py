import os
import datetime

def main():
    getInput()

def getInput():

    # Obtener parámetros de operación
    while(True):

        oper = input("[x] Introduzca 1 para encriptar en XOR \n [x] Introduzca 2 desencriptar XOR):")

        if(oper == "1" or oper == "2"):
            break
        else:
            print("¡La entrada es incorrecta, vuelva a ingresar!")

    # Obtener la contraseña del archivo
    while(True):

        password = input("Por favor introduzca la contraseña:")
    
        if(len(password) == 0):
            print("¡La contraseña no puede estar en blanco!")
        else:
            break

    # Obtener la ruta del archivo de la operación
    while(True):

        path = input("Introduzca la ruta del archivo (ejemplo: C: \\ test.txt):")

        try:
            f_read = open(path, "rb")
        except:
            print("Archivo no encontrado, compruebe si la ruta existe!")
        else:
            break

    # Realizar operaciones de cifrado o descifrado
   # if(oper == "e"): 
   #  encrypt(path, password)
  # elif(oper == "d"):
     #   decrypt(path, password)
main()