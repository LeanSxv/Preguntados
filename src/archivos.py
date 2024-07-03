import json
import os

def listar_csv(nombre_archivo:str, separador = ','):
    lista = []
    lista_claves = []
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        primer_linea = archivo.readline()
        lista_claves = primer_linea.replace("\n", "").split(separador)
        for linea in archivo:
            lista_valores = linea.replace("\n", "").split(",")
            diccionario = {}
            for i in range(len(lista_claves)):
                diccionario[lista_claves[i]] = lista_valores[i]
            lista.append(diccionario)
    return lista

def generar_csv(nombre_archivo:str, lista:list):
    lista_claves = list(lista[0].keys())
    cabecera = ",".join(lista_claves) 
    with open(nombre_archivo, "w") as archivo:
        archivo.write(cabecera + "\n")
        for elemento in lista:
            lista_valor = list(elemento.values())
            dato = ",".join(lista_valor) + "\n"            
            archivo.write(dato)

def generar_json(nombre_archivo:str, lista:list, nombre_lista:str):
    dict_json = {}
    dict_json[nombre_lista] = lista
    with open(nombre_archivo, "w") as archivo:
        json.dump(dict_json, archivo, indent=4)
