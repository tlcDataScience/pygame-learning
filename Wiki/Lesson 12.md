# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# 1. Objective

- Development Strategy
- Creating a project

# 2. User Requirements

## 2.1 User Stories

| User Story                                                                                                                                | Acceptance Criteria                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1. As a player, I want to be able to move the snake up, down, left, and right by using the ASWD keys so that I can control its movements. | The snake's body should follow the head, creating a trail behind it. |
| 2. As a player, I want the snake to grow longer each time it eats a bug so that it becomes more challenging to navigate around obstacles. | When the snake eats a bug, its length should increase by one.        |
| 3. As a player, I want to see bugs randomly appear on the screen so that I can move the snake to eat them.                                | Bugs should appear randomly on the game board.                       |
| 4. As a player, I want to be able to see the current score (number of bugs eaten) on the screen so that I can keep track of my progress.  | The score should increase by one each time the snake eats a bug      |

## 2.2 Personas

### 2.2.1 Persona 1: Casual Gamer

**Name:** Sarah

**Age:** 28

**Occupation:** Marketing Executive

**Behavior:** Sarah enjoys playing casual games on her phone during her commute to work. She likes games that are easy to understand and don't require a lot of time to play. She likes to challenge herself by trying to beat her own high score.

**Goals:** Sarah wants to play a game that is easy to pick up and doesn't require a lot of time commitment. She wants to feel a sense of accomplishment by achieving a high score.

### 2.2.2 Persona 2: Retro Gamer

**Name:** Michael

**Age:** 45

**Occupation:** Software Engineer

**Behavior:** Michael enjoys playing classic games from his childhood. He likes games that are simple to play but difficult to master. He enjoys the nostalgia of playing games that he used to play when he was younger.

**Goals:** Michael wants to play a game that reminds him of the classic games he used to play when he was younger. He wants to feel a sense of nostalgia and relive his childhood memories. He also wants a game that provides a good challenge and requires strategy to win.

# 3. Development Guide

This code is a basic implementation of a snake game using the Pygame library in Python.

The game has a snake object, a bug object, and a screen object. The snake object moves around the screen, and the goal is to eat the bug object to gain points. The screen object displays the score. The game ends when the snake collides with the boundaries of the screen or with its own body.

The snake can be moved by using the ASWD keys, and the 'q' key can be pressed to quit the game. The 'r' key is used for debugging purposes to grow the snake manually.

The bug object is randomly generated on the screen, and when the snake collides with it, it is randomly regenerated in a new location, and the snake grows.

The code uses a while loop to keep running the game until the user presses the 'q' key or the game ends. The clock object controls the frame rate of the game, and the pygame.display.flip() function updates the display.

Overall, this code provides a good foundation for a basic snake game, but it could be improved by adding sound effects, different levels, and obstacles.

## 3.1 Screen

The Pygame screen will be a full-screen window with a black background.

In the center of the screen, there will be a snake object represented by a yellow circle and a randomly placed bug object represented by a green circle.

The snake can be controlled by pressing the 'a', 'd', 'w', and 's' keys on the keyboard, which will move the snake left, right, up, and down respectively. The game will continue until the user presses the 'q' key, at which point the game will close.

The top-left corner of the screen will show a label with the text "bug: X", where X is the number of bugs eaten by the snake during the game.

The label will update in real-time as the user plays the game.

![image](https://user-images.githubusercontent.com/102406967/233605724-4855070e-c9c3-482c-a4df-23f1e8e75c99.png)

## 3.2 Behaviour

| Action    | Outcome       |
| --------- | ------------- |
| Press 'a' | Move Left     |
| Press 's' | Move Down     |
| Press 'w' | Move Up       |
| Press 'd' | Move Down     |
| Press 'p' | Pause         |
| Press 'q' | Exit the game |

In the initial implementation, you could program it to make the snake move every time the key is pressed, without requiring continuous movement.

## 3.3 Concepts

### 3.3.1 Creating the Snake

```python
class Snake:

    def __init__(self):
        self.x_pos = WIDTH // 2
        self.y_pos = HEIGHT // 2
        self.radius = 10
        self.body = [(self.x_pos, self.y_pos)]
        self.length = 2

    def moveLeft(self):
        if self.x_pos > PADDING:
            self.x_pos -= self.radius // 2
            self.body.append((self.x_pos, self.y_pos))

    def moveRight(self):
        if self.x_pos < WIDTH - PADDING:
            self.x_pos += self.radius // 2
            self.body.append((self.x_pos, self.y_pos))

    def moveUp(self):
        if self.y_pos > PADDING:
            self.y_pos -= self.radius // 2
            self.body.append((self.x_pos, self.y_pos))

    def moveDown(self):
        if self.y_pos < HEIGHT - PADDING:
            self.y_pos += self.radius // 2
            self.body.append((self.x_pos, self.y_pos))

    def collide(self):
        self.body.append(self.x_pos, self.y_pos)

    def grow(self):
        if self.length < 20:
            self.length += 2

    def render(self):
        self.clean()
        index = 0
        red = 255 - len(self.body) * 10
        for x, y in self.body:
            if index == len(self.body) - 1:
                pygame.draw.circle(WINDOW, (255, 255, 0), (x, y), self.radius)
            else:
                pygame.draw.circle(WINDOW, (red, 0, 0), (x, y), self.radius)
            index += 1
            red += 10

    def clean(self):
        while len(self.body) > self.length:
            self.body.pop(0)
```

This code defines a Snake class for a Pygame program that represents the behavior of a snake in a game.

The `__init__` method sets the initial position, size, and length of the snake.

The `moveLeft`, `moveRight`, `moveUp`, and `moveDown` methods control the snake's movement in different directions. The snake moves by changing its position by a certain amount, and its body grows longer by adding its new position to its body.

The `collide` method is called when the snake collides with something, and it adds the current position of the snake to its body.

The `grow` method increases the length of the snake if it is less than a certain length.

The `render` method draws the snake's body on the screen, and the clean method removes the oldest part of the body to keep it from getting too long.

In summary, this code creates a simple representation of a snake's behavior in a game, where the player can control the snake's movement and the snake grows longer as it moves.

### 3.3.2 Creating the Bug

```python
import random
class Bug:

    def __init__(self):
        self.x_pos = random.randint(PADDING * 2, WIDTH - PADDING * 2)
        self.y_pos = random.randint(PADDING * 2, HEIGHT - PADDING * 2)
        self.radius = 10

    def render(self):
        pygame.draw.circle(WINDOW, (0, 255, 0), (self.x_pos, self.y_pos),
                           self.radius)

    def randomize(self):
        self.x_pos = random.randint(PADDING * 2, WIDTH - PADDING * 2)
        self.y_pos = random.randint(PADDING * 2, HEIGHT - PADDING * 2)
```

This code defines a class called "Bug" using the Pygame library, which is a popular library used for creating games in Python.

The `__init__` method is used to initialize the instance variables of the class. The Bug class has three instance variables: x_pos, y_pos, and radius. The random.randint() function is used to generate random integers for the x_pos and y_pos variables, which will determine the starting position of the bug on the screen. The radius variable is set to 10.

The `render()` method is used to draw the bug on the screen. The pygame.draw.circle() function is used to draw a circle on the Pygame window. The first parameter, WINDOW, is the window object where the circle will be drawn. The second parameter is a tuple representing the RGB color value of the circle, which in this case is green. The third parameter is a tuple representing the position of the center of the circle, which is determined by the x_pos and y_pos variables. The fourth parameter is the radius of the circle, which is set to 10.

The `randomize()` method is used to randomly change the position of the bug on the screen. It does this by generating new random values for the x_pos and y_pos variables, just like in the **init** method. This method can be called at any time during the game to change the position of the bug.

## 3.4 Code

[Replit Code](https://replit.com/@tlcDataScience/SnakeV1#main.py)

# 4. Enhancement

First Enhancement:

| User Story                                                                                                               | Acceptance Criteria                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want the snake to move continuously so that I can enjoy a seamless and uninterrupted gameplay experience. | When the game starts, the snake should start moving in the direction specified by the player. <br> The snake should continue moving in the specified direction until the player changes the direction or the game ends. |

[Replit Code V2](https://replit.com/@tlcDataScience/SnakeV2#main.py)

Second Enhancement:

| User Story                                                  | Acceptance Criteria                                     |
| ----------------------------------------------------------- | ------------------------------------------------------- |
| As a player, I want the snake to know when it hits the wall | The game should end when the snake collides with a wall |

[Replit Code V3](https://replit.com/@tlcDataScience/SnakeV3#main.py)
