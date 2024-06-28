import pygame
import sys
from pygame.locals import *
from variables import *
from funciones import *
import os

pygame.init()
os.system("cls")

# configuracion ventana
pantalla = pygame.display.set_mode(SIZE_SCREEN) # tamano
pygame.display.set_caption("Preguntados") # titulo
icono =  pygame.image.load("./assets/logo.png") # cargo imagen
pygame.display.set_icon(icono) # icono

# configuracion fuentes
fuente_titulo = pygame.font.Font("./assets/This Cafe.ttf", 100)
fuente_jugar = pygame.font.SysFont("Comic Sans MS", 38)

# carga imagenes
imagen_fondo = pygame.image.load("./assets/fondo.jpeg")
fondo = pygame.transform.scale(imagen_fondo, SIZE_SCREEN)
imagen_sonido = pygame.image.load("./assets/sonido.png")
imagen_mute = pygame.image.load("./assets/mute.png")

# rects
boton_jugar_rect = pygame.Rect(WIDTH // 2 - (boton_jugar_width // 2), 520, boton_jugar_width, boton_jugar_height)
boton_sonido_rect = pygame.Rect(20, 20, 40, 40)
sonido = pygame.transform.scale(imagen_sonido, (boton_sonido_rect.width, boton_sonido_rect.height))
mute = pygame.transform.scale(imagen_mute, (boton_sonido_rect.width, boton_sonido_rect.height))

# configuracion sonidos
pygame.mixer.init()
sonido_fondo_menu = pygame.mixer.Sound("./assets/sonido_fondo_prueba.mp3")
sonido_fondo_menu.set_volume(0.05)
sonido_fondo_menu.play(-1)
sonido_click_boton = pygame.mixer.Sound("./assets/click_pop.mp3")
sonido_click_boton.set_volume(0.3)
sonido_click_boton_jugar = pygame.mixer.Sound("./assets/click_jugar.mp3")
sonido_click_boton_jugar.set_volume(0.2)

while funcionando:
    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            funcionando = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            coordenada_click = event.pos
            if punto_colicion_rectangulo(coordenada_click, boton_sonido_rect):
                sonido_click_boton.play()
                if muteado == False:
                    muteado = True
                else:
                    muteado = False
            if punto_colicion_rectangulo(coordenada_click, boton_jugar_rect):
                sonido_click_boton_jugar.play()
            
    pantalla.blit(fondo, (0, 0))

    # Actualizo pantalla
    mostrar_texto(pantalla, "PREGUNTADOS", fuente_titulo, coordenadas_titulo, BLANCO, None)
    bloque_jugar = pygame.draw.rect(pantalla, color_boton_jugar, boton_jugar_rect, 0, 10)
    pygame.draw.rect(pantalla, NEGRO, boton_jugar_rect, 2, 10)
    mostrar_texto(pantalla, "JUGAR", fuente_jugar, bloque_jugar.center, BLANCO, None)
    bloque_sonido = pygame.draw.rect(pantalla, color_boton_sonido, boton_sonido_rect, 0, 10)
    pygame.draw.rect(pantalla, NEGRO, boton_sonido_rect, 2, 10)
    if muteado:
        pantalla.blit(mute, bloque_sonido.topleft)
        sonido_fondo_menu.set_volume(0)
        sonido_click_boton.set_volume(0)
        sonido_click_boton_jugar.set_volume(0)

    else:
        pantalla.blit(sonido, bloque_sonido.topleft)
        sonido_fondo_menu.set_volume(0.05)
        sonido_click_boton.set_volume(0.3)
        sonido_click_boton_jugar.set_volume(0.2)

    pygame.display.flip() # Muestro la pantalla

pygame.quit()
sys.exit()