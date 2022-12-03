import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)


y = 0 # GLOBAL

class Scoreboard:
    def __init__(self, screen, count) :
        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)
        countdown = 30 - count

        # Countdown
        self.label = f"{countdown}"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 125))

        index = '00'
        global y
        y += 1
        if y >= 0 and y < 20:
            x = str(y)
            if len(x) == 1:
                index = '0' + x
            else:
                index = x
        else:
            y = 0
            x = str(y)
            if len(x) == 1:
                index = '0' + x
            else:
                index = x

        img = f"asset/frame_{index}_delay-0.1s.png"
        picture1 = pygame.image.load(img)
        
        self.image1 = pygame.transform.scale(picture1, (150, 150))
        self.imageRect1 = self.image1.get_rect(center=(100, 125))

        # Bar
        max_length = WIDTH//3

        
        if not (countdown == 0):
            percentage = countdown / 30
            fill = percentage * max_length
        else:
            fill = 0

        print(max_length, fill)        
        pygame.draw.rect(screen,(0,0,255),( (max_length,HEIGHT*2//3) ,(int(fill),20) )) # Fill
        pygame.draw.rect(screen,(0,0,0),( (max_length,HEIGHT*2//3),(max_length, 20) ),4) # Border

class Result:
   def __init__(self, p1, p2): 
        self.font = pygame.font.Font('freesansbold.ttf', 40)  
        if p1 > p2:
            self.text = "Player 1 win!"
        elif p1 < p2:
            self.text = "Player 2 win!"
        else:
            self.text = "Draw!"
        self.textBox = self.font.render(str(self.text), True, (0,0,0), (255,255,255))           
        self.textRect = self.textBox.get_rect(center=(WIDTH//2, HEIGHT//2))

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Player1 = 0
    Player2 = 0
    state = 0
    run = True
    count = 0
    
    while run:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            pass
        if count >= 30:
            count = 0
        count += 1
        sleep(0.1)

        screen1 = Scoreboard(screen, int(count))
        screen.blit(screen1.TextLabel, screen1.TextRect)
        screen.blit(screen1.image1, screen1.imageRect1)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()