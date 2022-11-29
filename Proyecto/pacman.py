import sys
import pygame
import random
#Programa que pone en la ventana de pygame los segundos trascurridos
pygame.init()

width = 600
heigth = 600

surface = pygame.display.set_mode((width,heigth)) 
pygame.display.set_caption('PacMan')

#color con RGB
NEGRO = (0,0,0)
WHITE = (255,255,255)
GRIS = (111,111,111)
AZUL = (0,0,255)
color_random1 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
color_random2 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

surface.fill(NEGRO) #color de superficie

#Se carga el sonido
introSound = pygame.mixer.Sound('./sounds/game_start.wav')
#pygame.mixer.music.load('./sounds/siren_1.wav')
#pygame.mixer.music.set_volume(1.0) # Float 0.0 - 1.0        
#reproduce la musica para (musica de fondo)
#pygame.mixer.music.play(1, 0.0) #primer aargumento para el numero de veces a repeter, segundo es el minuto a iniciar 
#                      -1 es argumento para q nunca deje de sonar 
#introSound.play()
#sirenaSound = pygame.mixer.music.load('./sounds/siren_1.wav')

#pygame.mixer.music.set_volume(1.0) #agusta el volumen de la musica
#pygame.mixer.music.play(-1, 0.0)
class Circulo():
    def __init__(self, color, radio, posX, posY):
        self.color = color
        self.radio = radio
        self.posX = posX
        self.posY = posY


while True:
    '''seconds = pygame.time.get_ticks() // 1000
    #print(seconds)
    if seconds > 5:
        pygame.mixer.music.play(-1, 0.0)'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Si se pulsa la tecla [Esc] se sale del programa.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    #                          (posX, posY, ancho, alto)
    #pygame.draw.rect(surface,AZUL,[20, 20, 450, 10],0, 1)
    pygame.draw.rect(surface,AZUL,[20, 20, 560, 10],0, 5) #barra sub
    #pygame.draw.rect(surface,AZUL,[20, 20, 10, 500],0, 5) #barra izq
    #pygame.draw.rect(surface,AZUL,[570, 20, 10, 500],0, 5) #barra der
    pygame.draw.rect(surface,AZUL,[20, 510, 560, 10],0, 5) #barra inferior

    

    pygame.draw.rect(surface,AZUL,[20, 20, 10, 230],0, 5) #barra izq arriba
    pygame.draw.rect(surface,AZUL,[20, 290, 10, 230],0, 5) #barra izq abajo

    pygame.draw.rect(surface,AZUL,[570, 20, 10, 230],0, 5) #barra der arriba
    pygame.draw.rect(surface,AZUL,[570, 290, 10, 230],0, 5) #barra der abajo
    
    pygame.draw.rect(surface,color_random1,[20, 240, 120, 10],0, 5)
    pygame.draw.rect(surface,color_random1,[20, 290, 120, 10],0, 5)

    pygame.draw.rect(surface,color_random1,[460, 240, 120, 10],0, 5)
    
    pygame.draw.rect(surface,GRIS,[40,35, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[10,255, 580, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[145,40, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[425,40, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[40,475, 520, 30],0, 15)
    pygame.draw.circle(surface,color_random2,[25,270],15) 

    pygame.display.update() #actualiza display

