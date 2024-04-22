import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mini Battle Royale')

# Colors
BLACK = (255, 255, 255)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
player_speed = 5

def draw_player(position):
    pygame.draw.rect(screen, GREEN, (position[0], position[1], player_size, player_size))

def move_player(player_pos, dx, dy):
    player_pos[0] += dx * player_speed
    player_pos[1] += dy * player_speed
    # Boundary checking
    player_pos[0] = max(0, min(SCREEN_WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(SCREEN_HEIGHT - player_size, player_pos[1]))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = 1

    move_player(player_pos, dx, dy)

    # Rendering
    screen.fill(BLACK)
    draw_player(player_pos)
    pygame.display.flip()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
