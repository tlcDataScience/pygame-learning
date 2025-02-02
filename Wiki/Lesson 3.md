# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# Digital Scoreboard

<kbd><img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215045430-322b4c38-7afe-4631-af30-f2508b21dde7.png"> </kbd> <br>
_Display of Digital Scoreboard when score is 0-0_
<br><br>
<kbd><img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215045605-250aa654-bb8f-4922-8eb5-bfeb2c609e16.png"> </kbd> <br>
_Display of Digital Scoreboard when score is 14-4_

# 1. Objective

- User Requirements
- Development Guide

# 2. User Requirements

This Python code is emulate a digital scoreboard for 2 players. User will be able to keep track of the 2 players by entering the input via the keyboard buttons.

This screen will be a basic display of the respective scores of the 2 players. Player 1 score will be shown on the left and Player 2 score will be shown on the right.

## 2.1 User Stories

| As a user, I want to...                      | So that I can...           |
| -------------------------------------------- | -------------------------- |
| Keep score for two players                   | Keep track of their scores |
| Add points for Player 1 by pressing 'a'      | Increase Player 1's score  |
| Add points for Player 2 by pressing 's'      | Increase Player 2's score  |
| Subtract points for Player 1 by pressing 'z' | Decrease Player 1's score  |
| Subtract points for Player 2 by pressing 'x' | Decrease Player 2's score  |
| Reset both scores by pressing 'r'            | Reset both scores to zero  |
| Quit the program by pressing 'SPACE'         | Exit the program           |

## 2.2 Personas

### 2.2.1 Persona 1: Coach Charlie

**Background:** Charlie is a high school basketball coach who has been coaching for over 10 years. He is passionate about basketball and wants his team to be the best. Charlie is responsible for keeping track of the scores during games and wants an easy-to-use digital scoreboard that he can operate on his own.

**Goals:** Charlie wants a digital scoreboard that is easy to use and can be operated by him during games. He wants to be able to quickly update the scores for both teams and display the current score for the audience to see.

**Challenges:** Charlie has limited experience with technology and wants a scoreboard that is easy to use and does not require a lot of technical expertise to operate. He also wants a scoreboard that is reliable and can withstand the rigors of a basketball game.

### 2.2.2 Persona 2: Spectator Sarah

**Background:**Sarah is a basketball fan who loves to watch her local high school team play. She attends all the games and enjoys keeping track of the score. Sarah wants to be able to easily see the score during the game without having to strain her eyes to read a small scoreboard.

**Goals:** Sarah wants a digital scoreboard that is easy to read and clearly displays the score for both teams. She wants to be able to quickly glance at the scoreboard to see the score without having to take her eyes off the game.

**Challenges:** Sarah has limited experience with technology and wants a scoreboard that is easy to read and does not require a lot of technical expertise to understand. She also wants a scoreboard that is visible from all angles of the court and does not obstruct her view of the game.

### 2.2.3 Persona 3: Scorekeeper Sam

**Background:** Sam is a volunteer scorekeeper who helps out at local basketball games. He is responsible for keeping track of the score and updating the scoreboard during the game. Sam wants a digital scoreboard that is easy to operate and can be updated quickly during the game.

**Goals:** Sam wants a digital scoreboard that is easy to operate and can be updated quickly during the game. He wants to be able to update the score for both teams with just a few button presses and display the current score for the audience to see.

**Challenges:** Sam has limited experience with technology and wants a scoreboard that is easy to use and does not require a lot of technical expertise to operate. He also wants a scoreboard that is reliable and can withstand the rigors of a basketball game.

# 3. Development Guide

Scores are not allowed to be negative in this version. Scores can go up till 20.

| Action           | Outcome                                     |
| :--------------- | :------------------------------------------ |
| Press 'a'        | Increase the score of Player 1 by 1         |
| Press 's'        | Increase the score of Player 2 by 1         |
| Press 'z'        | Decrease the score of Player 1 by 1         |
| Press 'x'        | Decrease the score of Player 2 by 1         |
| Press 'r'        | Reset both Player 1 and Player 2 score to 0 |
| Press 'Spacebar' | Exit the Scoreboard                         |

This Python code is emulate a digital scoreboard for 2 players. User will be able to keep track of the 2 players by entering the input via the keyboard buttons.

This screen will be a basic display of the respective scores of the 2 players. Player 1 score will be shown on the left and Player 2 score will be shown on the right.

Scores are not allowed to be negative in this version. Scores can go up till 20.

## 3.1 Sample Code

For the keyboard inputs, the following code can be referenced while building your Pygame Code.

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and state == 0:
        if event.key == pygame.K_a:
            if Player1 < 20: Player1 += 1
        elif event.key == pygame.K_s:
            if Player2 < 20: Player2 += 1
        elif event.key == pygame.K_z:
            if Player1 != 0: Player1 -= 1
        elif event.key == pygame.K_x:
            if Player2 != 0: Player2 -= 1
        elif event.key == pygame.K_r:
            Player1 = 0
            Player2 = 0
        elif event.key == pygame.K_SPACE:
            run = False
```

## 3.2 Full Code

```python
import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)

class Scoreboard:
    def __init__(self, p1, p2) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard
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

        # LINE
        self.dividerLabel = "|"
        self.dividerTextLabel = self.font1.render(str(self.dividerLabel), True, (0,0,0), (255,255,255))
        self.dividerTextLabelRect = self.dividerTextLabel.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0), (255,255,255))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-100,125))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-100, 225))

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
            if event.type == pygame.KEYDOWN and state == 0:
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
                elif event.key == pygame.K_SPACE:
                    run = False

        if state == 0:
            screen1 = Scoreboard(Player1, Player2)
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.dividerTextLabel, screen1.dividerTextLabelRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

## 4. Enhancement

As a user, I want to be able change the background color of the scoreboard by pressing the following keys:

- "U" key to increase the value of red color.
- "J" key to decrease the value of red color.
- "I" key to increase the value of green color.
- "K" key to decrease the value of green color.
- "O" key to increase the value of blue color.
- "L" key to decrease the value of blue color.

_When the student has additional time_

```python
import pygame

# -------------------
# Window Setup
# -------------------
WIDTH = 500
HEIGHT = 300

# -------------------
# Score Limits and Initial Background Color
# -------------------
MAX_SCORE = 20
MIN_SCORE = 0

# Initial background color components (starts as white)
bg_r, bg_g, bg_b = 255, 255, 255

# -------------------
# Scoreboard Class
# -------------------
class Scoreboard:
    def __init__(self, p1, p2, bg_color):
        # Fonts for text rendering
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font_big = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard title
        self.title = "Scoreboard"
        self.titleSurface = self.font.render(self.title, True, (0, 0, 0), bg_color)
        self.titleRect = self.titleSurface.get_rect(center=(WIDTH // 2, 45))
        
        # Player 1 label and score
        self.player1Label = "Player 1"
        self.player1LabelSurface = self.font.render(self.player1Label, True, (0, 0, 0), bg_color)
        self.player1LabelRect = self.player1LabelSurface.get_rect(center=(100, 125))
        self.player1Score = p1
        self.player1ScoreSurface = self.font.render(str(self.player1Score), True, (0, 0, 0), bg_color)
        self.player1ScoreRect = self.player1ScoreSurface.get_rect(center=(100, 225))
        
        # Divider between scores
        self.divider = "|"
        self.dividerSurface = self.font_big.render(self.divider, True, (0, 0, 0), bg_color)
        self.dividerRect = self.dividerSurface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        # Player 2 label and score
        self.player2Label = "Player 2"
        self.player2LabelSurface = self.font.render(self.player2Label, True, (0, 0, 0), bg_color)
        self.player2LabelRect = self.player2LabelSurface.get_rect(center=(WIDTH - 100, 125))
        self.player2Score = p2
        self.player2ScoreSurface = self.font.render(str(self.player2Score), True, (0, 0, 0), bg_color)
        self.player2ScoreRect = self.player2ScoreSurface.get_rect(center=(WIDTH - 100, 225))

# -------------------
# Main Function
# -------------------
def main():
    global bg_r, bg_g, bg_b

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Digital Scoreboard")

    # Initialize scores for both players
    player1 = 0
    player2 = 0

    running = True
    while running:
        # Set current background color tuple
        BACKGROUND = (bg_r, bg_g, bg_b)
        screen.fill(BACKGROUND)
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Score updates (only if in "scorekeeping" state)
                if event.key == pygame.K_a:
                    if player1 < MAX_SCORE:
                        player1 += 1
                elif event.key == pygame.K_s:
                    if player2 < MAX_SCORE:
                        player2 += 1
                elif event.key == pygame.K_z:
                    if player1 > MIN_SCORE:
                        player1 -= 1
                elif event.key == pygame.K_x:
                    if player2 > MIN_SCORE:
                        player2 -= 1
                elif event.key == pygame.K_r:
                    player1 = 0
                    player2 = 0
                elif event.key == pygame.K_SPACE:
                    running = False

                # Enhancement: Adjust background color. Keep in mind the screen starts with white (255,255,255), so you can only decrease from there.
                elif event.key == pygame.K_u:  # Increase red
                    bg_r += 5
                    if bg_r > 255: bg_r = 255
                elif event.key == pygame.K_j:  # Decrease red
                    bg_r -= 5
                    if bg_r < 0: bg_r = 0
                elif event.key == pygame.K_i:  # Increase green
                    bg_g += 5
                    if bg_g > 255: bg_g = 255
                elif event.key == pygame.K_k:  # Decrease green
                    bg_g -= 5
                    if bg_g < 0: bg_g = 0
                elif event.key == pygame.K_o:  # Increase blue
                    bg_b += 5
                    if bg_b > 255: bg_b = 255
                elif event.key == pygame.K_l:  # Decrease blue
                    bg_b -= 5
                    if bg_b < 0: bg_b = 0

        # Create a new scoreboard with updated scores and background color
        scoreboard = Scoreboard(player1, player2, BACKGROUND)
        # Blit (draw) all text surfaces onto the screen
        screen.blit(scoreboard.titleSurface, scoreboard.titleRect)
        screen.blit(scoreboard.player1LabelSurface, scoreboard.player1LabelRect)
        screen.blit(scoreboard.player1ScoreSurface, scoreboard.player1ScoreRect)
        screen.blit(scoreboard.dividerSurface, scoreboard.dividerRect)
        screen.blit(scoreboard.player2LabelSurface, scoreboard.player2LabelRect)
        screen.blit(scoreboard.player2ScoreSurface, scoreboard.player2ScoreRect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```

