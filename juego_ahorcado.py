#Juego del ahorcado
#En este reto se utilizara compehensions, manejo de errores, manejo de archivos
#Investigar enumerate
#Metodo get en diccionarios
#os.system("cls") limpiar pantalla
#Jorge Mejicanos
#github.com/Yorchriv

from operator import le, truediv
import os
import random


def run():
    ganaste = False
    palabras = []
    letrax = []
    letra = ""
    vidas = 1
    estado_ant = ""
    save = ""
    
    with open("./data.txt", "r", encoding="utf-8") as f:
        for names in f:
            palabras.append(str(names))
    
    num_ale = random.randint(0,171) #Mejorar esto despues
    len_string = len(palabras[num_ale]) #Largo del string
    pal = str([palabras[i] for i in range(0, 171) if i == num_ale]) #Traer palabra aleatoria a variable pal
    str_pal = "".join(pal) #Convertir a string la variable pal

    for i in range(0, len_string - 1):
        letrax.append("_")

    while ganaste == False:
        os.system("cls") #Limpiar pantalla
        print("Juego del Ahorcado!")
        print("Adivina la palabra!")
        for i in range(0, len_string - 1):
            if letra == str_pal[i + 2:i + 3:]:
                letrax[i] = str_pal[i + 2:i + 3:]

        str_letrax = "".join(letrax) #Convertir letrax en string
        print(str_letrax)

        if str_letrax == str_pal[2:len_string + 1:] or letra == "-":
            ganaste = True
            os.system("cls") #Limpiar pantalla
            print("Felicidades Has ganado, la palabra es: " + str_pal[2:len_string + 1:])
        elif vidas >= 6:
             os.system("cls") #Limpiar pantalla
             ahorcado(7)
             print("Has perdido :( la palabra era: " + str_pal[2:len_string + 1:])
             ganaste = True

        else:
            if save == str_letrax:
                vidas += 1
            else:
                save = str_letrax
                ganaste = False
            ahorcado(vidas)
            letra = input("Ingrese una Letra: ")
        
        
    

        
def ahorcado(num_int): #Datos del ahorcado
    intento = {
        1:
        "  ____ \n"
        " |    |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "-------\n",
        2:
        "  ____ \n"
        " |    |\n"
        " 0    |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "-------\n",
        3:
        "  ____ \n"
        " |    |\n"
        " 0/   |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "-------\n",
        4:
        "  ____ \n"
        " |    |\n"
        "_0/   |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "-------\n",
        5:
        "  ____ \n"
        " |    |\n"
        "_0/   |\n"
        " |    |\n"
        "      |\n"
        "      |\n"
        "-------\n",
        6:
        "  ____ \n"
        " |    |\n"
        "_0/   |\n"
        " |    |\n"
        "/     |\n"
        "      |\n"
        "-------\n",
        7:
        "  ____ \n"
        " |    |\n"
        "_X/   |\n"
        " |    |\n"
        "/ \   |\n"
        "      |\n"
        "-------\n"
        }
    return print(intento[num_int])


if __name__ == '__main__':
    run()