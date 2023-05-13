# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# 1. Objective

- Development Strategy - Falling Blocks

- Creating a project

# 2. User Requirements

This is a simple game built using Pygame library in Python. The game involves a bar at the bottom of the screen which can be moved left or right using the 'a' and 'd' keys. Drops of yellow ball that fall from the top of the screen randomly and the aim of the game is to catch as many drops as possible with the bar, while avoiding the drops from falling out of the screen. The game keeps track of the score and the number of times the drops fall out of the screen.

## 2.1 User Stories

| User Story                                                                                                  | Acceptance Criteria                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want to control the bar's movement using 'A' & 'D' keys so that I can catch falling objects. | When I press the 'A' & 'D' key, the bar moves to the left as long as it does not exceed the window's left boundary. When I press the right arrow key, the bar moves to the right as long as it does not exceed the window's right boundary. |
| As a player, I want to see the number of successfully caught objects so that I can track my score.          | The game should display a count of successfully caught objects on the screen. The count should increase whenever the bar catches a falling object.                                                                                          |
| As a player, I want to see the number of missed objects so that I can track my progress.                    | The game should display a count of missed objects on the screen. The count should increase whenever a falling object reaches the bottom of the screen without being caught by the bar.                                                      |

## 2.2 Personas

### 2.2.1 Persona 1: Young Kid

**Name:** Tommy

**Age:** 8

**Occupation:** Elementary school student

**Background:**

Tommy is an energetic and curious boy who loves to play games on his iPad. He is always looking for new games to play that are fun and challenging. His parents are supportive of his hobbies and encourage him to play games that will help him develop his hand-eye coordination and critical thinking skills.

**Goals:**

Tommy's goal is to find a game that is both fun and educational. He likes games that challenge him but are not too difficult or frustrating to play. He wants a game that he can play on his own without needing too much help from his parents.

**Challenges:**

Tommy's attention span can be short, so he needs a game that is easy to pick up and put down. He also has limited experience with using a keyboard or mouse, so he needs a game that is easy to control with a touch screen.

# 3. Development Guide

## 3.1 Screen

The screen in this Pygame code is a full-screen window with a black background color. The game interface consists of a blue rectangular bar at the bottom of the screen, representing the player's paddle, which can be moved left or right using the 'A' and 'D' keys.

## 3.2 Behaviour

The objective of the game is to catch yellow drops that fall from the top of the screen using the paddle, while avoiding drops that fall outside of the paddle's range. The drops are randomly generated with a random speed, and their sizes and positions vary as well. The score and fail counters are displayed at the top of the screen, and they are updated in real-time as the player catches or misses the drops.

## 3.3 Concepts

### 3.1 Creating a yellow drop

you can use a class to create a falling yellow drop in Pygame. One approach could be to create a Drop class that represents the drop and handles its movement, position, and appearance.

Here's an example implementation:

```python
import pygame
import random

# Define colors
YELLOW = (255, 255, 0)

class Drop:
    def __init__(self, screen_width):
        # Set drop initial position to a random x coordinate at the top of the screen
        self.x = random.randint(0, screen_width)
        self.y = 0

        # Set drop size and speed
        self.size = random.randint(10, 20)
        self.speed = random.randint(3, 6)

    def move(self):
        # Move drop downwards
        self.y += self.speed

    def draw(self, screen):
        # Draw drop on screen
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.size)

    def is_off_screen(self, screen_height):
        # Check if drop has fallen off the screen
        return self.y > screen_height
```

In this implementation, the Drop class is initialized with the screen_width parameter to determine the initial position of the drop. The `move()` method updates the position of the drop by moving it downwards by its current speed. The `draw()` method is responsible for rendering the drop on the screen using Pygame's draw.circle() function. Finally, the is_off_screen() method checks whether the drop has fallen off the bottom of the screen.

To use this class, you would create instances of the Drop class and call its methods in the main game loop. For example:

```python
# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a list to store drops
drops = []

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add a new drop every 10 frames
    if pygame.time.get_ticks() % 10 == 0:
        drops.append(Drop(screen_width))

    # Move drops and remove drops that have fallen off screen
    for drop in drops:
        drop.move()
        if drop.is_off_screen(screen_height):
            drops.remove(drop)

    # Draw drops on screen
    screen.fill((0, 0, 0))
    for drop in drops:
        drop.draw(screen)
    pygame.display.flip()
```

In this example, a list called drops is created to store instances of the Drop class. Every 10 frames, a new drop is added to the list using the `append()` method.
The `move()` and `is_off_screen()` methods of each drop in the list are called in the main game loop to update their position and check whether they have fallen off the screen.

Finally, the `draw()` method of each drop is called to render them on the screen using Pygame's `fill()` and `display.flip()` functions.

### 3.2 Creating a Blue catcher

```python
import pygame

class Bar:
    def __init__(self, screen_width, screen_height):
        self.width = 100
        self.height = 10
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - 50
        self.color = (0, 0, 255)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def move(self, direction):
        if direction == "left":
            self.x -= 10
        elif direction == "right":
            self.x += 10

        # keep the bar within the game window
        if self.x < 0:
            self.x = 0
        elif self.x > 400:
            self.x = 400

```

In this example, we define the Bar class, which takes in the width and height of the game screen as arguments. We set the initial position of the bar to be centered horizontally and near the bottom of the screen. We also set the color of the bar to blue.

In the **init** method, we create a pygame.Surface object that represents the bar. We set the dimensions of this surface to be the same as the width and height of the bar. We then fill this surface with the blue color.

The draw method is responsible for drawing the bar onto the game screen. We use the blit method of the game screen to draw the bar surface onto the screen at the position specified by self.x and self.y.

The move method is responsible for moving the bar horizontally in response to keyboard events. We take in a direction argument that specifies whether the bar should move left or right. We then adjust the self.x position of the bar accordingly. We also make sure to keep the bar within the boundaries of the game window.

We can create an instance of the Bar class in our game loop and call its draw and move methods as needed. By handling keyboard events, we can allow the player to control the movement of the bar and catch the falling yellow drops.

## 3.4 Code

[Replit Code V1](https://replit.com/@tlcDataScience/FallingBlockV1#main.py)

# 4. Enhancement

[Replit Code V2](https://replit.com/@tlcDataScience/FallingBlockV2#main.py)

[Replit Code V3](https://replit.com/@tlcDataScience/FallingBlockV3#main.py)
