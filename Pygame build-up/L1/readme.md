# Objective

The objective of this lesson:

- Pygame Basics
- Keyboard Inputs
- Mini Project - Color picker v1

# Setting up the Pygame Window

Let's begin with running a sample code using Python pygame. Copy the code below and run it in your Visual Studio Code.

**Sample Code**

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

# Understanding how the game renders the data for Pygame

Breaking down the sample code that was given, pygame can be easily explained in 3 simple parts.

1. Setting up of the screen
2. Reading of the inputs during the game runtime
3. Looping & updating the screen with the new values

Looking at the explanation of the following lines of code

**Loads in pygame module and initialises a pygame environment**

```Python
import pygame
pygame.init()
```

**Sets up the parameters for the screen and creates a window**

In this instance, we have see the color to white (255, 255, 255) with a window size of 400 x 300 pixels

```Python
# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
```

**Creating a loop to run the pygame**

Within the while loops, we need to continuously listen to pygame.events. We will also need to run refresh pygame display screen.

```Python
while True :
    # Get inputs
    for event in pygame.event.get() :
      pass

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
```

# To force quit the Pygame Window

In order to quit the Pygame program, we will need to go to the terminal & hit CTRL-C. At the moment, we have yet to implement a way to exit the Pygame from the window.

# Changing Screen Size

To change the size of the screen, we can change the dimensions. Try to adjust the values for the WIDTH and HEIGHT

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

# Changing Screen Colour

The background colour of the screen is white is (255, 255, 255). Try following the table and changing the values of the table to see what other colours can be created.

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

# Adding keyboard inputs

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

We can use keyboard controls to change the values of the color of the screen. In the code below, we use variables to define the specific values of the screen r, g, b. Based on the respective keyboard inputs, we will toggle between 0 and 255 for the values of r, g, b. These values are then passed to `BACKGROUND` which holds the background color. `WINDOW.fill(BACKGROUND)` & `pygame.display.update()` then updates the screen to the next colour.

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

# Color Picker - Mini Project

- Changing the color of the screen base on the values of r, g, b through the use of keyboard inputs
- Saving our favourite colors of the color picker by using Lists in Python

[Raw Code](https://raw.githubusercontent.com/tlcDataScience/pygame-learning/main/Pygame%20build-up/L1/bonus_1.py)
