import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)

# Path to Image
player1_avatar = 'Cute Cat.png'
player2_avatar = 'Gamer Girl.png'

class Menu:
    def __init__(self, label, img) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # LOADING AVATAR
        # SELECTION
        self.playerLabel = label
        self.playerTextLabel = self.font.render(str(self.playerLabel), True, (0,0,0), (255,255,255))
        self.playerTextRect = self.playerTextLabel.get_rect(center=(WIDTH//2, 200))

        picture1 = pygame.image.load(img)
        self.image1 = pygame.transform.scale(picture1, (100, 100))
        self.imageRect1 = self.image1.get_rect(center=(WIDTH//2, 125))

class Scoreboard:
    def __init__(self, screen, p1, Player1_img, p2,Player2_img) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard 1
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # LOADING AVATAR

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0,0,0), (255,255,255))
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(100, 200))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(100, 250))

        picture1 = pygame.image.load(Player1_img)
        self.image1 = pygame.transform.scale(picture1, (100, 100))
        self.imageRect1 = self.image1.get_rect(center=(100, 125))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0), (255,255,255))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-100,200))
        self.playerTwoScore = p2

        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-100, 250))

        picture2 = pygame.image.load(Player2_img)
        self.image2 = pygame.transform.scale(picture2, (100, 100))
        self.imageRect2 = self.image1.get_rect(center=(WIDTH-100, 125))

        # Bar
        max_length = WIDTH//3

        y_pos = HEIGHT*4//5
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
            pygame.draw.rect(screen,(0,0,255),( (max_length, y_pos) ,(int(max_length),20) )) # Fill
        if p1 != 0:
            pygame.draw.rect(screen,(255,0,0),( (max_length,y_pos) ,(int(fill),20) )) # Fill
        pygame.draw.rect(screen,(0,0,0),( (max_length, y_pos),(max_length, 20) ),4) # Border

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

    ptr = 0
    choices = [player1_avatar, player2_avatar]

    image_map = {
        'player1': None,
        'player2': None
    }

    image_map_keys = list(image_map.keys())
    image_map_keys_index = image_map_keys[0]

    while run:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if state == 0:
                    if event.key == pygame.K_x:
                        ptr = (ptr + 1) % 2
                    if event.key == pygame.K_p:
                        image_map[image_map_keys_index] = choices[ptr]
                        image_map_keys.remove(image_map_keys_index)
                        if len(image_map_keys) != 0:
                            image_map_keys_index = image_map_keys[0]
                        else:
                            state = 1
                elif state == 1:
                    if event.key == pygame.K_a:
                        Player1 += 1
                    elif event.key == pygame.K_s:
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
                if event.key == pygame.K_q:
                    run = False

        if state == 0:
            screen0 = Menu(image_map_keys_index, choices[ptr])
            screen.blit(screen0.playerTextLabel, screen0.playerTextRect)
            screen.blit(screen0.playerTextLabel, screen0.playerTextRect)
            screen.blit(screen0.image1, screen0.imageRect1)

        elif state == 1:
            screen1 = Scoreboard(screen, Player1, image_map['player1'], Player2, image_map['player2'])
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.image1, screen1.imageRect1)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)
            screen.blit(screen1.image2, screen1.imageRect2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()