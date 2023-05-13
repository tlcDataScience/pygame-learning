# Table of contents

| Content             | Remark                 |
| ------------------- | ---------------------- |
| 1. Objective        | ---                    |
| 2. Recap            | ---                    |
| 3. Lesson           | ---                    |
| 4. Review Questions | To check understanding |
| 5. Mini Project     | Bonus Task             |

# 1. Objective

- Transition of Screens

# 2. Recap on Pygame Basics

# 2.1 Setting up the Pygame Window

Let's recap by running a sample code using Python pygame in the previous lesson.

### Sample Code

```python
import pygame

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      pass

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
```

# 2.2 Mini Refresher - Taken from Lesson 2

```python
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            r = 255
          if event.key == pygame.K_z:
            r = 0
          if event.key == pygame.K_s:
            g = 255
          if event.key == pygame.K_x:
            g = 0
          if event.key == pygame.K_d:
            b = 255
          if event.key == pygame.K_c:
            b = 0
```

To check your understanding of Pygame mechanics, here are some questions

- What happens when a KEYDOWN event is detected??
- What is the purpose of setting "r" to 255?
- How is "r" set to 0?
- What happens when the pygame.K_z constant is detected?
- How does setting "g" to 255 affect the program?

# 3. Lesson

## 3.1 Transition of Screens using Functions

Using Functional Programming

Here is a basic example of how you can use Pygame to switch between screens:

1. Import the Pygame library

```python
import pygame
```

2. Initialize the Pygame library and create a display window

```python
pygame.init()
screen = pygame.display.set_mode((800, 600))
```

3. Define a function for each screen you want to create. Each function should include all the necessary Pygame code to display that screen. For example:

```python
def menu_screen():
    # Code for displaying the menu screen goes here
    pass

def game_screen():
    # Code for displaying the game screen goes here
    pass

def game_over_screen():
    # Code for displaying the game over screen goes here
    pass
```

4. Create a variable to keep track of which screen is currently being displayed. For example:

```python
current_screen = "menu"
```

5. In the main game loop, use an if-elif statement to call the appropriate function for the current screen. For example:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_screen == "menu":
        menu_screen()
    elif current_screen == "game":
        game_screen()
    elif current_screen == "game_over":
        game_over_screen()

    pygame.display.update()
```

6. To switch between screens, simply change the value of the current_screen variable. For example:

```python
if current_screen == "menu" and user_clicks_start_button:
    current_screen = "game"

if player_loses_game:
    current_screen = "game_over"
```

7. Don't forget to quit Pygame when the game loop ends

```python
pygame.quit()
```

## 3.2 Transition of Screens using Classes

Here is a basic example of how you can use Pygame to switch between screens:

1. Import the Pygame library

```python
import pygame
```

2. Initialize the Pygame library and create a display window

```python
pygame.init()
screen = pygame.display.set_mode((800, 600))
```

3. Define a function for each screen you want to create. Each function should include all the necessary Pygame code to display that screen. For example:

```
def menu_screen():
    # Code for displaying the menu screen goes here
    pass

def game_screen():
    # Code for displaying the game screen goes here
    pass

def game_over_screen():
    # Code for displaying the game over screen goes here
    pass
```

4. Create a variable to keep track of which screen is currently being displayed. For example:

```python
current_screen = "menu"
```

5. In the main game loop, use an if-elif statement to call the appropriate function for the current screen. For example:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_screen == "menu":
        menu_screen()
    elif current_screen == "game":
        game_screen()
    elif current_screen == "game_over":
        game_over_screen()

    pygame.display.update()
```

6. To switch between screens, simply change the value of the current_screen variable. For example:

```python
if current_screen == "menu" and user_clicks_start_button:
    current_screen = "game"

if player_loses_game:
    current_screen = "game_over"
```

7. Don't forget to quit Pygame when the game loop ends

```
pygame.quit()
```

This basic code should give you a good starting point for creating a Pygame application with multiple screens. You can then add more functionality, graphics, and animations to each screen as needed.

# 4. Review Questions

## Question 1

What is the purpose of using transition states in a Pygame game using OOP?

<ol type="a">
<li>To manage and switch between different game states
<li>To handle user input and events
<li>To draw graphics and display images
<li>All of the above
</ol>
<details>
  <summary>Answer</summary> A. To manage and switch between different game states
Explanation: Transition states are used to manage and switch between different game states in Pygame games using OOP. This allows for a more organized and modular game design, where different parts of the game can be handled separately.
</details>

---

## Question 2

In a Pygame game using OOP, how can you define a new transition state?

<ol type="a">
<li>By creating a new class that inherits from the pygame.sprite.Sprite class
<li>By creating a new function that handles the transition state
<li>By adding a new object to the Pygame event queue
<li>By modifying the pygame.display.set_mode() function
</ol>
<details>
  <summary>Answer</summary> A. By creating a new class that inherits from the pygame.sprite.Sprite class
Explanation: In Pygame games using OOP, you can define a new transition state by creating a new class that inherits from the pygame.sprite.Sprite class. This class can then implement its own update() and draw() methods to handle the transition state.
</details>

---

## Question 3

How can you switch between different transition states in a Pygame game using OOP?

<ol type="a">
<li>By modifying the current_state variable
<li>By calling the set_state() method of the pygame.sprite.Sprite class
<li>By adding a new object to the Pygame event queue
<li>By modifying the pygame.display.set_mode() function
</ol>
<details>
  <summary>Answer</summary> A. By modifying the current_state variable
Explanation: In Pygame games using OOP, you can switch between different transition states by modifying the current_state variable, which stores the current state of the game. This variable can be updated in response to user input or other events.
</details>

---

## Question 4

What is the purpose of the update() method in a Pygame transition state class?

<ol type="a">
<li>To update the game state based on user input and events
<li>To update the position and movement of game objects
<li>To update the display and draw graphics
<li>All of the above
</ol>
<details>
  <summary>Answer</summary> B. To update the position and movement of game objects
Explanation: The update() method in a Pygame transition state class is typically used to update the position and movement of game objects. This method is called every frame of the game loop to update the state of the game.
</details>

---

## Question 5

What is the purpose of the draw() method in a Pygame transition state class?

<ol type="a">
<li>To update the game state based on user input and events
<li>To update the position and movement of game objects
<li>To update the display and draw graphics
<li>All of the above
</ol>
<details>
  <summary>Answer</summary> C. To update the display and draw graphics
Explanation: The draw() method in a Pygame transition state class is typically used to update the display and draw graphics. This method is called every frame of the game loop to redraw the game window based on the current state of the game.
</details>

# 5. Mini Project - Toggling between different feature

In this project, you will learn how to enhance your game with additional features using Pygame and transition states in an object-oriented programming (OOP) style. The new features you will implement are a scoreboard and a gallery, which can be navigated to using the toggle feature.

Using Pygame, you will create separate classes for the different game states, including the `start screen`, `game screen`, game over screen, `scoreboard screen`, and `gallery screen`.

In addition to the basic game states, you will also create a Scoreboard class and a Gallery class. The Scoreboard class will keep track of the player's score and display it on the screen. The Gallery class will display images or animations related to the game, such as character or background art.

To navigate to the scoreboard or gallery, you will add specific key or button triggers to the game. For example, pressing the "s" key might transition to the scoreboard screen, while pressing the "g" key might transition to the gallery screen. You can use Pygame's built-in functions and classes to handle these elements and enhance the overall gameplay experience.

# 5.1 User Stories

| User Story                                                                                    | Acceptance Criteria                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want to see my score displayed on the screen during the game.                  | 1. The score should be displayed in a visible location on the screen. <br> 2. The score should increase by one point for every successful action. <br> 3. The score should not decrease if the player fails an action.           |
| As a player, I want to be able to access a scoreboard to view my high score.                  | 1. Pressing the "s" key should transition the game to the scoreboard screen. <br> 2. The scoreboard should display the player's high score. <br> 3. The scoreboard should have a button to return to the game.                   |
| As a player, I want to be able to access a gallery to view game-related images or animations. | 1. Pressing the "g" key should transition the game to the gallery screen. <br> 2. The gallery should display a list of images or animations related to the game. <br> 3. The gallery should have a button to return to the game. |

# 5.2 Screens

| Screen            | Description                                                                                                                                              | Class Name         |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Start Screen      | The initial screen that appears when the game is launched. It typically contains a title, instructions, and a button to start the game.                  | `StartScreen`      |
| Game Screen       | The main screen where the game is played. It displays the game objects, such as the player and enemies, and updates in real-time as the game progresses. | `GameScreen`       |
| Game Over Screen  | The screen that appears when the game ends. It typically displays the final score and a button to play again or return to the start screen.              | `GameOverScreen`   |
| Scoreboard Screen | A screen that displays the player's high score and possibly other statistics related to the game.                                                        | `ScoreboardScreen` |
| Gallery Screen    | A screen that displays game-related images or animations, such as character or background art.                                                           | `GalleryScreen`    |

# 5.3 Guide

_Rough Outline_

1. Create a Gallery class that has a method to load the images or animations and a method to draw them on the screen. You can use Pygame's image module to load the images.
2. In the method that loads the images, you can store them in a list or dictionary for easy access. You can also resize or scale the images if needed.
3. In the method that draws the images, you can iterate over the list or dictionary of images and blit them onto the screen surface using Pygame's blit method.
4. Add a key or button trigger to the game that will transition to the gallery screen. You can use Pygame's event module to detect key presses or button clicks. When the trigger is detected, you should change the current state to the gallery state.
5. Modify the update and draw methods in each state class to handle the transitions between states. When the current state is the gallery state, you can call the draw method of the Gallery class to display the images on the screen.
6. Create a Game class that will manage the game loop and the current state. The Game class should have methods to handle events, update the current state, and draw the current state on the screen.
7. Instantiate the Game class and start the game loop. The game loop should handle events, update the current state, and draw the current state on the screen in each iteration.
