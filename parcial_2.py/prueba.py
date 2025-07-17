import pygame
import sys
import juego
import partidas

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Preguntas")
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
fuente = pygame.font.SysFont(None, 36)

def mostrar_texto(texto, x, y):
    render = fuente.render(texto, True, NEGRO)
    pantalla.blit(render, (x, y))

def menu():
    while True:
        pantalla.fill(BLANCO)
        mostrar_texto("1. Jugar", 100, 100)
        mostrar_texto("2. Ver TOP 10", 100, 150)
        mostrar_texto("3. Salir", 100, 200)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    jugar()
                elif evento.key == pygame.K_2:
                    mostrar_top10()
                elif evento.key == pygame.K_3:
                    pygame.quit(); sys.exit()

if __name__ == '__main__':
    menu()
