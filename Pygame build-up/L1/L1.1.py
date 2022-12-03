import pygame

pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      pass
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()