import pygame # Importar e inicializar Pygame.
import random
pygame.init()
tamPantalla = (800,600)
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)
# Poner el título de la ventana.
pygame.display.set_caption("Juego Pong (part1)")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((0, 0, 139))# Azul Obscuro (0, 0, 255))#Azul
# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 
salir = False
# Loop principal (game loop) del juego.
pos =[ 50, 50]
velocidad=[5,5]
posXR1 = 50
posXR2 = 720
posYR1 = 20 #random.randrange(10,600)
posYR2 = 20
def movRec1(posxR1, posyR1,vel):
    if(posyR1 < 20):
        posyR1 += vel
    if(posyR1 > tamPantalla[1]):
        posyR1 -= vel
def movRec2(posxR2, posyR2,vel):
    if(posyR2 < 20):
        posyR2 += vel
    if(posyR2 > tamPantalla[1]):
        posyR2 -= vel

while not salir:

    # Timer que controla el frame rate.
    clock.tick(60)

    # Procesar los eventos que llegan a la aplicación.
    for event in pygame.event.get():
        # Si se cierra la ventana se sale del programa.
        if event.type == pygame.QUIT:
           salir = True

        # Si se pulsa la tecla [Esc] se sale del programa.
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_ESCAPE:
               salir = True

   # Actualizar la pantalla.
   
    screen.blit(imgBackground, (0, 0))
    pygame.draw.circle(screen, GREEN, pos, 30, 0)

    # Rectangulo de marco 
    pygame.draw.rect(screen, WHITE, [30, 10, 740, 500], 1)
    #rectangulos
    pygame.draw.rect(screen, BLACK, [posXR1, posYR1, 30, 200])#[50, 20, 30, 200])
    pygame.draw.rect(screen, BLACK, [posXR2, posYR2, 30, 200])#[720, 20, 30, 200])
    movRec1(posXR1,posYR1, velocidad[1])
    movRec1(posXR2,posYR2, velocidad[1])
    posYR1 += velocidad[1]
    posYR2 += velocidad[1]
    pos[1] = pos[1] + velocidad[1]
    pos[0] = pos[0] + velocidad[0]
    #print(pos)
    '''Validar las posiciones o limites de la pantalla y el objeto
    Limite de los laterales
    '''
    if(pos[0] < 50):
        velocidad[0] = 5
    if(pos[0]> tamPantalla[0] - 50):
        velocidad[0] =  -5
    #Limites Superior Inferior
    if(pos[1] < 50):
        velocidad[1] = 5
    if(pos[1] > tamPantalla[1] - 50):
        velocidad[1] = -5
    #print(posXR1, '-', posYR1)
   #pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()