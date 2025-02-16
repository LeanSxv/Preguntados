import pygame
from random import randrange, shuffle
from variables import *

def color_rgb_aleatorio():
    return (randrange(256), randrange(256), randrange(256))

def terminar():
    pygame.quit()
    exit()
    
def mostrar_texto(superficie, texto, fuente, coordenadas, color_fuente, color_fondo= None):
    # Renderiza el texto con la fuente y los colores especificados
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    # Obtiene el rectángulo del texto renderizado
    rect_texto = sup_texto.get_rect()
    # Centra el rectángulo en las coordenadas especificadas
    rect_texto.center = coordenadas
    # Dibuja el texto en la superficie
    superficie.blit(sup_texto, rect_texto)

def crear_bloque(imagen = False, left = 0, top = 0, ancho = 40, alto = 40, color = NEGRO, borde = 0, radio = -1):
    rectangulo = pygame.Rect(left, top, ancho, alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return {"rectangulo": rectangulo, "color": color, "borde": borde, "radio": radio, "imagen": imagen}

def punto_colicion_rectangulo(coordenada, rect):
    x, y = coordenada
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def ordenar_lista_orden_aleatorio(lista: list):
    shuffle(lista)

def seleccionar_pregunta(lista_de_preguntas):
    global indice_preguntas
    if indice_preguntas == 0:
        ordenar_lista_orden_aleatorio(lista_de_preguntas)
    pregunta = lista_de_preguntas[indice_preguntas]
    indice_preguntas += 1
    if indice_preguntas >= len(lista_de_preguntas):
        indice_preguntas = 0
    return pregunta

