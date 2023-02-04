import pygame

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the main menu screen class
class MainMenuScreen:
    def __init__(self):
        self.title_font = pygame.font.Font(None, 50)
        self.menu_font = pygame.font.Font(None, 30)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Transition to the game screen
                        game_screen = GameScreen()
                        game_screen.run()

            screen.fill(WHITE)

            title = self.title_font.render("Main Menu", True, BLACK)
            press_space = self.menu_font.render("Press SPACE to start", True, BLACK)

            screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_HEIGHT / 4))
            screen.blit(press_space, (SCREEN_WIDTH / 2 - press_space.get_width() / 2, SCREEN_HEIGHT / 2))

            pygame.display.update()

# Define the game screen class
class GameScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Transition to the main menu screen
                        main_menu_screen = MainMenuScreen()
                        main_menu_screen.run()

            screen.fill(WHITE)

            message = self.font.render("Playing the game", True, BLACK)
            screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2))

            pygame.display.update()

# Run the main menu screen
main_menu_screen = MainMenuScreen()
main_menu_screen.run()

# Quit Pygame
pygame.quit()
