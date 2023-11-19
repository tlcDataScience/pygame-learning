import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Sound Player")

# Load sound
sound = pygame.mixer.Sound('cardinal-37075.wav')
sound2 = pygame.mixer.Sound('sisters-voices-103432.wav')
# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                sound.play()
            if event.key == pygame.K_s:
                sound2.play()
    

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()