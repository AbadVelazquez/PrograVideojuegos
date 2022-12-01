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
ROJO = (255,0,0)
VERDE = (0,255,0)
color_random1 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
color_random2 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


# Crear la superficie del fondo o background
surfaceBackground = pygame.Surface(surface.get_size())
surfaceBackground = surfaceBackground.convert()
surfaceBackground.fill(NEGRO) #color de superficie

# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 

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
    color=[255,255,255]
    radio=2
    posX=0
    posY=0
    velocidad=5
    def __init__(self, color, radio, posX, posY, velocidad):
        self.color = color
        self.radio = radio
        self.posX = posX
        self.posY = posY
        self.velocidad = velocidad
    
    def avanza(self):
        #Evento de Teclado
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: # flecha derecha
            self.posY += self.velocidad
        if keys[pygame.K_LEFT]: # flecha izq
            self.posY -= self.velocidad
        if keys[pygame.K_UP]: # flecha arriba
            self.posX += self.velocidad
        if keys[pygame.K_DOWN]: # flecha abajo
            self.posX -= self.velocidad
        '''if keys[pygame.K_RIGHT]: # flecha derecha
            pos[0] += 1
        if keys[pygame.K_LEFT]: # flecha izq
            pos[0]-= 1
        if keys[pygame.K_UP]: # flecha arriba
            pos[1] -= 1
        if keys[pygame.K_DOWN]: # flecha abajo
            pos[1] += 1'''

#Pos Inicio [300,378]
pos = [300,378]#[48,104]#[25,270]
vel = 5
def movPelota():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]: # flecha derecha
        pos[0] += 1
    if keys[pygame.K_LEFT]: # flecha izq
        pos[0]-= 1
    if keys[pygame.K_UP]: # flecha arriba
        pos[1] -= 1
    if keys[pygame.K_DOWN]: # flecha abajo
        pos[1] += 1
    #print(pos)


while True:
    # Timer que controla el frame rate.
    clock.tick(60)
    surface.blit(surfaceBackground,(0,0))
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
    pygame.draw.rect(surface,AZUL,[20, 20, 560, 10],0, 5) #barra sub  # Rect 1
    pygame.draw.rect(surface,AZUL,[20, 510, 560, 10],0, 5) #barra inferior # Rect 8

    #   pygame.draw.rect(surface,AZUL,[20, 20, 10, 500],0, 5) #barra izq 
    pygame.draw.rect(surface,AZUL,[20, 20, 10, 170],0, 5) #barra izq arriba # Rect 2
    pygame.draw.rect(surface,AZUL,[20, 290, 10, 230],0, 5) #barra izq abajo # Rect 7
    
    #   pygame.draw.rect(surface,AZUL,[570, 20, 10, 500],0, 5) #barra der 
    pygame.draw.rect(surface,AZUL,[570, 20, 10, 170],0, 5) #barra der arriba # Rect 14
    pygame.draw.rect(surface,AZUL,[570, 290, 10, 230],0, 5) #barra der abajo # Rect 9
    
    pygame.draw.rect(surface,AZUL,[20, 180, 100, 10],0, 5) # Rect 3
    pygame.draw.rect(surface,AZUL,[20, 240, 100, 10],0, 5) # Rect 5
    pygame.draw.rect(surface,AZUL,[20, 290, 100, 10],0, 5) # Rect 6 
    pygame.draw.rect(surface,AZUL,[110, 180, 10, 70],0, 5) # Rect 4

    pygame.draw.rect(surface,AZUL,[480, 180, 100, 10],0, 5) # Rect 13
    pygame.draw.rect(surface,AZUL,[480, 240, 100, 10],0, 5) # Rect 11
    pygame.draw.rect(surface,AZUL,[480, 290, 100, 10],0, 5) # Rect 10 
    pygame.draw.rect(surface,AZUL,[480, 180, 10, 70],0, 5) # Rect 12


    #Lineas guias
    #Lineas Horizontales
    pygame.draw.rect(surface,GRIS,[40,35, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,90, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,145, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[10,255, 580, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,305, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,362, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,420, 520, 30],0, 15)
    pygame.draw.rect(surface,GRIS,[40,475, 520, 30],0, 15)
    #Lineas Verticales
    pygame.draw.rect(surface,GRIS,[125,40, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[445,40, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[35,50, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[535,50, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[185,50, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[385,50, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[250,50, 30, 450],0, 15)
    pygame.draw.rect(surface,GRIS,[320,50, 30, 450],0, 15)
    #       pygame.draw.circle(surface,WHITE,[25,270],15) 

    pygame.draw.rect(surface,ROJO,[65, 65, 56, 20],0, 10)       # Rect 15
    pygame.draw.rect(surface,ROJO,[160, 65, 85, 20],0, 10)      # Rect 16
    pygame.draw.rect(surface,ROJO,[65, 120, 56, 20],0, 10)      # Rect 20
    pygame.draw.rect(surface,ROJO,[288, 30, 25,55],0, 10,1,1)   # Rect 17
    pygame.draw.rect(surface,ROJO,[480, 65, 56, 20],0, 10)      # Rect 19
    pygame.draw.rect(surface,ROJO,[355, 65, 85, 20],0, 10)      # Rect 18
    pygame.draw.rect(surface,ROJO,[480, 120, 56, 20],0, 10)     # Rect 21

    pygame.draw.rect(surface,ROJO,[220, 120, 160, 20],0, 10)    # Rect 22
    pygame.draw.rect(surface,ROJO,[288, 140, 25,60],0, 10,1,1) # Rect 23

    pygame.draw.rect(surface,ROJO,[160, 120, 25,130],0, 10) # Rect 24
    pygame.draw.rect(surface,ROJO,[185, 180, 60, 20],0, 10,1,-1,1,-1) # Rect 25

    pygame.draw.rect(surface,ROJO,[415, 120, 25,130],0, 10) # Rect 26
    pygame.draw.rect(surface,ROJO,[355, 180, 60, 20],0, 10,-1,1,-1,1) # Rect 27

    pygame.draw.rect(surface,ROJO,[220, 235, 25,15],0, 5)       # Rect 28
    pygame.draw.rect(surface,ROJO,[355, 235, 25,15],0, 5)       # Rect 29
    pygame.draw.rect(surface,ROJO,[160, 290, 25,20],0, 5)       # Rect 30
    pygame.draw.rect(surface,ROJO,[415, 290, 25,20],0, 5)       # Rect 31

    pygame.draw.rect(surface,ROJO,[220, 290, 160, 20],0, 10)    # Rect 32
    #          pygame.draw.rect(surface,ROJO,[288, 310, 25,48],0, 10,1,1) # Rect 33  v2
    pygame.draw.rect(surface,ROJO,[288, 235, 25,125],0, 10)    # Rect 33

    pygame.draw.rect(surface,ROJO,[220, 395, 160, 20],0, 10)    # Rct 34
    pygame.draw.rect(surface,ROJO,[288, 415, 25,60],0, 10,1,1)  # Rect 35
    
    pygame.draw.rect(surface,ROJO,[160, 338, 85, 20],0, 10)     # Rect 36
    pygame.draw.rect(surface,ROJO,[355, 338, 85, 20],0, 10)     # Rect 37

    pygame.draw.rect(surface,ROJO,[65, 338, 55, 20],0, 10)      # Rect 38
    pygame.draw.rect(surface,ROJO,[100, 338, 20, 80],0, 10)     # Rect 39
    
    pygame.draw.rect(surface,ROJO,[480, 338, 55, 20],0, 10)     # Rect 40
    pygame.draw.rect(surface,ROJO,[480, 338, 20, 80],0, 10)     # Rect 41
    
    pygame.draw.rect(surface,ROJO,[30, 395, 35, 20],0, 10,1,-1,1,-1) # Rect 42
    pygame.draw.rect(surface,ROJO,[535, 395, 35, 20],0, 10,-1,1,-1,1) # Rect 43

    pygame.draw.rect(surface,ROJO,[65, 452, 180, 20],0, 10)     # Rect 44
    pygame.draw.rect(surface,ROJO,[160, 395, 25,58],0, 10,-1,-1,1,1) # Rect 45

    pygame.draw.rect(surface,ROJO,[355, 452, 180, 20],0, 10)    # Rect 46
    pygame.draw.rect(surface,ROJO,[415, 395, 25,58],0, 10,-1,-1,1,1) # Rect 47

    pygame.draw.circle(surface,VERDE,pos,13) 
    

    movPelota()
    #pygame.display.update() #actualiza display
    pygame.display.flip()
