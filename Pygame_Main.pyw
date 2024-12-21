# Importing modules.
import pygame
import random
import sys
import os

# Importing sub-modules.
from random import randint

# Initializing modules.
pygame.init()

# Settings section.
# Variables section.
running = True
mouse_visibility = True
clock = pygame.time.Clock()

# Specials variables
__version__ = "v1.0.0"

# Constants section.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

SCREEN_TITLE = "Pygame_Main"
FPS = 60
PLAYER_SPEED = 10

# Colors tuple section.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ALPHA = GREEN

# Setting up screen.
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} | {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(mouse_visibility)

# Functions section.
# Exit game function.
def exit():
    pygame.quit()
    sys.exit()
    running = False

# Class section.
# Hero class.
class Corenyatcha(pygame.sprite.Sprite):
    def __init__(self, pos_x=400, pos_y=300, scale_by=2):
        super().__init__()
        self.image = pygame.image.load("assets/corenyatcha-logo.png")
        self.image = pygame.transform.scale(self.image, (self.image.size[0] // scale_by, self.image.size[1] // scale_by))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect(center = [pos_x, pos_y])

    # Update hero method.
    def update(self):
        pass    #self.rect.y -= (PLAYER_SPEED * 

# Creating Hero group.
corenyatcha_group = pygame.sprite.Group()
corenyatcha = Corenyatcha()
corenyatcha_group.add(corenyatcha)

# Main game loop.
while running:

    # Delta time.
    dt = (clock.tick(FPS) / 1000)

    # If key pressed statements.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Keyboard imput.
    keys = pygame.key.get_pressed()

    # Basic movement logic.
    # Move foreward.
    #if keys[pygame.K_w]:
        #corenyatcha.rect.y -= (PLAYER_SPEED * dt)

    # Filling screen with black.
    SCREEN.fill(BLACK)

    # Drawing sprites on the screen.
    corenyatcha_group.update()
    corenyatcha_group.draw(SCREEN)

    # FPS counter.
    pygame.display.flip()
    clock.tick(FPS)
