import csv

def cargar_preguntas():
    lista = []
    with open("preguntas.csv", encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista.append(fila)
    return lista
