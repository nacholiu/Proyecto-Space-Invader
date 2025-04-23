import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla 
ANCHO = 800
ALTO = 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invader 🚀")

# Colores
NEGRO = (0, 0, 0) #Fondo
BLANCO = (255, 255, 255) #Bala

# Jugador
jugador_img = pygame.Surface((50, 10)) # Cambia el tamaño del jugador
jugador_img.fill((0, 255, 0))
Poscion_jugador_x = ANCHO // 2
Poscion_jugador_y = ALTO - 10
velocidad = 5

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    reloj.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Teclas para mover el jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and Poscion_jugador_x > 0:
        Poscion_jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and Poscion_jugador_x < ANCHO - 50:
        Poscion_jugador_x += velocidad

    # Dibujar fondo y jugador
    pantalla.fill(NEGRO)
    pantalla.blit(jugador_img, (Poscion_jugador_x, Poscion_jugador_y))
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()

