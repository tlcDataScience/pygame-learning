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

[Replit Code](https://replit.com/@tlcDataScience/L6-InteractiveDigitalScoreboard)

# 4. Enhancement

## Additional Features

- As a user, I want to be able to select different themes (at least 2)
  - not color but different bar graphs. Instead of stacked bar graph, have them as separate.
    "M" key

_When the student has additional time_

[Replit Code](https://replit.com/@tlcDataScience/L6-InteractiveDigitalScoreboard-Enhance#main.py)
