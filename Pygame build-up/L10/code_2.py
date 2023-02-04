import pygame

# Initialize Pygame
pygame.init()

# Define the screen size and title
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Timer")

# Define the timer font
timer_font = pygame.font.Font(None, 36)

# Define color themes
themes = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

# Set the default theme
theme = "red"

# Set the timer duration in seconds
duration = 10

# Set the start time
start_time = pygame.time.get_ticks()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key events to switch themes
        if event.type == pygame.KEYDOWN:
            if event.unicode == "r":
                theme = "red"
            elif event.unicode == "g":
                theme = "green"
            elif event.unicode == "b":
                theme = "blue"

    # Clear the screen
    screen.fill((255, 255, 255))

    # Calculate the time remaining
    time_remaining = duration - (pygame.time.get_ticks() - start_time) / 1000

    # Render the timer text
    timer_text = timer_font.render(str(time_remaining), True, themes[theme])
    timer_rect = timer_text.get_rect()
    timer_rect.center = (200, 150)

    # Draw the timer
    screen.blit(timer_text, timer_rect)

    # Update the display
    pygame.display.update()

    # End the game loop when the timer is up
    if time_remaining <= 0:
        running = False

# Quit Pygame
pygame.quit()
