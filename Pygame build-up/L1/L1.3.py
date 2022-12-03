# ADD IN KEYBOARD TO CONTROL THE COLOR


import pygame

pygame.init()

r, g, b = 0, 0, 0
 
# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            r = 255
          if event.key == pygame.K_z:
            r = 0
          if event.key == pygame.K_s:
            g = 255
          if event.key == pygame.K_x:
            g = 0
          if event.key == pygame.K_d:
            b = 255
          if event.key == pygame.K_c:
            b = 0
          

    BACKGROUND = (r, g, b)                
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()