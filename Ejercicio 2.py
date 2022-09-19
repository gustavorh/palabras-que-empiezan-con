# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:59:53 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""
import string


def palabras_comienzan_con_letra(nombre_archivo):

    # Se crea un diccionario con la librería "string" con todas las letras del alfabeto
    alfabeto = dict.fromkeys(string.ascii_lowercase, "")

    # Se abre el archivo con el nombre ingresado por teclado.
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        # Se leen los datos dentro del archivo de una sola vez y se almacenan en la variable 'datos_leidos'.
        datos_leidos = archivo.read()

        # Se deben dividir las oraciones en palabras usando el siguiente método. split() es usado para dividir cada oración dentro de 'datos_leidos'
        # y toda esa información se guarda en la variable 'palabras'.
        palabras = datos_leidos.split()

        lista_palabras = []
        # Se itera entre todas las keys (llaves) del diccionario.
        for llaves in alfabeto.keys():
            for palabra in palabras:  # Se itera entre todas las palabras obtenidas del archivo.
                # Si la primera letra de la palabra iterada es igual a la llave del diccionario.
                if palabra[0] == llaves:
                    # Se guarda en el diccionario su llave y su valor, cada palabra separada por un ";"
                    alfabeto[llaves] += palabra + ";"
                    alfabeto[llaves] = [alfabeto.values()]

    # Return entregando el diccionario del alfabeto con cada palabra que comienze con la llave.
    return alfabeto, lista_palabras


# Se pregunta al usuario por el nombre del archivo y su extensión.
nombre_archivo = input(
    "Ingrese el nombre del archivo y su extensión (Ejemplo.txt): ")
# Se llama a la función pasando como parámetro el nombre del archivo ingresado por teclado.
diccionario_palabras, lista_palabras = palabras_comienzan_con_letra(
    nombre_archivo)
# lista_palabras = lista_palabras_comienzan_con_letra(nombre_archivo) # Se llama a la función pasando como parámetro el nombre del archivo ingresado por teclado.

# print(diccionario_palabras)
print(diccionario_palabras, lista_palabras)
