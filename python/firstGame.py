import pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 640, 480
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Boundary checking
    player_x = max(0, min(player_x, WIDTH))
    player_y = max(0, min(player_y, HEIGHT))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

pygame.quit()
