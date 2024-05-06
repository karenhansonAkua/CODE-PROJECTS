# Import necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0) #1-red, 2,green,3-blue
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create a font object for displaying text
font = pygame.font.Font(None, 36)

# Initial positions and direction of the snake
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = (20, 0)

# Initial position of the food
food = (
    random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
)

# Game state variables
running = True
game_over = False
score = 0

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input for snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 20):
        snake_direction = (0, -20)
    if keys[pygame.K_DOWN] and snake_direction != (0, -20):
        snake_direction = (0, 20)
    if keys[pygame.K_LEFT] and snake_direction != (20, 0):
        snake_direction = (-20, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-20, 0):
        snake_direction = (20, 0)

    # Update game logic if the game is not over
    if not game_over:
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check if the snake ate the food
        if snake[0] == food:
            score += 1
            # Generate new food at a random position
            food = (
                random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
            )
        else:
            # If the snake did not eat the food, remove the last segment
            snake.pop()

        # Check if the snake collided with the screen boundaries or itself
        if (
            snake[0][0] < 0
            or snake[0][0] >= WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= HEIGHT
            or snake[0] in snake[1:]
        ):
            game_over = True

    # Draw the game elements on the screen
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display "Game Over" text if the game is over
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
# Import necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create a font object for displaying text
font = pygame.font.Font(None, 36)

# Initial positions and direction of the snake
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = (20, 0)

# Initial position of the food
food = (
    random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
)

# Game state variables
running = True
game_over = False
score = 0

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input for snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 20):
        snake_direction = (0, -20)
    if keys[pygame.K_DOWN] and snake_direction != (0, -20):
        snake_direction = (0, 20)
    if keys[pygame.K_LEFT] and snake_direction != (20, 0):
        snake_direction = (-20, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-20, 0):
        snake_direction = (20, 0)

    # Update game logic if the game is not over
    if not game_over:
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check if the snake ate the food
        if snake[0] == food:
            score += 1
            # Generate new food at a random position
            food = (
                random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
            )
        else:
            # If the snake did not eat the food, remove the last segment
            snake.pop()

        # Check if the snake collided with the screen boundaries or itself
        if (
            snake[0][0] < 0
            or snake[0][0] >= WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= HEIGHT
            or snake[0] in snake[1:]
        ):
            game_over = True

    # Draw the game elements on the screen
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display "Game Over" text if the game is over
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
