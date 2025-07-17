import pygame
import random
import sys
from preguntas import cargar_preguntas
from partidas import guardar_partida

TIEMPO_LIMITE = 10
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
fuente = pygame.font.SysFont(None, 36)

def mostrar_texto(texto, x, y):
    render = fuente.render(texto, True, NEGRO)
    pantalla.blit(render, (x, y))

def jugar():
    preguntas = cargar_preguntas()
    vidas = 3
    puntos = 0

    while vidas > 0:
        pregunta = random.choice(preguntas)
        opciones = [pregunta['opcion1'], pregunta['opcion2'], pregunta['opcion3'], pregunta['opcion4']]
        random.shuffle(opciones)
        correcta = pregunta['respuesta']
        seleccion = None

        tiempo_inicio = pygame.time.get_ticks()

        while seleccion is None:
            pantalla.fill(BLANCO)
            mostrar_texto(pregunta['pregunta'], 50, 50)
            for i, opc in enumerate(opciones):
                mostrar_texto(f"{i+1}. {opc}", 50, 120 + i*50)

            tiempo_actual = pygame.time.get_ticks()
            tiempo_pasado = (tiempo_actual - tiempo_inicio) // 1000
            tiempo_restante = max(0, TIEMPO_LIMITE - tiempo_pasado)
            mostrar_texto(f"Tiempo: {tiempo_restante}s | Vidas: {vidas} | Puntos: {puntos}", 50, 400)
            pygame.display.flip()

            if tiempo_restante == 0:
                vidas -= 1
                break

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        idx = evento.key - pygame.K_1
                        if idx < len(opciones):
                            seleccion = opciones[idx]
                            if seleccion == correcta:
                                puntos += 10
                            else:
                                vidas -= 1

    nombre = input("Juego terminado. Ingresa tu nombre: ").strip()
    guardar_partida(nombre, puntos)
