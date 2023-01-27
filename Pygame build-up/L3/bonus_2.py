import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300

class Scoreboard:
    def __init__(self, p1, p2, v) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), v)
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0,0,0), v)
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(100, 125))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0,0,0), v)           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(100, 225))

        # LINE
        self.dividerLabel = "|"
        self.dividerTextLabel = self.font1.render(str(self.dividerLabel), True, (0,0,0), v)
        self.dividerTextLabelRect = self.dividerTextLabel.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0), v)
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-100,125))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), v)   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-100, 225))
 
class Result():
    def __init__(self, hist) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.TextLabel = []
        self.TextRect = []
        #
        count = 0
        for i in hist:
            self.label = f"{i}"
            self.TextLabel.append(self.font.render(str(self.label), True, (0,0,0), (255,255,255)))
            self.TextRect.append(self.TextLabel[count - 1].get_rect(topleft=(WIDTH//3, HEIGHT//10*(2+count))))
            count += 1

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Player1 = 0
    Player2 = 0
    state = 0
    run = True
    r, g, b = 255, 255, 255
    hist = []
    
    while run:
        BACKGROUND = (r, g, b)
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and state == 0:
                if event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_a:
                    if Player1 < 20:
                        Player1 += 1
                elif event.key == pygame.K_s:
                    if Player2 < 20:
                        Player2 += 1
                elif event.key == pygame.K_z:
                    if Player1 != 0:
                        Player1 -= 1
                elif event.key == pygame.K_x:
                    if Player2 != 0:
                        Player2 -= 1
                elif event.key == pygame.K_r:
                    Player1 = 0
                    Player2 = 0
                elif event.key == pygame.K_SPACE:
                    if Player1 > Player2:
                        hist.append('Player 1')
                    elif Player2 > Player1:
                        hist.append('Player 2')
                    else:
                        hist.append('Draw')
                    if len(hist) > 5:
                        hist.pop(0)
                    Player1 = 0
                    Player2 = 0
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
                if event.key == pygame.K_p:
                   state = 1
                   print(state)
            elif event.type == pygame.KEYDOWN and state == 1:
                if event.key == pygame.K_p:
                   state = 0

        if state == 0:
            screen1 = Scoreboard(Player1, Player2, (r,g,b))
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.dividerTextLabel, screen1.dividerTextLabelRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        if state == 1:
            
            screen2 = Result(hist[::-1])
            for i in range(len(hist)):
                screen.blit(screen2.TextLabel[i], screen2.TextRect[i])

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
