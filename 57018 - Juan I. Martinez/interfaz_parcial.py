#Juan I. Martinez, Legajo 57018

from conversor import *

def main():
   while True:
      salir = ""
      x = input("Ingrese un numero o presione c para salir: ")
      if x == "c":     
         break
      else:
         y = interfaz(x)
         print("El numero ingresado en su forma Hexadecimal es:", y)


def interfaz(val):
    try:
       nro = int(val)
       return completo(nro)
    except ValueError:
       return "Disculpe, solo acepto numeros"

#main() 
#quitar comentario anterior para probar interfaz