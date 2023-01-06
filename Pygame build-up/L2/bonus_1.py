# Controlling positions

import pygame

# Game Setup
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300


class Screen:
    def __init__(self, text, w, h, c) :
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.label = text
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(w, h))   # Change position

# The main game loop

def main():
    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2
    r,g,b = 0, 0, 0

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    PADDING = 50

    run = True

    while run :
        BACKGROUND = (r,g,b)
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

                if event.key == pygame.K_a:
                    if w > PADDING:
                        w = w - 10
                if event.key == pygame.K_d:
                    if w < WINDOW_WIDTH-PADDING:
                        w = w + 10
                if event.key == pygame.K_w:
                    if h > PADDING:
                        h = h - 10
                if event.key == pygame.K_s:
                    if h < WINDOW_HEIGHT-PADDING:
                        h = h + 10

                ##
                if event.key == pygame.K_u:
                    r += 5
                    if r > 255:
                        r = 255
                if event.key == pygame.K_j:
                    r -= 5
                    if r < 0:
                        r = 0
                if event.key == pygame.K_i:
                    g += 5
                    if g > 255:
                        g = 255
                if event.key == pygame.K_k:
                    g -= 5
                    if g < 0:
                        g = 0
                if event.key == pygame.K_o:
                    b += 5
                    if b > 255:
                        b = 255
                if event.key == pygame.K_l:
                    b -= 5
                    if b < 0:
                       b = 0



        text = f"({r}, {g}, {b})"
        test_screen = Screen(text, w, h, (r,b,g))
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
