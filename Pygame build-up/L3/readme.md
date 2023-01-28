# Digital Scoreboard

<kbd> <img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215045430-322b4c38-7afe-4631-af30-f2508b21dde7.png"> </kbd> <br>
Display of Digital Scoreboard when score is 0-0
<br><br>
<kbd> <img width="500" alt="image" src="https://user-images.githubusercontent.com/102406967/215045605-250aa654-bb8f-4922-8eb5-bfeb2c609e16.png"> </kbd> <br>
Display of Digital Scoreboard when score is 14-4

# Objective

- Development Strategy:
- Digital Scoreboard - only text

# User Guide

## Description

This Python code is emulate a digital scoreboard for 2 players. User will be able to keep track of the 2 players by entering the input via the keyboard buttons.

## Screen

This screen will be a basic display of the respective scores of the 2 players. Player 1 score will be shown on the left and Player 2 score will be shown on the right.

### Scenario

Scores are not allowed to be negative in this version. Scores can go up till 20.

## Instruction

| Action           | Outcome                                     |
| ---------------- | ------------------------------------------- |
| Press 'a'        | Increase the score of Player 1 by 1         |
| Press 's'        | Increase the score of Player 2 by 1         |
| Press 'z'        | Decrease the score of Player 1 by 1         |
| Press 'x'        | Decrease the score of Player 2 by 1         |
| Press 'r'        | Reset both Player 1 and Player 2 score to 0 |
| Press 'Spacebar' | Exit the Scoreboard                         |

# Developer Guide

## Description

This Python code is emulate a digital scoreboard for 2 players. User will be able to keep track of the 2 players by entering the input via the keyboard buttons.

## Screen

This screen will be a basic display of the respective scores of the 2 players. Player 1 score will be shown on the left and Player 2 score will be shown on the right.

### Scenario

Scores are not allowed to be negative in this version. Scores can go up till 20.

## Behaviour

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

# Full Code

[Sample Code](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L3%20-%20Digital%20Scoreboard/main.py)

# Enhancement

## Additional Features

- As a user, I want to be able to select different themes (at least 3) and able to rotate
- As a user, I want to display past winnings

_When the student has additional time_

[First Feature](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L3%20-%20Digital%20Scoreboard/bonus_1.py)

[Second Feature](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L3%20-%20Digital%20Scoreboard/bonus_2.py)
