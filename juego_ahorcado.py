#Juego del ahorcado
#En este reto se utilizara compehensions, manejo de errores, manejo de archivos
#Investigar enumerate
#Metodo get en diccionarios
#os.system("cls") limpiar pantalla
#Jorge Mejicanos
#Yorchriv

from operator import truediv
import os
import random

def run():
    ganaste = False
    palabras = []
    letrax = []
    

    with open("./data.txt", "r", encoding="utf-8") as f:
        for names in f:
            palabras.append(str(names))
    
    num_ale = random.randint(0,171) #Mejorar esto despues
    len_string = len(palabras[num_ale]) #Largo del string
    pal = str([palabras[i] for i in range(0, 171) if i == num_ale]) #Traer palabra aleatoria a variable pal
    str_pal = "".join(pal) #Convertir a string la variable pal


    while ganaste == False:
        print("Adivina la palabra!\n")

        for i in range(0, len_string - 1):
            print("_", end=" ")

        print(str_pal[2:len_string + 1:])
        # letra = input("Ingrese una letra: ")
        
        # os.system("pause") #pausa
        # os.system("cls") #Limpiar pantalla
        ganaste = True

if __name__ == '__main__':
    run()