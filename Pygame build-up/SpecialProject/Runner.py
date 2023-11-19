import pygame
import sys

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 255, 255))

    def render(self, screen):
        screen.blit(self.surface, (0, 0))

class WelcomeScreen(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.font = pygame.font.Font(None, 72)
        self.big_font = pygame.font.Font(None, 36)

    def render(self, screen):
        super().render(screen)

        welcome_text = self.font.render("Toast Run", True, (0, 0, 0))
        welcome_rect = welcome_text.get_rect(center=(self.width // 2, self.height // 2 - 36))
        self.surface.blit(welcome_text, welcome_rect)

        start_text = self.big_font.render("To start, press A", True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(self.width // 2, self.height // 2 + 36))
        self.surface.blit(start_text, start_rect)

class GameOverScreen(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.font = pygame.font.Font(None, 72)
        self.big_font = pygame.font.Font(None, 36)

    def render(self, screen):
        super().render(screen)

        game_over_text = self.big_font.render("Game Over", True, (0, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 36))
        self.surface.blit(game_over_text, game_over_rect)

        restart_text = self.font.render("To restart, press R", True, (0, 0, 0))
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 36))
        self.surface.blit(restart_text, restart_rect)

class ScoreScreen(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.font = pygame.font.Font(None, 36)

    def render(self, screen, score, high_score):
        super().render(screen)

        score_text = self.font.render("Score: " + str(score), True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        self.surface.blit(score_text, score_rect)

        high_score_text = self.font.render("High Score: " + str(high_score), True, (0, 0, 0))
        high_score_rect = high_score_text.get_rect()
        high_score_rect.topleft = (10, score_rect.bottom + 10)
        self.surface.blit(high_score_text, high_score_rect)

class Game:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Score Example")

        self.clock = pygame.time.Clock()

        self.welcome_screen = WelcomeScreen(self.width, self.height)
        self.game_over_screen = GameOverScreen(self.width, self.height)
        self.score_screen = ScoreScreen(self.width, self.height)

        self.score = 0
        self.high_score = 0
        self.game_over = True
        self.welcome = True

    def run(self):
        while True:
            self.handle_events()
            self.update_logic()
            self.render()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart_game()
                elif event.key == pygame.K_e and self.game_over:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a and self.welcome:
                    self.start_game()
                elif event.key == pygame.K_SPACE and not self.game_over:
                    self.increment_score()

    def update_logic(self):
        if not self.game_over:
            # Game logic here

            if self.score >= 100:
                self.game_over = True

    def render(self):
        self.screen.fill((255, 255, 255))

        if self.welcome:
            self.welcome_screen.render(self.screen)
        elif self.game_over:
            self.game_over_screen.render(self.screen)
            self.score_screen.render(self.screen, self.score, self.high_score)
        else:
            self.score_screen.render(self.screen, self.score, self.high_score)

    def restart_game(self):
        self.welcome = False
        self.game_over = False
        self.score = 0

    def start_game(self):
        self.welcome = False
        self.game_over = False
        self.score = 0

    def increment_score(self):
        self.score += 10

if __name__ == "__main__":
    game = Game()
    game.run()
