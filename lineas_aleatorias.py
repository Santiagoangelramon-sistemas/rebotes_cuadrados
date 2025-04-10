import pygame
import sys
import random


rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)



color_aleatorio = random.randint (0, 225)

pygame.init()

ventana = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Dibujar formas con pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # Rellenar la ventana de color 
    ventana.fill(negro)

    # Dibujar formas con el metodo pygame.draw

    # Dibujar una linea 
    pygame.draw.line(ventana, color_aleatorio,(100,100),(300,300))
    pygame.draw.line(ventana, color_aleatorio,(100,300),(300,100))
    pygame.draw.line(ventana, color_aleatorio,(150,100),(300,300))
    pygame.draw.line(ventana, color_aleatorio,(300,200),(160,100))
    pygame.draw.line(ventana, color_aleatorio,(100,110),(300,110))
    pygame.draw.line(ventana, color_aleatorio,(120,100),(170,300))


    # Dibujar un rectangulo

    # rectangulo sin relleno,esquina sup. izq: (100,100),esquina. inf. der: (150,200).

    pygame.draw.rect(ventana,blanco , ((100,100),(475,475)), 1)


    # Agregar texto
    # Fuente tipo Arial, tamaño 35, negrilla y cursiva.
    fuente_arial = pygame.font.SysFont("Arial", 39, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 3, blanco)
    ventana.blit(texto,(100,20))

    fuente_arial = pygame.font.SysFont("Arial", 31, 1, 1)
    texto = fuente_arial.render("Mistery Dream (Santiago Angel Ramon)", 2, blanco)
    ventana.blit(texto,(80,600))
    # Actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################