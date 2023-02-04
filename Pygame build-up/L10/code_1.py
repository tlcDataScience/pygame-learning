import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Timer")

# Define the timer duration
duration = 10
start_time = pygame.time.get_ticks()

# Create a font to display the timer
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    remaining_time = duration - elapsed_time

    # Render the timer text
    text = font.render("Time remaining: " + str(int(remaining_time)), True, (0, 0, 0))
    screen.blit(text, (100, 100))

    # Update the display
    pygame.display.update()

    # End the timer if the duration has been reached
    if remaining_time <= 0:
        running = False

# Quit Pygame
pygame.quit()
