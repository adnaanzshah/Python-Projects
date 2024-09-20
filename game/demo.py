import pygame
import random

pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Advanced Game")

# Colors
background_color = (0, 0, 0)  # Black
player_color = (0, 255, 0)    # Green
enemy_color = (255, 0, 0)     # Red
bullet_color = (255, 255, 0)  # Yellow

# Player position
player_x = 370
player_y = 480
player_x_change = 0

# Enemy positions
num_of_enemies = 6
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
for i in range(num_of_enemies):
    enemy_x.append(random.randint(0, 750))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)

# Bullet position
bullet_x = 0
bullet_y = 480
bullet_y_change = 0.5
bullet_state = "ready"  # "ready" means you can't see the bullet on the screen

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player_draw(x, y):
    pygame.draw.rect(screen, player_color, (x, y, 50, 50))

def enemy_draw(x, y, i):
    pygame.draw.rect(screen, enemy_color, (x, y, 50, 50))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, bullet_color, (x + 20, y + 10, 10, 20))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    return distance < 27

# Main game loop
running = True
while running:
    screen.fill(background_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change

    # Boundary checking for player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 750:
        player_x = 750

    # Update enemy positions
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 750:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i]

        # Collision detection
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 750)
            enemy_y[i] = random.randint(50, 150)

        enemy_draw(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player_draw(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()

pygame.quit()