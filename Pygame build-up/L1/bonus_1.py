import pygame

pygame.init()

r, g, b = 0, 0, 0

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ChangeDetected = False
listUpdated = False 

lst = []

# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
        ChangeDetected = True
        if event.key == pygame.K_a:
            r += 5
            if r > 255:
                r = 255
        if event.key == pygame.K_z:
            r -= 5
            if r < 0:
                r = 0
        if event.key == pygame.K_s:
            g += 5
            if g > 255:
                g = 255
        if event.key == pygame.K_x:
            g -= 5
            if g < 0:
                g = 0
        if event.key == pygame.K_d:
            b += 5
            if b > 255:
                b = 255
        if event.key == pygame.K_c:
            b -= 5
            if b < 0:
                b = 0
        if event.key == pygame.K_p:
            lst.append((r,g,b))
            listUpdated = True


    if ChangeDetected:
        ChangeDetected = False
        print(f" (r,g,b) = ({r}, {g}, {b})")
        if listUpdated:
            print("="*10)
            for i in lst:
                print(i)
        print("="*10)
        BACKGROUND = (r, g, b)
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()
