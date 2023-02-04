import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)

class Screen1:
    def __init__(self, WINDOW):
        self.font = pygame.font.Font('freesansbold.ttf', 40)  
        self.text = 'Welcome'
        self.textBox = self.font.render(str(self.text), True, (0,0,0), (255,255,255))           
        self.textRect = self.textBox.get_rect(center=(WIDTH//2, HEIGHT//2))
        WINDOW.blit(self.textBox, self.textRect)

class Screen2:
    def __init__(self, WINDOW):
        pygame.draw.polygon(WINDOW, (0,255,0), ((100, 140), (120, 120), (130, 160), (120, 200), (110, 180))) 

class Screen3:
    def __init__(self, WINDOW):
        pygame.draw.polygon(WINDOW, (0,255,255), ((100, 140), (120, 120), (130, 160), (120, 200), (110, 180))) 

def main():
    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    state = 1  

    while run:
        WINDOW.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_a:
                    state = (state + 1) % 3

        if state == 0:
            s1 = Screen1(WINDOW)
        elif state == 1:
            s2 = Screen2(WINDOW)
        elif state == 2:
            s3 = Screen3(WINDOW)
        

        pygame.display.flip()
        clock.tick(60)
            

if __name__ == "__main__":
    main()