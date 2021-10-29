import argparse
from Crypto.Cipher import XOR




print("\n")
print(" $$$$$$\                                 $$\                $$$$$$\                                ")
print("$$  __$$\                                $$ |              $$  __$$\                               ")
print("$$ /  \__| $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$\    $$$$$$\  $$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\  ")
print("$$ |      $$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|  $$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$  __$$\ ")
print("$$ |      $$ |  \__|$$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |$$ |      $$ /  $$ |$$ |  \__|$$$$$$$$ |")
print("$$ |  $$\ $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |  $$\ $$ |  $$ |$$ |      $$   ____|")
print("\$$$$$$  |$$ |      \$$$$$$$ |$$$$$$$  | \$$$$  |\$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ ")
print(" \______/ \__|       \____$$ |$$  ____/   \____/  \______/  \______/  \______/ \__|       \_______|")
print("                    $$\   $$ |$$ |")                                                                 
print("                    \$$$$$$  |$$ |")                                                                 
print("                     \______/ \__|")                                                                 
print("\n")
print("Realizado por Schwd, paulaajwm, sergioo\n")

parser = argparse.ArgumentParser()
parser.add_argument( '-infile', help="Archivo a modificar", type=argparse.FileType('r'))
parser.add_argument( '-type', help="Seleccion tipo difrado: Cesar(1) o XOR(2)", type=int )
parser.add_argument( '-fitch', help="Numero de turnos para cifrado Cesar", type=int)
parser.add_argument( '-key', help="La key para realizar el XOR")
parser.add_argument( '-mode', help="Introduzca 'e'  para encriptar y 'd' para desencriptar", type=str)
parser.add_argument( '-f', help="Realiza fuerza bruta",default=3)
parser.add_argument( '-outfile', help="Archivo decodificado", type=argparse.FileType('w'))

args = parser.parse_args()
with args.infile as infile:
     file = infile.read()

turn = args.fitch

def getInput(): #primer argumento la  key, segundo argumento a cifrar o descifrar , tercer argiumento e o d
        
            # Realizar operaciones de cifrado o descifrado 
            
            if (args.mode == "e"):
                m = XOR.new(args.key)
                enc = m.encrypt(file)
                with args.outfile as outfile:  
                 outfile.write(enc.decode("utf-8"))
            if (args.mode == "d"):                
                m = XOR.new(args.key)
                dec = m.decrypt(file)
                with args.outfile as outfile:  
                 outfile.write(dec.decode("utf-8"))


def decrypt(text,turn):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (text[i]==" "):
            result += " "
        elif (char.islower()):
            result += chr((ord(char) - turn - 97) % 26 + 97)
        elif (char.isupper()):
            result += chr((ord(char) - turn - 65) % 26 + 65)
        else:
            result += text[i] 
    return result

def encrypt(text,turn):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (text[i]==" "):
            result += " "
        elif (char.islower()):
            result += chr((ord(char) + turn - 97) % 26 + 97)
        elif (char.isupper()):
            result += chr((ord(char) + turn - 65) % 26 + 65)
        else:
            result += text[i] 
    return result

def force(text):   
 with args.outfile as outfile:
  for i in range(25):
   outfile.write("f=" + str(i) +" "+decrypt(file,i) + '\n')
   

if __name__ == '__main__':
   if(args.type==1):
    if(args.mode=="d"):
        with args.outfile as outfile:
         outfile.write(decrypt(file,turn))
    elif(args.mode=="e"):
        with args.outfile as outfile:
         outfile.write(encrypt(file,turn))
    else:
         force(file)
   else:
     getInput()
   infile.close() 
