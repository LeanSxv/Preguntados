import pygame
from random import randrange
from variables import *
from archivos import listar_csv

def color_rgb_aleatorio():
    return (randrange(256), randrange(256), randrange(256))

def terminar():
    pygame.quit()
    exit()
    
def mostrar_texto(superficie, texto, fuente, coordenadas, color_fuente, color_fondo=NEGRO):
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

def seleccionar_pregunta(lista_preguntas):
    return lista_preguntas[randrange(len(lista_preguntas))]

