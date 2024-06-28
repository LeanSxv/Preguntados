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
icono =  pygame.image.load("./assets/menu/logo.png") # cargo imagen
pygame.display.set_icon(icono) # icono

escena = "Menu Principal"
# fuentes
fuente_titulo_menu = pygame.font.Font("./assets/menu/This Cafe.ttf", 100)
fuente_jugar = pygame.font.SysFont("Comic Sans MS", 38)

# carga imagenes
# menu
imagen_fondo_menu = pygame.image.load("./assets/menu/fondo.jpeg")
fondo_menu = pygame.transform.scale(imagen_fondo_menu, SIZE_SCREEN)
imagen_sonido = pygame.image.load("./assets/menu/sonido.png")
imagen_mute = pygame.image.load("./assets/menu/mute.png")
# juego
imagen_fondo_juego = pygame.image.load("./assets/juego/fondo.jpeg")
fondo_juego = pygame.transform.scale(imagen_fondo_juego, SIZE_SCREEN)

# rects
# menu
boton_jugar_rect = pygame.Rect(WIDTH // 2 - (boton_jugar_width // 2), 520, boton_jugar_width, boton_jugar_height)
boton_sonido_rect = pygame.Rect(20, 20, 40, 40)
sonido = pygame.transform.scale(imagen_sonido, (boton_sonido_rect.width, boton_sonido_rect.height))
mute = pygame.transform.scale(imagen_mute, (boton_sonido_rect.width, boton_sonido_rect.height))
# juego

widht_bloque_juego = WIDTH // 1.5
height_bloque_juego = HEIGHT // 12
distancia_bloques = 35
bloque_1_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, 10, widht_bloque_juego, height_bloque_juego)
bloque_2_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, distancia_bloques + bloque_1_juego_rect.bottom, widht_bloque_juego, height_bloque_juego * 3)
bloque_3_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, distancia_bloques + bloque_2_juego_rect.bottom, widht_bloque_juego, height_bloque_juego)
bloque_4_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, distancia_bloques + bloque_3_juego_rect.bottom, widht_bloque_juego, height_bloque_juego)
bloque_5_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, distancia_bloques + bloque_4_juego_rect.bottom, widht_bloque_juego, height_bloque_juego)
bloque_6_juego_rect = pygame.Rect(CENTER_X - widht_bloque_juego // 2, HEIGHT - height_bloque_juego - 10, widht_bloque_juego, height_bloque_juego)


# configuracion sonidos
pygame.mixer.init()
# sonidos menu
sonido_fondo_menu = pygame.mixer.Sound("./assets/menu/sonido_fondo_prueba.mp3")
sonido_fondo_menu.set_volume(0.05)
sonido_fondo_menu.play(-1)

sonido_click_boton_menu = pygame.mixer.Sound("./assets/menu/click_pop.mp3")
sonido_click_boton_menu.set_volume(0.3)
sonido_click_boton_jugar = pygame.mixer.Sound("./assets/menu/click_jugar.mp3")
sonido_click_boton_jugar.set_volume(0.2)
# sonidos juego
sonido_fondo_juego = pygame.mixer.Sound("./assets/juego/reloj.mp3")
sonido_fondo_juego.set_volume(0.10)

# tiempo
tick_1s = pygame.USEREVENT + 0
tick_2s = pygame.USEREVENT + 1
pygame.time.set_timer(tick_1s,1000)
pygame.time.set_timer(tick_2s,2000)


# settings juego
tiempo_para_responder = 15
segundos = tiempo_para_responder


def ejecutar_menu():
    global funcionando
    global escena
    global muteado
    pantalla.fill(NEGRO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            funcionando = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coordenada_click = event.pos
            if punto_colicion_rectangulo(coordenada_click, boton_jugar_rect):
                sonido_fondo_menu.stop()
                sonido_click_boton_jugar.play()
                sonido_fondo_juego.play(-1, segundos * 1000)
                escena = "Juego"
            elif punto_colicion_rectangulo(coordenada_click, boton_sonido_rect):
                sonido_click_boton_menu.play()
                muteado = not muteado
            
    pantalla.blit(fondo_menu, (0, 0))

    # Actualizo pantalla
    mostrar_texto(pantalla, "PREGUNTADOS", fuente_titulo_menu, coordenadas_titulo, BLANCO, None)
    bloque_jugar = pygame.draw.rect(pantalla, color_boton_jugar, boton_jugar_rect, 0, 10)
    pygame.draw.rect(pantalla, NEGRO, boton_jugar_rect, 2, 10)
    mostrar_texto(pantalla, "JUGAR", fuente_jugar, bloque_jugar.center, BLANCO, None)
    bloque_sonido = pygame.draw.rect(pantalla, color_boton_sonido, boton_sonido_rect, 0, 10)
    pygame.draw.rect(pantalla, NEGRO, boton_sonido_rect, 2, 10)
    if muteado:
        pantalla.blit(mute, bloque_sonido.topleft)
        sonido_fondo_menu.set_volume(0)
        sonido_click_boton_menu.set_volume(0)
        sonido_click_boton_jugar.set_volume(0)
    else:
        pantalla.blit(sonido, bloque_sonido.topleft)
        sonido_fondo_menu.set_volume(0.10)
        sonido_click_boton_menu.set_volume(0.3)
        sonido_click_boton_jugar.set_volume(0.2)

    pygame.display.flip() # Muestro la pantalla

def ejecutar_juego():
    global funcionando
    global escena
    global muteado
    global segundos
    pantalla.fill(NEGRO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            funcionando = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coordenada_click = event.pos
            if punto_colicion_rectangulo(coordenada_click, boton_sonido_rect):
                sonido_click_boton_menu.play()
                muteado = not muteado
        if event.type == tick_1s:
            segundos -= 1
            print(segundos)
    pantalla.blit(fondo_juego, (0, 0))
    bloque_sonido = pygame.draw.rect(pantalla, color_boton_sonido, boton_sonido_rect, 0, 10)
    pygame.draw.rect(pantalla, NEGRO, boton_sonido_rect, 2, 10)
    pygame.draw.rect(pantalla, BLANCO, bloque_1_juego_rect, 0, 2)
    pygame.draw.rect(pantalla, BLANCO, bloque_2_juego_rect, 0, 10)
    pygame.draw.rect(pantalla, BLANCO, bloque_3_juego_rect, 0, 10)
    pygame.draw.rect(pantalla, BLANCO, bloque_4_juego_rect, 0, 10)
    pygame.draw.rect(pantalla, BLANCO, bloque_5_juego_rect, 0, 10)
    pygame.draw.rect(pantalla, BLANCO, bloque_6_juego_rect, 0, 2)
    if muteado:
        pantalla.blit(mute, bloque_sonido.topleft)
        sonido_fondo_juego.set_volume(0)
        # sonido_click_boton_menu.set_volume(0)
        # sonido_click_boton_jugar.set_volume(0)
    else:
        pantalla.blit(sonido, bloque_sonido.topleft)
        sonido_fondo_juego.set_volume(0.10)
        # sonido_click_boton_menu.set_volume(0.3)
        # sonido_click_boton_jugar.set_volume(0.2)
    pygame.display.flip() # Muestro la pantalla


while funcionando:

    match escena:
        case "Menu Principal":
            ejecutar_menu()
        case "Configuracion":
            # mostrar_configuracion()
            pass
        case "Juego":
            ejecutar_juego()
        case "Game Over":
            # ejecutar_game_over()
            pass

pygame.quit()
sys.exit()