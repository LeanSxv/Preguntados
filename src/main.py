import pygame
import sys
import os
from pygame.locals import *
from variables import *
from funciones import *
from archivos import listar_csv, generar_json

pygame.init()

os.system('cls')

def terminar():
    pygame.quit()
    exit()


# configuracion ventana
pantalla = pygame.display.set_mode(SIZE_SCREEN) # tamano
pygame.display.set_caption('Preguntados') # titulo
icono =  pygame.image.load('./assets/menu/logo.png') # cargo imagen
pygame.display.set_icon(icono) # icono

escena = 'Menu Principal'

# fuentes
# menu
fuente_jugar_menu = pygame.font.SysFont('Comic Sans MS', 38)
# juego
fuente_juego = pygame.font.SysFont('Verdana', 16)
# fin pregunta
fuente_titulo_fin_pregunta = pygame.font.SysFont('Segoe Print', 25, True)
fuente_continuar_fin_pregunta = pygame.font.SysFont('Comic Sans MS', 20)
fuente_vidas_fin_pregunta = pygame.font.SysFont('System', 35)
fuente_titulo_fin_pregunta.underline = True


# carga imagenes
# menu
imagen_fondo_menu = pygame.image.load('./assets/menu/fondo.jpeg')
fondo_menu = pygame.transform.scale(imagen_fondo_menu, SIZE_SCREEN)
imagen_sonido = pygame.image.load('./assets/menu/sonido.png')
imagen_mute = pygame.image.load('./assets/menu/mute.png')
imagen_titulo = pygame.image.load('./assets/menu/titulo.png')
# juego
imagen_fondo_juego = pygame.image.load('./assets/juego/fondo.jpeg')
fondo_juego = pygame.transform.scale(imagen_fondo_juego, SIZE_SCREEN)
imagen_no_powerups = pygame.image.load('./assets/juego/logo_nombre.webp')
# fin pregunta
imagen_fondo_fin_pregunta = pygame.image.load('./assets/fin_juego/fondo.png')
imagen_corazon = pygame.image.load('./assets/fin_juego/corazon.png')
corazon1 = pygame.transform.scale(imagen_corazon, (50, 50))
corazon2 = pygame.transform.scale(imagen_corazon, (50, 50))
corazon3 = pygame.transform.scale(imagen_corazon, (50, 50))
width_personaje = 175
height_personaje = 175
tamano_personaje = (width_personaje, height_personaje)
imagen_asustado = pygame.image.load('./assets/fin_juego/no_bien/asustado.png')
imagen_aterrado = pygame.image.load('./assets/fin_juego/no_bien/aterrado.png')
imagen_poker = pygame.image.load('./assets/fin_juego/no_bien/poker.png')
imagen_serio = pygame.image.load('./assets/fin_juego/no_bien/serio.png')
imagen_triste = pygame.image.load('./assets/fin_juego/no_bien/triste.png')
lista_imagenes_no_bien = [imagen_asustado, imagen_aterrado, imagen_poker, imagen_serio, imagen_triste]
imagen_a_gusto = pygame.image.load('./assets/fin_juego/bien/a_gusto.png')
imagen_avergonzado = pygame.image.load('./assets/fin_juego/bien/avergonzado.png')
imagen_confiado = pygame.image.load('./assets/fin_juego/bien/confiado.png')
imagen_feliz = pygame.image.load('./assets/fin_juego/bien/feliz.png')
imagen_sonriente = pygame.image.load('./assets/fin_juego/bien/sonriente.png')
lista_imagenes_bien = [imagen_a_gusto, imagen_avergonzado, imagen_confiado, imagen_feliz, imagen_sonriente]
for i in range(len(lista_imagenes_no_bien)):
    lista_imagenes_no_bien[i] = pygame.transform.scale(lista_imagenes_no_bien[i], tamano_personaje)
for i in range(len(lista_imagenes_bien)):
    lista_imagenes_bien[i] = pygame.transform.scale(lista_imagenes_bien[i], tamano_personaje)



# rects
# menu
boton_jugar_rect = pygame.Rect(WIDTH // 2 - (boton_jugar_width // 2), 520, boton_jugar_width, boton_jugar_height)
boton_sonido_rect = pygame.Rect(20, 20, 40, 40)
sonido = pygame.transform.scale(imagen_sonido, (boton_sonido_rect.width, boton_sonido_rect.height))
mute = pygame.transform.scale(imagen_mute, (boton_sonido_rect.width, boton_sonido_rect.height))
titulo_width = 650
titulo_height = 100
titulo_rect = pygame.Rect(CENTER_X - titulo_width // 2, 60, titulo_width, titulo_height)
titulo = pygame.transform.scale(imagen_titulo, (titulo_rect.width, titulo_rect.height))
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
width_no_powerups = 235
height_no_powerups = height_bloque_juego * 2
no_powerups = pygame.transform.scale(imagen_no_powerups, (width_no_powerups ,height_no_powerups))
width_rect_segundos = 40
height_rect_segundos = 40
segundos_rect = pygame.Rect(bloque_1_juego_rect.centerx - width_rect_segundos // 2, bloque_1_juego_rect.centery - height_rect_segundos // 2, width_rect_segundos, height_rect_segundos)
# fin pregunta
width_bloque_fondo_fin_pregunta = WIDTH // 1.5
height_bloque_fondo_fin_pregunta = HEIGHT // 2
bloque_fondo_fin_pregunta = pygame.Rect(CENTER_X - width_bloque_fondo_fin_pregunta // 2, CENTER_Y - height_bloque_fondo_fin_pregunta // 2, width_bloque_fondo_fin_pregunta, height_bloque_fondo_fin_pregunta)
fondo_fin_pregunta = pygame.transform.scale(imagen_fondo_fin_pregunta, (bloque_fondo_fin_pregunta.width, bloque_fondo_fin_pregunta.height))
width_bloque_continuar = 150
height_bloque_continuar = 30
bloque_continuar = pygame.Rect(bloque_fondo_fin_pregunta.centerx - width_bloque_continuar // 2, bloque_fondo_fin_pregunta.bottom - 40, width_bloque_continuar, height_bloque_continuar)

# configuracion sonidos
pygame.mixer.init()
# sonidos menu
sonido_fondo_menu = pygame.mixer.Sound('./assets/menu/sonido_fondo_prueba.mp3')
sonido_fondo_menu.set_volume(0.05)
sonido_click_boton_menu = pygame.mixer.Sound('./assets/menu/click_pop.mp3')
sonido_click_boton_menu.set_volume(0.3)
sonido_click_boton_jugar = pygame.mixer.Sound('./assets/menu/click_jugar.mp3')
sonido_click_boton_jugar.set_volume(0.2)
# sonidos juego
sonido_fondo_juego = pygame.mixer.Sound('./assets/juego/reloj.mp3')
sonido_fondo_juego.set_volume(0.1)
sonido_comienzo_juego = pygame.mixer.Sound('./assets/juego/despliegue_pregunta.mp3')
sonido_comienzo_juego.set_volume(0.5)
sonido_time_out_juego = pygame.mixer.Sound('./assets/juego/time_out.mp3')
sonido_time_out_juego.set_volume(0.5)
sonido_correcto_juego = pygame.mixer.Sound('./assets/juego/correcto.mp3')
sonido_time_out_juego.set_volume(0.5)
sonido_incorrecto_juego = pygame.mixer.Sound('./assets/juego/incorrecto.mp3')
sonido_time_out_juego.set_volume(0.5)
# sonidos fin pregunta
sonido_click_boton_continuar = pygame.mixer.Sound('./assets/fin_juego/click_pandereta.mp3')
sonido_click_boton_continuar.set_volume(0.5)

# tiempo
tick_1s = pygame.USEREVENT + 0
tick_2s = pygame.USEREVENT + 1
pygame.time.set_timer(tick_1s,1000)
pygame.time.set_timer(tick_2s,2000)

# settings juego
tiempo_para_responder = 5
lista_preguntas = listar_csv('preguntas.csv')
puntaje = 0
vidas_configuradas = 5
vidas = vidas_configuradas

def ejecutar_menu():
    global escena
    global muteado
    global vidas
    vidas = vidas_configuradas
    sonido_fondo_menu.play(-1)
    while escena == 'Menu Principal':
        pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_jugar_rect):
                    sonido_fondo_menu.stop()
                    sonido_click_boton_jugar.play()
                    escena = 'Juego'
                elif punto_colicion_rectangulo(coordenada_click, boton_sonido_rect):
                    sonido_click_boton_menu.play()
                    muteado = not muteado
        pantalla.blit(fondo_menu, (0, 0))
        pantalla.blit(titulo, titulo_rect.topleft)
        bloque_jugar = pygame.draw.rect(pantalla, color_boton_jugar, boton_jugar_rect, 0, 10)
        pygame.draw.rect(pantalla, NEGRO, boton_jugar_rect, 2, 10) # borde bloque "JUGAR"
        mostrar_texto(pantalla, 'JUGAR', fuente_jugar_menu, bloque_jugar.center, BLANCO, None)
        pygame.draw.rect(pantalla, NEGRO, boton_sonido_rect, 2, 10) # borde bloque sonido
        if muteado:
            pantalla.blit(mute, boton_sonido_rect.topleft)
            sonido_fondo_menu.set_volume(0)
            sonido_click_boton_menu.set_volume(0)
            sonido_click_boton_jugar.set_volume(0)
        else:
            pantalla.blit(sonido, boton_sonido_rect.topleft)
            sonido_fondo_menu.set_volume(0.10)
            sonido_click_boton_menu.set_volume(0.3)
            sonido_click_boton_jugar.set_volume(0.2)
        pygame.display.flip() # Muestro la pantalla

def ejecutar_juego():
    global escena
    global muteado
    global segundos
    global contesto_bien
    segundos = tiempo_para_responder
    sonido_comienzo_juego.play()
    pregunta = seleccionar_pregunta(lista_preguntas)
    color_bloque_reespuesta_a = BLANCO
    color_bloque_reespuesta_b = BLANCO
    color_bloque_reespuesta_c = BLANCO
    respuesta = None
    contesto_bien = None
    while escena == 'Juego':
        pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_sonido_rect):
                    sonido_click_boton_menu.play()
                    muteado = not muteado
                elif punto_colicion_rectangulo(coordenada_click, bloque_respuesta_a):
                    respuesta = 'a'
                    if respuesta == pregunta['respuesta_correcta']:
                        sonido_correcto_juego.play()
                        color_bloque_reespuesta_a = VERDE
                        contesto_bien = True
                    else:
                        sonido_incorrecto_juego.play()
                        color_bloque_reespuesta_a = ROJO
                        contesto_bien = False
                    escena = 'Fin Pregunta'
                    
                elif punto_colicion_rectangulo(coordenada_click, bloque_respuesta_b):
                    respuesta = 'b'
                    if respuesta == pregunta['respuesta_correcta']:
                        sonido_correcto_juego.play()
                        color_bloque_reespuesta_b = VERDE
                        contesto_bien = True
                    else:
                        sonido_incorrecto_juego.play()
                        color_bloque_reespuesta_b = ROJO
                        contesto_bien = False
                    escena = 'Fin Pregunta'
                elif punto_colicion_rectangulo(coordenada_click, bloque_respuesta_c):
                    respuesta = 'c'
                    if respuesta == pregunta['respuesta_correcta']:
                        sonido_correcto_juego.play()
                        color_bloque_reespuesta_c = VERDE
                        contesto_bien = True
                    else:
                        sonido_incorrecto_juego.play()
                        color_bloque_reespuesta_c = ROJO
                        contesto_bien = False
                    escena = 'Fin Pregunta'
                    
            if event.type == tick_1s:
                segundos -= 1
                if segundos == 5:
                    sonido_fondo_juego.play(-1, (segundos + 1) * 1000)
                elif segundos == -1:
                    sonido_time_out_juego.play()
                    escena = 'Fin Pregunta'
        pantalla.blit(fondo_juego, (0, 0))
        borde_bloque_sonido = pygame.draw.rect(pantalla, NEGRO, boton_sonido_rect, 2, 10)
        bloque_superior = pygame.draw.rect(pantalla, BLANCO, bloque_1_juego_rect, 0, 2)
        bloque_segundos_circulo = pygame.draw.rect(pantalla, NEGRO, segundos_rect, 5, 25)
        texto_segundos = f'{segundos}'
        if not texto_segundos.isdigit():
            texto_segundos = ';_;'
        mostrar_texto(pantalla, texto_segundos, fuente_juego, bloque_segundos_circulo.center, NEGRO, None)
        bloque_pregunta = pygame.draw.rect(pantalla, BLANCO, bloque_2_juego_rect, 0, 10)
        mostrar_texto(pantalla, pregunta['pregunta'], fuente_juego, bloque_pregunta.center, NEGRO, None)
        bloque_respuesta_a = pygame.draw.rect(pantalla, color_bloque_reespuesta_a, bloque_3_juego_rect, 0, 10)
        mostrar_texto(pantalla, pregunta['respuesta_a'], fuente_juego, bloque_respuesta_a.center, NEGRO, None)
        bloque_respuesta_b = pygame.draw.rect(pantalla, color_bloque_reespuesta_b, bloque_4_juego_rect, 0, 10)
        mostrar_texto(pantalla, pregunta['respuesta_b'], fuente_juego, bloque_respuesta_b.center, NEGRO, None)
        bloque_respuesta_c = pygame.draw.rect(pantalla, color_bloque_reespuesta_c, bloque_5_juego_rect, 0, 10)
        mostrar_texto(pantalla, pregunta['respuesta_c'], fuente_juego, bloque_respuesta_c.center, NEGRO, None)
        bloque_inferior = pygame.draw.rect(pantalla, BLANCO, bloque_6_juego_rect, 0, 2)
        pantalla.blit(no_powerups, (bloque_inferior.centerx - width_no_powerups // 2, bloque_inferior.centery - height_no_powerups // 2))

        if muteado:
            pantalla.blit(mute, boton_sonido_rect.topleft)
            sonido_comienzo_juego.set_volume(0)
            sonido_fondo_juego.set_volume(0)
            sonido_correcto_juego.set_volume(0)
            sonido_incorrecto_juego.set_volume(0)
            sonido_time_out_juego.set_volume(0)
        else:
            pantalla.blit(sonido, boton_sonido_rect.topleft)
            sonido_comienzo_juego.set_volume(0.5)
            sonido_fondo_juego.set_volume(0.1)
            sonido_correcto_juego.set_volume(0.5)
            sonido_incorrecto_juego.set_volume(0.5)
            sonido_time_out_juego.set_volume(0.5)
        pygame.display.flip() # Muestro la pantalla

def ejecutar_fin_pregunta():
    global escena
    global muteado
    global puntaje
    global vidas
    global contesto_bien
    if sonido_fondo_juego:
        sonido_fondo_juego.stop()
    match contesto_bien:
        case True:
            puntaje += 100
            imagen_personaje = lista_imagenes_bien[randrange(len(lista_imagenes_bien))]
            titulo_string = '¡BIEN HECHO!'
            color_titulo = VERDE
        case _:
            vidas -= 1
            imagen_personaje = lista_imagenes_no_bien[randrange(len(lista_imagenes_no_bien))]
            match contesto_bien:
                case False:
                    titulo_string = 'LA PROXIMA SERA...'
                    color_titulo = ROJO
                case None:
                    titulo_string = 'TE QUEDASTE SIN TIEMPO'
                    color_titulo = AMARILLO
    while escena == 'Fin Pregunta':
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_continuar):
                    sonido_click_boton_continuar.play()
                    if vidas > 0:
                        escena = 'Juego'
                    else:
                        escena = 'Game Over'
        pantalla.blit(fondo_fin_pregunta, bloque_fondo_fin_pregunta.topleft)
        pygame.draw.rect(pantalla, NEGRO, bloque_fondo_fin_pregunta, 8, 10) # borde imagen
        mostrar_texto(pantalla, titulo_string, fuente_titulo_fin_pregunta, (bloque_fondo_fin_pregunta.centerx, bloque_fondo_fin_pregunta.top + 25), color_titulo, None)
        pantalla.blit(imagen_personaje, (bloque_fondo_fin_pregunta.centerx - width_personaje // 2, bloque_fondo_fin_pregunta.centery - height_personaje // 2))
        mostrar_texto(pantalla, f'VIDAS', fuente_vidas_fin_pregunta, (bloque_fondo_fin_pregunta.left + 10 + 50 + 10 + 25, bloque_fondo_fin_pregunta.centery - 30), ROJO, None)
        if vidas >= 1:
            pantalla.blit(corazon1, (bloque_fondo_fin_pregunta.left + 10, bloque_fondo_fin_pregunta.centery))
        if vidas >= 2:
            pantalla.blit(corazon2, (bloque_fondo_fin_pregunta.left + 10 + 50 + 10, bloque_fondo_fin_pregunta.centery))
        if vidas >= 3:
            pantalla.blit(corazon3, (bloque_fondo_fin_pregunta.left + 10 + 50 + 10 + 50 + 10, bloque_fondo_fin_pregunta.centery))
        if vidas > 3:
            mostrar_texto(pantalla, f'+{vidas - 3}', fuente_juego, (bloque_fondo_fin_pregunta.left + 10 + 50 + 10 + 25, bloque_fondo_fin_pregunta.centery + 60), VIOLETA, None)
        boton_continuar = pygame.draw.rect(pantalla, VERDE_CLARO, bloque_continuar, 0, 10)
        mostrar_texto(pantalla, f'PUNTAJE', fuente_vidas_fin_pregunta, (bloque_fondo_fin_pregunta.right - 10 - 50 - 10 - 25, bloque_fondo_fin_pregunta.centery - 30), ROJO, None)
        mostrar_texto(pantalla, f'{puntaje}', fuente_juego, (bloque_fondo_fin_pregunta.right - 10 - 50 - 10 - 25, bloque_fondo_fin_pregunta.centery + 25), BLANCO, NEGRO)
        mostrar_texto(pantalla, 'CONTINUAR', fuente_continuar_fin_pregunta, bloque_continuar.center, BLANCO, None)
        pygame.display.flip()

def ejecutar_game_over():
    global escena
    global muteado
    global puntaje
    global vidas
    while escena == 'Game Over':
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_continuar):
                    escena = 'Menu Principal'
        pantalla.fill(NEGRO)
        boton_continuar = pygame.draw.rect(pantalla, VERDE_CLARO, bloque_continuar, 0, 10)
        mostrar_texto(pantalla, 'CONTINUAR', fuente_continuar_fin_pregunta, bloque_continuar.center, BLANCO, None)
        pygame.display.flip()

while funcionando:
    lista_preguntas = listar_csv('preguntas.csv')
    match escena:
        case 'Menu Principal':
            ejecutar_menu()
        case 'Configuracion':
            # ejecutar_configuracion()
            pass
        case 'Juego':
            ejecutar_juego()
        case 'Fin Pregunta':
            ejecutar_fin_pregunta()
        case 'Game Over':
            ejecutar_game_over()

pygame.quit()
sys.exit()