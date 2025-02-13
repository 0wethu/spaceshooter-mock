import pygame 
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_img = pygame.image.load("player.png")
player_width = 64
player_height = 64
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Set up the enemy
enemy_img = pygame.image.load("enemy.png")
enemy_width = 64
enemy_height = 64
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = random.randint(50, 150)
enemy_speed = 2

# Set up the bullets
bullet_img = pygame.image.load("bullet.png")
bullet_width = 32
bullet_height = 32
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"  # "ready" - ready to be fired, "fire" - bullet is moving

# Set up the score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def player(x, y):
    window.blit(player_img, (x, y))


def enemy(x, y):
    window.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (x + player_width / 2 - bullet_width / 2, y - bullet_height))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:
        return True
    return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, WHITE)
    window.blit(score, (x, y))


def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, WHITE)
    window.blit(over_text, (WIDTH / 2 - 200, HEIGHT / 2 - 50))


# Game loop
running = True
while running:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

    # Player movement boundary
    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Enemy movement
    enemy_x += enemy_speed
    if enemy_x < 0:
        enemy_speed = 2
        enemy_y += enemy_height
   
