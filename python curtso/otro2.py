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
white = (255, 255, 255)  # Color para el texto
game_over_color = (255, 0, 0)  # Color para el texto de Game Over
shield_color = (0, 255, 0)  # Color para el escudo (bordes)

# Tamaños
square_size = 50
shield_size = 70  # Tamaño del escudo (mayor que el jugador)
initial_enemy_speed = 1  # Velocidad inicial de los enemigos
initial_enemy_count = 5  # Número inicial de enemigos

# Posición del jugador (inicialización)
x = (width - square_size) // 2
y = (height - square_size) // 2

def create_enemies(num, speed):
    """Función para crear enemigos."""
    enemies = []
    for _ in range(num):
        enemy_x = random.randint(0, width - square_size)
        enemy_y = random.randint(-height, 0)
        enemies.append([enemy_x, enemy_y, speed])
    return enemies

# Crear enemigos iniciales
enemies = create_enemies(initial_enemy_count, initial_enemy_speed)

# Inicializar puntuación
score = 0
score_timer = pygame.time.get_ticks()  # Temporizador para los puntos
shield_timer = 0  # Temporizador para el escudo
shield_duration = 5000  # Duración del escudo en milisegundos (5 segundos)

# Configuración de la fuente
font = pygame.font.Font(None, 36)  # Fuente predeterminada de Pygame
game_over_font = pygame.font.Font(None, 72)  # Fuente para Game Over
option_font = pygame.font.Font(None, 48)  # Fuente para las opciones
purchase_font = pygame.font.Font(None, 36)  # Fuente para las compras

# Estado del juego
game_over = False
shield_active = False  # Estado del escudo

# Contador externo para la dificultad
difficulty_counter = 0  # Comenzar el contador de dificultad en 0
difficulty_increment_time = 10000  # Incrementar dificultad cada 10 segundos
last_difficulty_update = pygame.time.get_ticks()  # Temporizador para la dificultad

# Crear un reloj para controlar la tasa de frames
clock = pygame.time.Clock()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    
    if not game_over:
        # Mover el jugador
        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_UP]:
            y -= 5
        if keys[pygame.K_DOWN]:
            y += 5

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

        # Comprobar colisiones entre el jugador y los enemigos
        player_rect = pygame.Rect(x, y, square_size, square_size)
        
        for enemy in enemies[:]:  # Iterar sobre una copia para poder eliminar elementos
            enemy_rect = pygame.Rect(enemy[0], enemy[1], square_size, square_size)
            
            # Colisión entre el jugador y el enemigo
            if player_rect.colliderect(enemy_rect):
                if not shield_active:  # Solo si no hay escudo
                    game_over = True  # Cambia el estado a game over
            
            # Colisión entre el escudo y el enemigo
            if shield_active:
                shield_rect = pygame.Rect(x - 10, y - 10, shield_size, shield_size)
                if shield_rect.colliderect(enemy_rect):
                    enemies.remove(enemy)  # Eliminar el enemigo al colisionar con el escudo
                    score += 1  # Aumentar la puntuación al destruir un enemigo

        # Actualizar la puntuación cada segundo
        current_time = pygame.time.get_ticks()
        if current_time - score_timer >= 500:  # 1000 ms = 1 segundo 
            score += 1
            score_timer = current_time  # Reiniciar el temporizador

        # Aumentar dificultad cada 10 segundos
        if current_time - last_difficulty_update >= difficulty_increment_time:  
            initial_enemy_count += 1  # Aumentar el número de enemigos
            initial_enemy_speed += 1  # Aumentar la velocidad de los enemigos
            enemies = create_enemies(initial_enemy_count, initial_enemy_speed)  # Crear nuevos enemigos
            last_difficulty_update = current_time  # Reiniciar el temporizador de dificultad

        # Asegurar que siempre haya enemigos en pantalla
        while len(enemies) < initial_enemy_count:
            enemies.append([random.randint(0, width - square_size), random.randint(-height, 0), initial_enemy_speed])

        # Limpiar la pantalla
        window.fill(black)

        # Dibujar el escudo si está activo
        if shield_active:
            shield_rect = pygame.Rect(x - 10, y - 10, shield_size, shield_size)
            pygame.draw.rect(window, shield_color, shield_rect, 2)  # Dibujar el escudo (bordes)

            # Comprobar si el escudo ha durado más de la duración permitida
            if current_time - shield_timer >= shield_duration:
                shield_active = False  # Desactivar el escudo

        # Dibujar el jugador (cuadrado azul)
        pygame.draw.rect(window, blue, (x, y, square_size, square_size))

        # Dibujar los enemigos (cuadrados rojos)
        for enemy in enemies:
            pygame.draw.rect(window, red, (enemy[0], enemy[1], square_size, square_size))

        # Mostrar la puntuación en la parte superior izquierda
        score_text = font.render(f"Puntos: {score}", True, white)
        window.blit(score_text, (10, 10))

        # Opciones de compra
        purchase_text = purchase_font.render("Presiona S para comprar escudo (10 puntos)", True, white)
        window.blit(purchase_text, (10, 40))

        # Comprobar si el jugador puede comprar el escudo
        if keys[pygame.K_s] and score >= 10:
            score -= 10  # Reducir los puntos por el escudo
            shield_active = True  # Activar el escudo
            shield_timer = current_time  # Reiniciar el temporizador del escudo

    else:
        # Pantalla de Game Over
        window.fill(black)
        game_over_text = game_over_font.render("Game Over", True, game_over_color)
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 50))
        window.blit(game_over_text, text_rect)

        # Mostrar la puntuación final
        final_score_text = font.render(f"Puntos: {score}", True, white)
        final_score_rect = final_score_text.get_rect(center=(width // 2, height // 2 + 50))
        window.blit(final_score_text, final_score_rect)

        # Opciones de continuar y salir
        continue_text = option_font.render("Presiona C para Continuar", True, white)
        continue_rect = continue_text.get_rect(center=(width // 2, height // 2 + 100))
        window.blit(continue_text, continue_rect)

        exit_text = option_font.render("Presiona Q para Salir", True, white)
        exit_rect = exit_text.get_rect(center=(width // 2, height // 2 + 150))
        window.blit(exit_text, exit_rect)

        # Comprobar teclas para opciones
        if keys[pygame.K_c]:  # Continuar
            # Reiniciar el juego
            score = 0
            game_over = False
            enemies = create_enemies(initial_enemy_count, initial_enemy_speed)  # Crear enemigos nuevamente
            last_difficulty_update = pygame.time.get_ticks()  # Reiniciar el temporizador de dificultad
        if keys[pygame.K_q]:  # Salir
            pygame.quit()
            sys.exit()

    # Actualizar la ventana
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 fps
