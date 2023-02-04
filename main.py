import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

# Define a font for the text input
font = pygame.font.Font(None, 32)

# Create a text input box
text_input = pygame.Rect(100, 150, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_active
active = False
text = ''

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You entered: ", text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) < 15:
                    text += event.unicode

    # Render the text input box
    screen.fill((30, 30, 30))
    txt_surface = font.render(text, True, (0,0,0))
    width = max(200, txt_surface.get_width()+10)
    text_input.w = width
    pygame.draw.rect(screen, color, text_input)
    screen.blit(txt_surface, (text_input.x+5, text_input.y+5))
    pygame.display.update()

# Quit pygame
pygame.quit()
