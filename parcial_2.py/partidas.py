import json
import pygame
import sys
from datetime import datetime

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
fuente = pygame.font.SysFont(None, 36)

def mostrar_texto(texto, x, y):
    render = fuente.render(texto, True, NEGRO)
    pantalla.blit(render, (x, y))

def guardar_partida(nombre, puntaje):
    nueva = {"nombre": nombre, "puntaje": puntaje, "fecha": datetime.now().strftime("%Y-%m-%d")}
    try:
        with open("partidas.json", "r", encoding='utf-8') as archivo:
            partidas = json.load(archivo)
    except:
        partidas = []
    partidas.append(nueva)
    with open("partidas.json", "w", encoding='utf-8') as archivo:
        json.dump(partidas, archivo, indent=4)

def mostrar_top10():
    pantalla.fill(BLANCO)
    try:
        with open("partidas.json", "r", encoding='utf-8') as archivo:
            partidas = json.load(archivo)
    except:
        partidas = []

    partidas.sort(key=lambda x: x["puntaje"], reverse=True)
    mostrar_texto("TOP 10:", 50, 30)
    for i, p in enumerate(partidas[:10]):
        texto = f\"{i+1}. {p['nombre']} - {p['puntaje']} pts - {p['fecha']}\"
        mostrar_texto(texto, 50, 70 + i * 40)

    mostrar_texto(\"Presiona cualquier tecla para volver\", 50, 520)
    pygame.display.flip()
    esperar_tecla()

def esperar_tecla():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif evento.type == pygame.KEYDOWN:
                esperando = False
