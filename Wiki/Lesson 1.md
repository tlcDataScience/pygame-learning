# Table of contents

| Content                           | Remark                 |
| --------------------------------- | ---------------------- |
| 1. Objective                      | ---                    |
| 2. What is Pygame & its Features? | ---                    |
| 3. Pygame Basics                  | ---                    |
| 4. Review Questions               | To check understanding |
| 5. Mini Project - Color Picker V1 | Bonus Task             |

# 1. Objective

- Introduction to Pygame and its features
- Pygame setup and creating a window
- Handling keyboard inputs with Pygame
- Mini Project: Color Picker v1

# 2. What is Pygame & its Features?

![image](https://user-images.githubusercontent.com/102406967/224467903-60b5212a-678d-4720-a9bc-5e3b19002fa1.png)

Pygame is a computer program that helps people make video games. It's like having a big box of tools that lets you draw pictures, make sounds, and control what happens in your game. With Pygame, you can create your own characters, make them move around the screen, and make them do cool things like jump, shoot, or talk.

You can also make the game react when you press keys on your keyboard, move your mouse, or touch the screen. Pygame is a fun way to learn about programming and create your own games that you can share with your friends and family!

Pygame comes with a variety of features that make it an excellent choice for game development, including its support for handling graphics, sound, input devices, and network communications. The library provides a set of intuitive functions for creating and manipulating images, playing sounds and music, handling keyboard and mouse events, and connecting to other devices over a network.

One of the key advantages of using Pygame is its ability to integrate with other Python libraries and tools, such as NumPy and SciPy, which allow developers to implement advanced algorithms for data analysis and visualization. Pygame also supports several game development frameworks, such as PyOpenGL and Pyglet, which can be used to create more complex 3D games.

Overall, Pygame is an excellent tool for developing 2D games and multimedia applications in Python, and its user-friendly interface and broad range of features make it an attractive option for both novice and experienced developers.

# 3. Pygame Basics

## 3.1 Setting up the Pygame Window

Let's begin with running a sample code using Python pygame. Copy the code below and run it in your Visual Studio Code.

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

## 3.2 Understanding how the game renders the data for Pygame

Breaking down the sample code that was given, pygame can be easily explained in 3 simple parts.

1. Setting up of the screen
2. Reading of the inputs during the game runtime
3. Looping & updating the screen with the new values

Looking at the explanation of the following lines of code

### Sample Code - loads in pygame module and initialises a pygame environment\*\*

```python
import pygame
pygame.init()
```

### Sample Code - Sets up the parameters for the screen and creates a window\*\*

In this instance, we have see the color to white (255, 255, 255) with a window size of 400 x 300 pixels

```python
# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
```

### Sample Code - Creating a loop to run the pygame\*\*

Within the while loops, we need to continuously listen to pygame.events. We will also need to run refresh pygame display screen.

```python
while True :
    # Get inputs
    for event in pygame.event.get() :
      pass

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
```

## 3.3 To force quit the Pygame Window

In order to quit the Pygame program, we will need to go to the terminal & hit CTRL-C. At the moment, we have yet to implement a way to exit the Pygame from the window.

## 3.4 Changing Screen Size

To change the size of the screen, we can change the dimensions. Try to adjust the values for the WIDTH and HEIGHT

### Sample Code

```python
import pygame

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
WINDOW_WIDTH = 400 ### CHANGE THE WIDTH HERE
WINDOW_HEIGHT = 300 ### CHANGE THE HEIGHT HERE

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

## 3.5 Changing Screen Colour

The screen's background color is currently set to white, which is represented by the RGB values (255, 255, 255). You can experiment with different colors by adjusting the values in the table below.

### Activity

| BACKGROUND      | Colour |
| --------------- | ------ |
| (255, 255, 255) | White  |
| (255, 0, 0)     |        |
| (0, 255, 0)     |        |
| (0, 0, 255)     |        |
| (0, 0, 0)       |        |

_Fill up the table with the respective colours_

```python
import pygame

pygame.init()

# Colours
BACKGROUND = (255, 255, 255) ### Activity - Change the code here

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

## 3.6 Adding keyboard inputs

Now, let's make it interactive by adding keyboard controls. To add keyboard inputs, we need to trigger it through the events.

We can enhance our code by introducing the following. This is allow pygame to detect a key press & which key it is.

`event.type == pygame.KEYDOWN` detects a key press

`event.key == pygame.K_a` detects if the key 'a' is pressed.

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

We can adjust the color of the screen by using keyboard controls. In the code below, we've defined variables for the red (r), green (g), and blue (b) values of the screen color. Depending on the keyboard inputs we receive, we will switch between setting these values to either 0 or 255. We then pass these values to a variable called BACKGROUND, which holds the background color. Finally, we use WINDOW.fill(BACKGROUND) and pygame.display.update() to update the screen to the new color.

```python
import pygame

pygame.init()

r, g, b = 0, 0, 0

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# The main game loop
while True :
    # Get inputs
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


    BACKGROUND = (r, g, b)
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
```

Let's make more improvements. If we want to only update when there are changes and show the new values of r, g, b, we can use boolean to control the state of when to update. It is similar to a flag concept where we now introduce `ChangeDetected` to store the state of when to print out the values of the color of the screen.

```python
import pygame

pygame.init()

r, g, b = 0, 0, 0

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ChangeDetected = False

# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
        ChangeDetected = True
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

    if ChangeDetected:
        ChangeDetected = False
        print(f" (r,g,b) = ({r}, {g}, {b})")
        BACKGROUND = (r, g, b)
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()

```

At this point, we have only achieve switching the color of r, g, b on & off. Colors are a spectrum. There is a range of values for r, g, b and we can slowly increment and decrement it over a scale 0 - 255. Let's try to introduce increment. Take a look at the code.

```python
import pygame

pygame.init()

r, g, b = 0, 0, 0

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ChangeDetected = False

# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
        ChangeDetected = True
        if event.key == pygame.K_a:
            r += 5
            if r > 255:
                r = 255
        if event.key == pygame.K_z:
            r = 0
        if event.key == pygame.K_s:
            g += 5
            if g > 255:
                g = 255
        if event.key == pygame.K_x:
            g = 0
        if event.key == pygame.K_d:
            b += 5
            if b > 255:
                b = 255
        if event.key == pygame.K_c:
            b = 0

    if ChangeDetected:
        ChangeDetected = False
        print(f" (r,g,b) = ({r}, {g}, {b})")
        BACKGROUND = (r, g, b)
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()

```

Now, from the code above, add in the feature to decrement instead of setting the value directly to 0.

By the end of this lesson, we have created a basic colour picker. For the different combination of colors, we can refer to the console for our favourite choice

# 4. Review Questions

## Question 1

Which Pygame function is used to create a new window?

<ol type="a">
  <li>Pygame.create_window()</li>
  <li>Pygame.create_surface()</li>
  <li>Pygame.display.set_mode()</li>
  <li>Pygame.display.create_window()</li>
</ol>

<details>
  <summary>Answer</summary>
  c. Pygame.display.set_mode()
</details>

---

## Question 2

Which arguments are required when creating a new Pygame window?

<ol type="a">
  <li>The window width and height</li>
  <li>The window caption</li>
  <li>The window background color</li>
  <li>Both a and b</li>
</ol>

<details>
  <summary>Answer</summary>
  d. Both a and b
</details>

---

## Question 3

Which argument is used to set the background color of a Pygame window?

<ol type="a">
  <li>A tuple containing RGB values</li>
  <li>A single integer representing the RGB value</li>
  <li>A string representing the color name</li>
  <li>All of the above</li>
</ol>

<details>
  <summary>Answer</summary>
  a. A tuple containing RGB values
</details>

---

## Question 4

Which Pygame module is used to handle events?

<ol type="a">
  <li>Pygame.event</li>
  <li>Pygame.display</li>
  <li>Pygame.sprite</li>
  <li>Pygame.keyboard</li>
</ol>

<details>
  <summary>Answer</summary>
  a. Pygame.event
</details>

---

## Question 5

What does the following Pygame code do?

```python
# The main game loop
while True:
    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ChangeDetected = True
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

    if ChangeDetected:
        ChangeDetected = False
        print(f"(r,g,b) = ({r}, {g}, {b})")
        BACKGROUND = (r, g, b)
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()
```

<ol type="a">
  <li>It creates a game window and fills it with a black background</li>
  <li>It allows the player to move a sprite on the screen</li>
  <li>It changes the background color of the game window based on keyboard input</li>
  <li>It plays music and sound effects in the game</li>
</ol>

<details>
  <summary>Answer</summary>
  c. It changes the background color of the game window based on keyboard input
</details>

# 5. Mini Project - Color Picker V1

- Changing the color of the screen base on the values of r, g, b through the use of keyboard inputs. Starts with black.
- Saving our favourite colors of the color picker by using Lists in Python
- Paste the code below into trinket.io/pygame
- Remember to click on the pygame screen first to ensure the keyboard inputs are controlling the pygame module

```python
import pygame

# Initialize Pygame
pygame.init()

# Print instructions to the console
print("Color Picker V1")
print("Use keys:")
print("  A to increase red, Z to decrease red")
print("  S to increase green, X to decrease green")
print("  D to increase blue, C to decrease blue")
print("  F to save the current color as a favorite")
print("Close the window or press CTRL+C in the console to exit.")

# Starting color values
r, g, b = 0, 0, 0

# List to save favorite colors
favorites = []

# Window setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Color Picker V1")

change_detected = False
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        # Allow the user to close the window
        if event.type == pygame.QUIT:
            running = False
        
        # Check for key presses
        if event.type == pygame.KEYDOWN:
            change_detected = True

            # Increase or decrease Red
            if event.key == pygame.K_a:
                r += 5
                if r > 255:
                    r = 255
            if event.key == pygame.K_z:
                r -= 5
                if r < 0:
                    r = 0

            # Increase or decrease Green
            if event.key == pygame.K_s:
                g += 5
                if g > 255:
                    g = 255
            if event.key == pygame.K_x:
                g -= 5
                if g < 0:
                    g = 0

            # Increase or decrease Blue
            if event.key == pygame.K_d:
                b += 5
                if b > 255:
                    b = 255
            if event.key == pygame.K_c:
                b -= 5
                if b < 0:
                    b = 0

            # Save the current color when F is pressed
            if event.key == pygame.K_f:
                favorites.append((r, g, b))
                print("Favorite colors:", favorites)

    # If any change occurred, update the screen and print the current color
    if change_detected:
        change_detected = False
        current_color = (r, g, b)
        print(f"(r, g, b) = {current_color}")
        WINDOW.fill(current_color)
        pygame.display.update()

pygame.quit()
```

