import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mini Battle Royale')

# Load and scale the background image
background_image = pygame.image.load('minigame2.jpg')  # Replace with your image file path
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors for drawing the player
SKIN_COLOR = (255, 224, 189)  # A skin-like color
SHIRT_COLOR = (0, 0, 255)     # Blue shirt
PANTS_COLOR = (128, 0, 0)     # Dark red pants

# Player settings
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5

def draw_player(position):
    # Head
    pygame.draw.rect(screen, SKIN_COLOR, (position[0] + 10, position[1], 30, 30))
    # Body
    pygame.draw.rect(screen, SHIRT_COLOR, (position[0], position[1] + 30, 50, 50))
    # Legs
    pygame.draw.rect(screen, PANTS_COLOR, (position[0], position[1] + 80, 20, 50))
    pygame.draw.rect(screen, PANTS_COLOR, (position[0] + 30, position[1] + 80, 20, 50))

def move_player(player_pos, dx, dy):
    player_pos[0] += dx * player_speed
    player_pos[1] += dy * player_speed
    # Boundary checking
    player_pos[0] = max(0, min(SCREEN_WIDTH - 50, player_pos[0]))
    player_pos[1] = max(0, min(SCREEN_HEIGHT - 130, player_pos[1]))

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    dx = dy = 0
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
    screen.blit(background_image, (0, 0))  # Draw the background image
    draw_player(player_pos)
    pygame.display.flip()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
