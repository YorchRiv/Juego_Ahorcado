#Juego del ahorcado
#En este reto se utilizara compehensions, manejo de errores, manejo de archivos
#Investigar enumerate
#Metodo git en diccionarios
#os.system("cls") limpiar pantalla
#Jorge Mejicanos
#Yorchriv

from operator import truediv
import os

def run():
    ganaste = False
    while ganaste == False:
        print("Adivina la palabra!")
        letra = input("Ingrese una letra: ")
        os.system("cls") #Limpiar pantalla
        ganaste = True

if __name__ == '__main__':
    run()