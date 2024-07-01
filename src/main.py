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
imagen_fondo_fin_pregunta = pygame.image.load('./assets/fin_juego/fondo.jpg')
imagen_personaje_bueno_fin_pregunta = pygame.image.load('./assets/fin_juego/feliz.png')
imagen_personaje_malo_fin_pregunta = pygame.image.load('./assets/fin_juego/enojado.png')


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
width_bloque_fondo_fin_pregunta = WIDTH // 2
height_bloque_fondo_fin_pregunta = HEIGHT // 3
bloque_fondo_fin_pregunta = pygame.Rect(CENTER_X - width_bloque_fondo_fin_pregunta // 2, CENTER_Y - height_bloque_fondo_fin_pregunta // 2, width_bloque_fondo_fin_pregunta, height_bloque_fondo_fin_pregunta)
fondo_fin_pregunta = pygame.transform.scale(imagen_fondo_fin_pregunta, (bloque_fondo_fin_pregunta.width, bloque_fondo_fin_pregunta.height))
widht_personaje = 100
height_personaje = 100
personaje_bueno = pygame.transform.scale(imagen_personaje_bueno_fin_pregunta, (widht_personaje, height_personaje))
personaje_malo = pygame.transform.scale(imagen_personaje_malo_fin_pregunta, (widht_personaje, height_personaje))
width_bloque_continuar = 150
height_bloque_continuar = 30
bloque_continuar = pygame.Rect(bloque_fondo_fin_pregunta.centerx - width_bloque_continuar // 2, bloque_fondo_fin_pregunta.centery + height_personaje // 2 + height_bloque_continuar // 2, width_bloque_continuar, height_bloque_continuar)

# configuracion sonidos
pygame.mixer.init()
# sonidos menu
sonido_fondo_menu = pygame.mixer.Sound('./assets/menu/sonido_fondo_prueba.mp3')
sonido_fondo_menu.set_volume(0.05)
sonido_fondo_menu.play(-1)
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

# tiempo
tick_1s = pygame.USEREVENT + 0
tick_2s = pygame.USEREVENT + 1
pygame.time.set_timer(tick_1s,1000)
pygame.time.set_timer(tick_2s,2000)

# settings juego
milisegundos = 0
tiempo_para_responder = 15
lista_preguntas = listar_csv('preguntas.csv')
pregunta = seleccionar_pregunta(lista_preguntas)
puntaje = 0
vidas = 3

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
                escena = 'Juego'
                break
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
    global funcionando
    global escena
    global muteado
    global segundos
    global milisegundos
    global lista_preguntas
    global contesto_bien
    segundos = tiempo_para_responder
    sonido_comienzo_juego.play()
    pregunta = seleccionar_pregunta(lista_preguntas)
    color_bloque_reespuesta_a = BLANCO
    color_bloque_reespuesta_b = BLANCO
    color_bloque_reespuesta_c = BLANCO
    juganding = True
    respuesta = None
    chau = False
    contesto_bien = None
    while juganding:
        pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                chau = True
                juganding = False
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
                    juganding = False
                    
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
                    juganding = False
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
                    juganding = False
                    
            if event.type == tick_1s:
                segundos -= 1
                if segundos == 5:
                    sonido_fondo_juego.play(-1, segundos * 1000)
                elif segundos == -1:
                    sonido_time_out_juego.play()
                    juganding = False
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
    if chau:
        funcionando = False
    else:
        escena = 'Fin Pregunta'

def ejecutar_fin_pregunta():
    global funcionando
    global escena
    global muteado
    global puntaje
    global vidas
    global contesto_bien
    fin_pregunta = True
    if sonido_fondo_juego:
        sonido_fondo_juego.stop()
    match contesto_bien:
        case True:
            puntaje += 100
            imagen_personaje = personaje_bueno
            titulo_string = '¡BIEN HECHO!'
            color_titulo = VERDE
        case _:
            vidas -= 1
            imagen_personaje = personaje_malo
            match contesto_bien:
                case False:
                    titulo_string = 'LA PROXIMA SERA...'
                    color_titulo = ROJO
                case None:
                    titulo_string = 'TE QUEDASTE SIN TIEMPO'
                    color_titulo = AMARILLO
    print(vidas)
    print(puntaje)
    while fin_pregunta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_continuar):
                    fin_pregunta = False
        pantalla.blit(fondo_fin_pregunta, bloque_fondo_fin_pregunta.topleft)
        mostrar_texto(pantalla, titulo_string, fuente_titulo_fin_pregunta, (bloque_fondo_fin_pregunta.centerx, bloque_fondo_fin_pregunta.top + 25), color_titulo, None)
        pantalla.blit(imagen_personaje, (bloque_fondo_fin_pregunta.centerx - widht_personaje // 2, bloque_fondo_fin_pregunta.centery - height_personaje // 2))
        boton_continuar = pygame.draw.rect(pantalla, VERDE_CLARO, bloque_continuar, 0, 10)
        mostrar_texto(pantalla, 'CONTINUAR', fuente_continuar_fin_pregunta, bloque_continuar.center, BLANCO, None)
        pygame.display.flip()
    if vidas > 0:
        escena = 'Juego'
    else:
        escena = 'Game Over'

def ejecutar_game_over():
    global funcionando
    global escena
    global muteado
    global puntaje
    global vidas
    print(puntaje)
    not_continuar = True
    while not_continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coordenada_click = event.pos
                if punto_colicion_rectangulo(coordenada_click, boton_continuar):
                    not_continuar = False
        pantalla.fill(NEGRO)
        boton_continuar = pygame.draw.rect(pantalla, VERDE_CLARO, bloque_continuar, 0, 10)
        mostrar_texto(pantalla, 'CONTINUAR', fuente_continuar_fin_pregunta, bloque_continuar.center, BLANCO, None)
        pygame.display.flip()
    vidas = 3
    escena = 'Menu Principal'

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