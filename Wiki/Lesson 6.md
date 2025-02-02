# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# Digital Scoreboard with interactive bar

<kbd>
<img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215028184-c1133854-f9f0-48a7-a720-72c4e9b4d79e.png">
</kbd><br>
_Display of Digital Scoreboard when score is 0-0_
<br><br>
<kbd>
<img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215028238-0aaeb6d7-b8a2-4b64-adf8-2941974defc4.png">
</kbd><br>
_Display of Digital Scoreboard when score is 10-4_
<br>

# 1. Objective

- User Requirements
- Development Guide

# 2. User Guide

This is a simple program that implements a scoreboard for two players in a game. It uses the Pygame library for graphics and input handling.

The program initializes some constants such as the width and height of the screen, and the background color. It also defines a Scoreboard class that is used to display the scores for each player, as well as the bar that represents the relative scores of each player.

The main loop of the program updates the scores of the players based on keyboard input, and displays the scoreboard using the Scoreboard class. It also handles quitting the game using the space key.

Overall, the program is a simple example of using Pygame to create a graphical interface for a game or application.

## 2.1 User Stories

| User Story                                               | Acceptance Criteria                                                                                                                                                                                     |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want to increase my score.                | 1. Press the "A" key to increase player 1's score. <br> 2. Press the "S" key to increase player 2's score.                                                                                              |
| As a player, I want to decrease my score.                | 1. Press the "Z" key to decrease player 1's score. <br> 2. Press the "X" key to decrease player 2's score.                                                                                              |
| As a player, I want to reset the scores to zero.         | 1. Press the "R" key to reset the scores of both players to zero.                                                                                                                                       |
| As a player, I want to see my score displayed on screen. | 1. The score of each player should be displayed on the screen. <br> 2. The score of player 1 should be displayed on the left side. <br> 3. The score of player 2 should be displayed on the right side. |
| As a player, I want to exit the game.                    | 1. Press the "SPACE" key to exit the game.                                                                                                                                                              |
|                                                          |

## 2.2 Personas

### 2.2.1 Persona 1: Scorekeeper Sam

**Background:** Sam is a volunteer scorekeeper who helps out at local basketball games. He is responsible for keeping track of the score and updating the scoreboard during the game. Sam wants a digital scoreboard that is easy to operate and can be updated quickly during the game.

**Goals:** Sam wants a digital scoreboard that is easy to operate and can be updated quickly during the game. He wants to be able to update the score for both teams with just a few button presses and display the current score for the audience to see.

**Challenges:** Sam has limited experience with technology and wants a scoreboard that is easy to use and does not require a lot of technical expertise to operate. He also wants a scoreboard that is reliable and can withstand the rigors of a basketball game.

# 3. Developer Guide

## 3.1 Description

This Python code is emulate a digital scoreboard for 2 players. User will be able to keep track of the 2 players by entering the input via the keyboard buttons. User should be able to have a visual cue on the scoreboard. This visual cue is a ratio between the 2 players score.

## 3.2 Screen

This screen will be a basic display of the respective scores of the 2 players with an interactive bar that moves based on the scores of the players. Player 1 score will be shown on the left and Player 2 score will be shown on the right. The interactive bar will be shown in the middle.

## 3.3 Scenario

Scores are not allowed to be negative in this version. Scores can go up till 20.

## 3.4 Behaviour

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

| Action           | Outcome                                     |
| ---------------- | ------------------------------------------- |
| Press 'a'        | Increase the score of Player 1 by 1         |
| Press 's'        | Increase the score of Player 2 by 1         |
| Press 'z'        | Decrease the score of Player 1 by 1         |
| Press 'x'        | Decrease the score of Player 2 by 1         |
| Press 'r'        | Reset both Player 1 and Player 2 score to 0 |
| Press 'Spacebar' | Exit the Scoreboard                         |

# 3.5 Full Code

```python
import pygame

# Initialize Pygame
pygame.init()

# -------------------------------
# Window Settings
# -------------------------------
WIDTH = 500            # Window width in pixels
HEIGHT = 300           # Window height in pixels
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Scoreboard - Raw")

# -------------------------------
# Define Colors
# -------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# -------------------------------
# Score Limits and Initial Scores
# -------------------------------
MAX_SCORE = 20
player1 = 0
player2 = 0

# -------------------------------
# Helper Function
# -------------------------------
def clamp(value, min_val, max_val):
    """Ensure the value stays between min_val and max_val."""
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    else:
        return value

# -------------------------------
# Scoreboard Class for Raw Functionality
# -------------------------------
class Scoreboard:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Set up a font using the default freesansbold.ttf at size 32
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
        # Row 1: Title ("Scoreboard") centered at the top
        self.titleSurface = self.font.render("Scoreboard", True, BLACK)
        self.titleRect = self.titleSurface.get_rect(center=(WIDTH // 2, 30))
        
        # Row 2: Player Labels
        self.label1Surface = self.font.render("Player 1", True, BLACK)
        self.label1Rect = self.label1Surface.get_rect(center=(int(WIDTH * 0.25), 60))
        
        self.label2Surface = self.font.render("Player 2", True, BLACK)
        self.label2Rect = self.label2Surface.get_rect(center=(int(WIDTH * 0.75), 60))
        
        # Row 3: Score Texts (these will be updated every frame)
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(center=(int(WIDTH * 0.25), 120))
        
        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(center=(int(WIDTH * 0.75), 120))
        
        # Row 3: Interactive Bar (a stacked bar) will be drawn in the center
        self.bar_width = 150
        self.bar_height = 30
        # The bar is centered horizontally at 50% of WIDTH and vertically at 120 pixels
        self.bar_rect = pygame.Rect(WIDTH // 2 - self.bar_width // 2, 120 - self.bar_height // 2, self.bar_width, self.bar_height)
    
    def draw(self, surface):
        # Draw the title and labels
        surface.blit(self.titleSurface, self.titleRect)
        surface.blit(self.label1Surface, self.label1Rect)
        surface.blit(self.label2Surface, self.label2Rect)
        
        # Update the score texts to match the current scores
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(center=(int(WIDTH * 0.25), 120))
        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(center=(int(WIDTH * 0.75), 120))
        
        # Draw the score texts
        surface.blit(self.score1Surface, self.score1Rect)
        surface.blit(self.score2Surface, self.score2Rect)
        
        # Draw the interactive stacked bar in the center
        # Draw a black border around the bar
        pygame.draw.rect(surface, BLACK, self.bar_rect, 2)
        
        # Calculate the ratio for the stacked bar
        total = self.p1 + self.p2
        if total == 0:
            ratio = 0.5  # Split evenly if both scores are zero
        else:
            ratio = self.p1 / total
        # Calculate widths for each part of the bar
        p1_bar_width = int(ratio * self.bar_width)
        p2_bar_width = self.bar_width - p1_bar_width
        
        # Draw Player 1's portion (red) on the left
        left_bar_rect = pygame.Rect(self.bar_rect.x, self.bar_rect.y, p1_bar_width, self.bar_height)
        pygame.draw.rect(surface, RED, left_bar_rect)
        # Draw Player 2's portion (blue) on the right
        right_bar_rect = pygame.Rect(self.bar_rect.x + p1_bar_width, self.bar_rect.y, p2_bar_width, self.bar_height)
        pygame.draw.rect(surface, BLUE, right_bar_rect)

# -------------------------------
# Main Game Loop for Raw Functionality
# -------------------------------
clock = pygame.time.Clock()
running = True

while running:
    WINDOW.fill(WHITE)  # Fill background with white
    
    # Process user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Quit the program when SPACE is pressed
            if event.key == pygame.K_SPACE:
                running = False
            # Increase Player 1's score with A (up to MAX_SCORE)
            if event.key == pygame.K_a:
                if player1 < MAX_SCORE:
                    player1 += 1
            # Increase Player 2's score with S
            if event.key == pygame.K_s:
                if player2 < MAX_SCORE:
                    player2 += 1
            # Decrease Player 1's score with Z (not below 0)
            if event.key == pygame.K_z:
                if player1 > 0:
                    player1 -= 1
            # Decrease Player 2's score with X
            if event.key == pygame.K_x:
                if player2 > 0:
                    player2 -= 1
            # Reset scores with R
            if event.key == pygame.K_r:
                player1 = 0
                player2 = 0
    
    # Create a Scoreboard object with the current scores
    scoreboard = Scoreboard(player1, player2)
    scoreboard.draw(WINDOW)
    
    # Update the display and control frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

# 4. Enhancement

## Additional Features

- As a user, I want to be able to select different themes (at least 2)
  - not color but different bar graphs. Instead of stacked bar graph, have them as separate.
    "M" key

_When the student has additional time_

```python
import pygame

# Initialize Pygame
pygame.init()

# -------------------------------
# Window Settings
# -------------------------------
WIDTH = 500            # Window width in pixels
HEIGHT = 300           # Window height in pixels
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Scoreboard - Enhanced")

# -------------------------------
# Define Colors
# -------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# -------------------------------
# Score Limits and Initial Scores
# -------------------------------
MAX_SCORE = 20
player1 = 0
player2 = 0

# Theme variable: 0 = Stacked Bar (default), 1 = Separate Bars
theme = 0

# -------------------------------
# Helper Function
# -------------------------------
def clamp(value, min_val, max_val):
    """Ensure the value stays between min_val and max_val."""
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    else:
        return value

# -------------------------------
# Enhanced Scoreboard Class
# -------------------------------
class Scoreboard:
    def __init__(self, p1, p2, theme):
        self.p1 = p1
        self.p2 = p2
        self.theme = theme
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
        # Row 1: Title ("Scoreboard") centered at the top
        self.titleSurface = self.font.render("Scoreboard", True, BLACK)
        self.titleRect = self.titleSurface.get_rect(center=(WIDTH // 2, 30))
        
        # Row 2: Player Labels ("Player 1" on left, "Player 2" on right)
        self.label1Surface = self.font.render("Player 1", True, BLACK)
        self.label1Rect = self.label1Surface.get_rect(center=(int(WIDTH * 0.25), 60))
        
        self.label2Surface = self.font.render("Player 2", True, BLACK)
        self.label2Rect = self.label2Surface.get_rect(center=(int(WIDTH * 0.75), 60))
        
        # Row 3: Score Texts for each player
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(center=(int(WIDTH * 0.25), 120))
        
        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(center=(int(WIDTH * 0.75), 120))
        
        # For Theme 0: Set up interactive stacked bar parameters
        self.bar_width = 150
        self.bar_height = 30
        self.bar_rect = pygame.Rect(WIDTH // 2 - self.bar_width // 2, 120 - self.bar_height // 2, self.bar_width, self.bar_height)
    
    def draw(self, surface):
        # Draw title and player labels
        surface.blit(self.titleSurface, self.titleRect)
        surface.blit(self.label1Surface, self.label1Rect)
        surface.blit(self.label2Surface, self.label2Rect)
        
        # Update and draw score texts
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(center=(int(WIDTH * 0.25), 120))
        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(center=(int(WIDTH * 0.75), 120))
        surface.blit(self.score1Surface, self.score1Rect)
        surface.blit(self.score2Surface, self.score2Rect)
        
        # Draw the interactive bar based on the selected theme
        if self.theme == 0:
            # Theme 0: Stacked Bar in the center
            pygame.draw.rect(surface, BLACK, self.bar_rect, 2)  # Draw border
            total = self.p1 + self.p2
            if total == 0:
                ratio = 0.5
            else:
                ratio = self.p1 / total
            p1_bar_width = int(ratio * self.bar_width)
            p2_bar_width = self.bar_width - p1_bar_width
            left_bar_rect = pygame.Rect(self.bar_rect.x, self.bar_rect.y, p1_bar_width, self.bar_height)
            pygame.draw.rect(surface, RED, left_bar_rect)
            right_bar_rect = pygame.Rect(self.bar_rect.x + p1_bar_width, self.bar_rect.y, p2_bar_width, self.bar_height)
            pygame.draw.rect(surface, BLUE, right_bar_rect)
        else:
            # Theme 1: Separate Bars for each player
            max_bar_width = 150
            bar_height = 30
            # Left side bar for Player 1
            bar_rect1 = pygame.Rect(20, 130, max_bar_width, bar_height)
            p1_width = int((self.p1 / MAX_SCORE) * max_bar_width)
            pygame.draw.rect(surface, BLACK, bar_rect1, 2)
            pygame.draw.rect(surface, RED, (bar_rect1.x, bar_rect1.y, p1_width, bar_height))
            # Right side bar for Player 2
            bar_rect2 = pygame.Rect(WIDTH - 20 - max_bar_width, 130, max_bar_width, bar_height)
            p2_width = int((self.p2 / MAX_SCORE) * max_bar_width)
            pygame.draw.rect(surface, BLACK, bar_rect2, 2)
            pygame.draw.rect(surface, BLUE, (bar_rect2.x, bar_rect2.y, p2_width, bar_height))

# -------------------------------
# Main Game Loop for Enhanced Functionality
# -------------------------------
clock = pygame.time.Clock()
running = True

while running:
    WINDOW.fill(WHITE)  # Fill background with white
    
    # Process events (keyboard input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Quit with SPACE
            if event.key == pygame.K_SPACE:
                running = False
            # Increase scores
            if event.key == pygame.K_a:
                if player1 < MAX_SCORE:
                    player1 += 1
            if event.key == pygame.K_s:
                if player2 < MAX_SCORE:
                    player2 += 1
            # Decrease scores
            if event.key == pygame.K_z:
                if player1 > 0:
                    player1 -= 1
            if event.key == pygame.K_x:
                if player2 > 0:
                    player2 -= 1
            # Reset scores with R
            if event.key == pygame.K_r:
                player1 = 0
                player2 = 0
            # Toggle bar theme with M
            if event.key == pygame.K_m:
                theme = 1 - theme  # Switches between 0 and 1
    
    # Create an enhanced Scoreboard object with current scores and theme
    scoreboard = Scoreboard(player1, player2, theme)
    scoreboard.draw(WINDOW)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```
