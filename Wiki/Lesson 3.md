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

[Sample Code](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L3/main.py)

[Replit Code](https://replit.com/@tlcDataScience/L3-DigitalScoreboard#)

## 4. Enhancement

As a user, I want to be able change the background color of the scoreboard by pressing the following keys:

- "U" key to increase the value of red color.
- "J" key to decrease the value of red color.
- "I" key to increase the value of green color.
- "K" key to decrease the value of green color.
- "O" key to increase the value of blue color.
- "L" key to decrease the value of blue color.

_When the student has additional time_

[Replit Code](https://replit.com/@tlcDataScience/L3-DigitalScoreboard-Enhanced#main.py)
