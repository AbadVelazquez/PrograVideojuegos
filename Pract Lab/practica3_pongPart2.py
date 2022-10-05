import pygame # Importar e inicializar Pygame.
import random
pygame.init()
tamPantalla = (800,600)
tamPelota = 30
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)
# Poner el título de la ventana.
pygame.display.set_caption("Juego Pong (part2)")

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
pos =[ 355, 245]
velocidad=[5,5] #Velocidad de pelota
velBarra1 =[4,4] #Velocidad de barra 1
velBarra2 =[4,4] #Velocidad de barra 1
posXR1 = 50
posXR2 = 720
posYR1 = random.randrange(20,300)
posYR2 = random.randrange(20,300)#20
def movRec1(posxR1, posyR1,vel):
    if(posyR1 < 22):
        velBarra1[1] = -vel
        #print('B1 borde superior ^|')
    if(posyR1 > tamPantalla[1] - 300):
        velBarra1[1] = -vel
        #print('B1 borde innf v|')
def movRec2(posxR2, posyR2,vel):
    if(posyR2 < 20):
        velBarra2[1] = -vel
        #print('B2 borde superior ^|')
    if(posyR2 > tamPantalla[1] - 300):
        velBarra2[1] = -vel
        #print('B2 borde innf v|')
def movPelota(posX, posY):
    #tamPantalla = (800,600) 
    #pygame.draw.rect(screen, WHITE, [30, 10, 740, 500], 1) # dim del rectangulo de marco
    if(posX < (tamPelota + 31)):
        velocidad[0] = -velocidad[0]
    if(posX> tamPantalla[0] - tamPelota -31):
        velocidad[0] = -velocidad[0]
    #Limites Superior Inferior
    if(posY < (tamPelota + 11)):
        velocidad[1] = -velocidad[1]
    if(posY > tamPantalla[1] - tamPelota -91):
        velocidad[1] = -velocidad[1]
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
    pygame.draw.circle(screen, GREEN, pos, tamPelota, 0)

    # Rectangulo de marco 
    pygame.draw.rect(screen, WHITE, [30, 10, 740, 500], 1)
    #rectangulos
    
    pygame.draw.rect(screen, BLACK, [posXR1, posYR1, 30, 200])#[50, 20, 30, 200])
    pygame.draw.rect(screen, BLACK, [posXR2, posYR2, 30, 200])#[720, 20, 30, 200])
    movRec1(posXR1,posYR1, velBarra1[1])
    movRec2(posXR2,posYR2, velBarra2[1])
    #posYR1 += velBarra1[1]
    #
     #Evento de Teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        posYR1 += velBarra1[1]
    if keys[pygame.K_s]:
        posYR1 += velBarra1[1]
    if keys[pygame.K_UP]:
        posYR2 += velBarra2[1]
    if keys[pygame.K_DOWN]:
        posYR2 += velBarra2[1]
    pos[1] = pos[1] + velocidad[1]
    pos[0] = pos[0] + velocidad[0]
    #print(pos)
    movPelota(pos[0], pos[1])
    '''Validar las posiciones o limites de la pantalla y el objeto
    Limite de los laterales
    
    if(pos[0] < 50):
        velocidad[0] = 5
    if(pos[0]> tamPantalla[0] - 50):
        velocidad[0] =  -5
    #Limites Superior Inferior
    if(pos[1] < 50):
        velocidad[1] = 5
    if(pos[1] > tamPantalla[1] - 50):
        velocidad[1] = -5
    '''
    #print(posXR1, '-', posYR1)
    #pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()