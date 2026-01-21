import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 1500, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mover Cuadrado con Flechas")

# Colores
black = (0, 0, 0)
blue = (0, 0, 255)  # Color del jugador
red = (255, 0, 0)    # Color del enemigo

# Tamaños
square_size = 50
speed = 6

# Posición del jugador
x = (width - square_size) // 2
y = (height - square_size) // 2

# Crear enemigos
num_enemies = 15
enemies = []

for _ in range(num_enemies):
    enemy_x = random.randint(0, width - square_size)
    enemy_y = random.randint(-height, 0)
    enemy_speed = random.randint(5, 10)
    enemies.append([enemy_x, enemy_y, enemy_speed])

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    
    # Mover el jugador
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Limitar el movimiento del jugador dentro de la ventana
    x = max(0, min(x, width - square_size))
    y = max(0, min(y, height - square_size))

    # Actualizar la posición de los enemigos
    for enemy in enemies:
        enemy[1] += enemy[2]  # Mueve el enemigo hacia abajo

        # Si el enemigo sale de la ventana, respawnea en la parte superior
        if enemy[1] > height:
            enemy[1] = random.randint(-height, 0)
            enemy[0] = random.randint(0, width - square_size)
            enemy[2] = random.randint(5, 10)

    # Comprobar colisiones entre el jugador y los enemigos
    player_rect = pygame.Rect(x, y, square_size, square_size)
    
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], square_size, square_size)
        
        # Colisión entre el jugador y el enemigo
        if player_rect.colliderect(enemy_rect):
            pygame.quit()  # Cierra Pygame si hay colisión
            sys.exit()

        # Colisiones entre enemigos
        for other_enemy in enemies:
            if enemy != other_enemy:
                other_enemy_rect = pygame.Rect(other_enemy[0], other_enemy[1], square_size, square_size)
                if enemy_rect.colliderect(other_enemy_rect):
                    # Reiniciar la posición de ambos enemigos
                    enemy[1] = random.randint(-height, 0)
                    enemy[0] = random.randint(0, width - square_size)
                    enemy[2] = random.randint(5, 10)
                    
                    other_enemy[1] = random.randint(-height, 0)
                    other_enemy[0] = random.randint(0, width - square_size)
                    other_enemy[2] = random.randint(5, 10)

                    # Multiplicar enemigos
                    new_enemy_x = random.randint(0, width - square_size)
                    new_enemy_y = random.randint(-height, 0)
                    new_enemy_speed = random.randint(5, 10)
                    enemies.append([new_enemy_x, new_enemy_y, new_enemy_speed])  # Agregar nuevo enemigo

    # Limpiar la pantalla
    window.fill(black)

    # Dibujar el jugador (cuadrado azul)
    pygame.draw.rect(window, blue, (x, y, square_size, square_size))

    # Dibujar los enemigos (cuadrados rojos)
    for enemy in enemies:
        pygame.draw.rect(window, red, (enemy[0], enemy[1], square_size, square_size))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la tasa de frames
    pygame.time.Clock().tick(60)
