#Esta librería tiene funciones para resolver operaciones matemáticas
#limpia() : netejerà la pantalla del terminal
#leerJson(): Llegirà un fitxer json i ho carregarà a un diccionari
#escribirJson(): carregarà un diccionari a un fitxer
import os
import json


def limpia():
    os.system('clear')
    
def leerJson(filename):
    #Arg1: Nombre/ruta del fichero
    #devuelve diccionario
    with open(filename, 'r', encoding='utf-8') as fichero:
        diccionario = json.load(fichero)
    return diccionario

def escribirJson(diccionario,filename):
    #Arg1: Diccionario a convertir
    #Arg2: Nombre/ruta del fichero
    #No devuelve nada
    with open(filename, 'w', encoding='utf-8') as fichero:
        json.dump(diccionario, fichero, ensure_ascii=False, indent=4)

# variable1=1
# vauto=1

# def limpia():
#     os.system('clear')

# def autosuma(vauto):
#     vauto=vauto+1
#     return vauto

# def suma2(): #Rutina que muestra la suma por pantalla
#     variable1=2
#     variable2=2
#     print(variable1+variable2)

# def suma3(): #Función que devuelve un int
#     variable1=3
#     variable2=3
#     return variable1+variable2

# def divide(pepe=2):
#     variable1=100
#     return variable1/pepe
