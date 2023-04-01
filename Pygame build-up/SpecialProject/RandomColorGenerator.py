import pygame
import random

class ColorGenerator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        self.running = True
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    color = [random.randint(0, 255) for i in range(3)]
                    hex_color = "#{:02X}{:02X}{:02X}".format(*color)
                    text = self.font.render(hex_color, True, (255, 255, 255))
                    self.screen.fill(color)
                    self.screen.blit(text, (100, 100))
                    pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    color_generator = ColorGenerator()
    color_generator.run()
