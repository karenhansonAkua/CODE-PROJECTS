"""
import pgzrun
from random import randint
apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10 , 800)
    apple.y = randint(10 , 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("GOOD SHOOT!")
        place_apple()
    else:
        print("YOU MISSED!")
        quit()

place_apple()
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FRUIT_SIZE = 50
PLAYER_SIZE = 50

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot the Fruit")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("player.png")
fruit_image = pygame.image.load("fruit.png")

# Set up the player
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - PLAYER_SIZE)

# List to store fruit rectangles
fruits = []

# Function to generate a new fruit
def create_fruit():
    x = random.randint(0, WIDTH - FRUIT_SIZE)
    y = random.randint(0, HEIGHT - FRUIT_SIZE)
    fruit_rect = fruit_image.get_rect()
    fruit_rect.topleft = (x, y)
    fruits.append(fruit_rect)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            click_rect = pygame.Rect(mx, my, 1, 1)
            for fruit in fruits[:]:
                if fruit.colliderect(click_rect):
                    fruits.remove(fruit)

    # Update logic
    create_fruit()

    # Draw everything
    screen.fill(WHITE)

    for fruit in fruits:
        screen.blit(fruit_image, fruit)

    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)


