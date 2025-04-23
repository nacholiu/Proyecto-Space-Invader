import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla de juego
ANCHO = 800
ALTO = 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invader 🚀")

# Colores
NEGRO = (0, 0, 0) #Fondo
BLANCO = (255, 255, 255) #Bala

# Jugador
nave_img = pygame.Surface((50, 10)) # Cambia el tamaño del jugador
nave_img.fill((0, 255, 0))
Poscion_nave_x = ANCHO // 2
Poscion_nave_y = ALTO - 10
velocidad = 5

# Bucle principal
reloj = pygame.time.Clock()
movimiento = True

while movimiento:
    reloj.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            movimiento = False

    # Teclas para mover el jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and Poscion_nave_x > 0:
        Poscion_nave_x -= velocidad
    if teclas[pygame.K_RIGHT] and Poscion_nave_x < ANCHO - 50:
        Poscion_nave_x += velocidad

    # Dibujar fondo y jugador
    pantalla.fill(NEGRO)
    pantalla.blit(nave_img, (Poscion_nave_x, Poscion_nave_y))
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()

