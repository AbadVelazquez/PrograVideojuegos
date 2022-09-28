# Importar Pygame.
import pygame
# Varaibles para tamaño, velocidad, posicion, colores, etc
dimX = 800 #Variables para resolicion de la pantalla
dimY = 600
tamPelota = 27 # Variable para el tamaño de la pelota
pos = [tamPelota,tamPelota]  # Var para la posicion inicial de la pelota
posPelolas = {
    1: [tamPelota,tamPelota], #pelota1
    2: [tamPelota,tamPelota], #pelota2
    3: [tamPelota,tamPelota], #pelota3
    4: [tamPelota,tamPelota], #pelota4
    5: [tamPelota,tamPelota], #pelota5
    6: [tamPelota,tamPelota], #pelota6
    7: [tamPelota,tamPelota], #pelota7
    8: [tamPelota,tamPelota], #pelota8
    9: [tamPelota,tamPelota], #pelota9
    10: [tamPelota,tamPelota] #pelota10
    
}
#velocidad = [5,5] 
numTPelotas=0 #Var para el numero total de pelotas
velocidades=[] #Varaibles para almacenar las velocidades de las pelotas (1,3,10 pixeles)  
fps = 60 # Variable para determinar los frames per seconds
#https://www.delftstack.com/es/howto/python/colors-in-python/
colors= {       # Dicciinario para almacenar la lista de colores disponibles
    1 : (255,0,0),  # Rojo - Red
    2 : (0,255,0),  # Verde - Green
    3 : (0,0,255),   # Azul - Blue
    4 : (255,255,0),   # Amarillo
    5 : (255,117,0),   # Naranja
    6 : (148,0,211),   # Violeta
    7 : (255,0,255),   # Magenta
    8 : (0,255,255),   # Cyan
    9 : (139,69,19),   # Cafe
    0 : (255,255,255)   # blanco
}

# Solicita el numero de pelotas totales y valida si esta en el rango valido (numTPelotas <= 10)
# en caso q no este en el rango, vueve a solicitar el num de pelotas
while True:
    numTPelotas = int(input('\nIngrese el número de pelotas (max 10): '))
    if numTPelotas > 10 or numTPelotas < 1:
        print(' El número de pelotas no es valido, intente de nuevo.')
    else: break

# Se modifica el tamaño de la pelota dependiendo el numero de pelotas totales
#tamPelota = dimX // numTPelotas

# Solicita la velicidad de cada pelota/
cont = 1
while cont<=numTPelotas:
    while True:
        v = int(input(f'Ingrese la velocidad de la pelota {cont} (1,3,5,10,etc): '))
        if v <= 0:
            print(' La velocidad dada no es valido (velocidad > 0), intente de nuevo.')
        else: break
    velocidades.append([v,v])
    cont+=1
print(velocidades)
# Se solicita el color de cada pelota
cont = 1
listColorPelotas=[] #Var q almacena el color de cada pelota
c=-1 #var para color aux
while cont<=numTPelotas:
    while True:
        c = int(input(f"""\nSeleccione un color para la pelota {cont}:
    1. Rojo,
    2. Verde,
    3. Azul,
    4. Amarillo,
    5. Naranja,
    6. Violeta,
    7. Magenta,
    8. Cyan,
    9. Cafe,
    0. Blanco.
 Color seleccionado para pelota {cont}: """))
        if c<0 or c>9:
            print(' El color seleccionado no es valido, intente de nuevo.')
        elif c in listColorPelotas:
            print(f' El color {c} ya a sido seleccionado, intente de nuevo.')
        else: break
    listColorPelotas.append(c)
    cont+=1
        
def showPelota(colores,poss, veloc):
    #print(f'colores,poss, veloc = {colores},{poss},{veloc}')
    pygame.draw.circle(screen, colores, poss, tamPelota, 0)
    if(poss[0] < tamPantalla[0] - tamPelota): #se mueve la pelota
        poss[0] = poss[0]+veloc[0]
    else:
        poss[0]=poss[0] #si llega al "borde" de la derecha se detiene
    
# Inicializar Pygame.
pygame.init()
tamPantalla = (dimX, dimY)
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)
# Poner el título de la ventana.
pygame.display.set_caption("Mi Juego: Practica 1 (parte 1)")

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((0, 0, 139))# Azul Obscuro (0, 0, 255))#Azul
# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 
salir = False

# Loop principal (game loop) del juego.
while not salir:

    # Timer que controla el frame rate.
    clock.tick(fps)

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
    
    if 1 <= numTPelotas:
        #showPelota(colores,poss, velocidad):'''
        showPelota(colors[listColorPelotas[0]],pos, velocidades[0])
        print(f'pos1 : {pos}, vel: {velocidades[0]}')
    if 2 <= numTPelotas:
        posy=tamPelota*3 #posicion Y de proxima pelota
        showPelota(colors[listColorPelotas[1]],[pos[0],(posy+10)], velocidades[1])
        print(f'Pos2 : {pos}, Vel2: {velocidades[1]}')
    if 3 <= numTPelotas:
        posy=tamPelota*5
        showPelota(colors[listColorPelotas[2]],[pos[0],(posy+15)], velocidades[2])
        print(f'Pos3 : {pos}, Vel2: {velocidades[2]}')
    if 4 <= numTPelotas:
        posy=tamPelota*7
        showPelota(colors[listColorPelotas[3]],[pos[0],(posy+20)], velocidades[3])
        print(f'Pos4 : {pos}, Vel2: {velocidades[3]}')
    if 5 <= numTPelotas:
        posy=tamPelota*9
        showPelota(colors[listColorPelotas[4]],[pos[0],(posy+25)], velocidades[4])
        print(f'Pos5 : {pos}, Vel2: {velocidades[4]}')
    if 6 <= numTPelotas:
        posy=tamPelota*11
        showPelota(colors[listColorPelotas[5]],[pos[0],(posy+30)], velocidades[5])
        print(f'Pos6 : {pos}, Vel2: {velocidades[5]}')
    if 7 <= numTPelotas:
        posy=tamPelota*13
        showPelota(colors[listColorPelotas[6]],[pos[0],(posy+35)], velocidades[6])
        print(f'Pos7 : {pos}, Vel2: {velocidades[6]}')
    if 8 <= numTPelotas:
        posy=tamPelota*15
        showPelota(colors[listColorPelotas[7]],[pos[0],(posy+40)], velocidades[7])
        print(f'Pos8 : {pos}, Vel2: {velocidades[7]}')
    if 9 <= numTPelotas:
        posy=tamPelota*17
        showPelota(colors[listColorPelotas[8]],[pos[0],(posy+45)], velocidades[8])
        print(f'Pos9 : {pos}, Vel2: {velocidades[8]}')
    if 10 <= numTPelotas:
        posy=tamPelota*19
        showPelota(colors[listColorPelotas[9]],[pos[0],(posy+50)], velocidades[9])
        print(f'Pos10 : {pos}, Vel2: {velocidades[9]}')
    
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()

