# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# Digital Scoreboard with an interactive Bar and Avatar

<kbd> <img width="493" alt="image" src="https://user-images.githubusercontent.com/102406967/215033820-0b2cd348-df18-4cbb-98d0-5bf9d56df0d9.png"> </kbd><br>
Display of Digital Scoreboard when score is 10-4

# 1. Objective

- User Requirements
- Development Guide

# 2. User Requirements

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

# 3. Development Guide

## 3.1 Screen

This screen will be a display of the respective scores of the 2 players with a power bar in the middle. Player 1 score will be shown on the left and Player 2 score will be shown on the right. Scores are not allowed to be negative in this version. For each player, there will be an avatar assigned to each player. Avatar is shown on top of the player.

Player 1 will be represented in Red; Player 2 will be represented in Blue

## 3.2 Scenario

If Player 1 is 0 and Player 2 is 0, the power bar will be White.  
If Player 1 is 0 and Player 2 is not 0, the power bar will be Blue.  
If Player 2 is 0 and Player 1 is not 0, the power bar will be Red.

| Player 1 Score | Player 2 Score | Power Bar |
| :------------: | :------------: | :-------: |
|       0        |       0        |   White   |
|       0        |       5        |   Blue    |
|       5        |       0        |    Red    |

## 3.3 Instruction

| Action           | Outcome                                     |
| ---------------- | ------------------------------------------- |
| Press 'a'        | Increase the score of Player 1 by 1         |
| Press 's'        | Increase the score of Player 2 by 1         |
| Press 'z'        | Decrease the score of Player 1 by 1         |
| Press 'x'        | Decrease the score of Player 2 by 1         |
| Press 'r'        | Reset both Player 1 and Player 2 score to 0 |
| Press 'Spacebar' | Exit the Scoreboard                         |

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

# 3.5 Full Code

[Replit Code](https://replit.com/@tlcDataScience/L9-AvatarDigitalScoreboard#main.py)

# 4. Enhancement

## Additional Features

- As a user, I want to pre-select the avatars first
- As a user, I want to show the winner after computing the score

_When the student has additional time_

| Action           | Outcome                                     |
| ---------------- | ------------------------------------------- |
| Press 'a'        | Increase the score of Player 1 by 1         |
| Press 's'        | Increase the score of Player 2 by 1         |
| Press 'z'        | Decrease the score of Player 1 by 1         |
| Press 'x'        | Decrease the score of Player 2 by 1         |
| Press 'r'        | Reset both Player 1 and Player 2 score to 0 |
| Press 'Spacebar' | Exit the Scoreboard                         |

[First Feature](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L9/bonus_1.py)
