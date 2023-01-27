import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)

class Scoreboard:
    def __init__(self, screen, p1, p2, type) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard 1
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0,0,0), (255,255,255))
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(100, 125))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(100, 225))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0), (255,255,255))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-100,125))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-100, 225))


        if type == 'BAR 1':
            # Bar
            max_length = WIDTH//3
            if not (p1 == 0 and p2 == 0):
                if p1 == 0:
                    fill = 0
                elif p2 == 0:
                    fill = max_length
                else:
                    percentage = p1 / (p1+p2) * 100
                    total = 100/percentage 
                    fill = max_length/total
            else:
                fill = 0
            
            if p2 != 0:
                pygame.draw.rect(screen,(0,0,255),( (max_length,HEIGHT*2//3) ,(int(max_length),20) )) # Fill
            if p1 != 0:
                pygame.draw.rect(screen,(255,0,0),( (max_length,HEIGHT*2//3) ,(int(fill),20) )) # Fill
            pygame.draw.rect(screen,(0,0,0),( (max_length,HEIGHT*2//3),(max_length, 20) ),4) # Border
        
        elif type == 'BAR 2':
            # Bar
            max_length = WIDTH//3
            
            try:
                percentage = p1 / (p1+p2) * 100
                total_p1 = 100/percentage 
                fill_p1 = max_length/total_p1
            except:
                fill_p1 = 0

            try:
                percentage = p2 / (p1+p2) * 100
                total_p2 = 100/percentage 
                fill_p2 = max_length/total_p2
            except:
                fill_p2 = 0

            if p1 != 0:
                pygame.draw.rect(screen,(255,0,0),( (max_length,HEIGHT*2//3+15) ,(int(fill_p1),20) )) # Fill
            if p2 != 0:
                pygame.draw.rect(screen,(0,0,255),( (max_length,HEIGHT*2//3-15) ,(int(fill_p2),20) )) # Fill

            pygame.draw.rect(screen,(0,0,0),( (max_length,HEIGHT*2//3-15),(max_length, 20) ),4) # Border
            pygame.draw.rect(screen,(0,0,0),( (max_length,HEIGHT*2//3+15),(max_length, 20) ),4) # Border                

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Player1 = 0
    Player2 = 0
    state = 0
    run = True
    while run:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
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
                elif event.key == pygame.K_m:
                    state = (state + 1) % 2
                elif event.key == pygame.K_SPACE:
                    run = False

        if state == 0:
            screen1 = Scoreboard(screen, Player1, Player2, 'BAR 1')
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        elif state == 1:
            screen1 = Scoreboard(screen, Player1, Player2, 'BAR 2')
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()