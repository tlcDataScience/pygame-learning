# Lesson 4

# 3.6 Moving shapes with keyboard inputs

```python

# Creating shapes

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_w:
                    h -= 10
                if event.key == pygame.K_s:
                    h += 10
                if event.key == pygame.K_a:
                    w -= 10
                if event.key == pygame.K_d:
                    w += 10

        if w < PADDING:
            w = PADDING
        elif w > WINDOW_WIDTH - PADDING:
            w = WINDOW_WIDTH - PADDING

        if h < PADDING:
            h = PADDING
        elif h > WINDOW_HEIGHT - PADDING:
            h = WINDOW_HEIGHT - PADDING

        pygame.draw.circle(WINDOW, BLUE, (w,h), 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


```

# Continous movement

```python
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
            # CONTINUOUS
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                h -= 3
            if keys[pygame.K_s]:
                h += 3
            if keys[pygame.K_a]:
                w -= 3
            if keys[pygame.K_d]:
                w += 3

```

```python

# Creating shapes

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
            # CONTINUOUS
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                h -= 3
            if keys[pygame.K_s]:
                h += 3
            if keys[pygame.K_a]:
                w -= 3
            if keys[pygame.K_d]:
                w += 3

        if w < PADDING:
            w = PADDING
        elif w > WINDOW_WIDTH - PADDING:
            w = WINDOW_WIDTH - PADDING

        if h < PADDING:
            h = PADDING
        elif h > WINDOW_HEIGHT - PADDING:
            h = WINDOW_HEIGHT - PADDING

        pygame.draw.circle(WINDOW, BLUE, (w,h), 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

```

## Question 1:

Which Pygame function can be used to manage moving objects in Pygame?

<ol type="a">
    <li>pygame.animate()</li>  
    <li>pygame.move()</li>
    <li>pygame.sprite()</li>
    <li>pygame.draw()</li>
</ol>

<details>
<summary>Answer</summary>
Answer: b. pygame.move()
</details>

---

## Question 2:

What is collision detection in Pygame?

<ol type="a">
    <li>Checking whether two objects have collided</li>
    <li>Determining the movement speed of an object</li>
    <li>Creating an image in Pygame</li>
    <li>Creating animation in Pygame</li>
</ol>

<details>
<summary>Answer</summary>
Answer: a. Checking whether two objects have collided
</details>

---

## Question 3:

Which Pygame module is used for displaying and managing images?

<ol type="a">
    <li>pygame.image</li>  
    <li>pygame.sprite</li>  
    <li>pygame.display</li>  
    <li>pygame.draw</li>
</ol>

<details>
<summary>Answer</summary>
Answer: a. pygame.image
</details>

---

## Question 4:

What is an animation in Pygame?

<ol type="a">
    <li>A still image displayed on the screen</li>
    <li>A series of still images displayed in a sequence </li>
    <li>A moving image on the screen </li>
    <li>A sound effect played in the game</li>
</ol>

<details>
<summary>Answer</summary>
Answer: b. A series of still images displayed in a sequence
</details>

---

## Question 5

How can you create animation in Pygame?

<ol type="a">
  <li>By creating a single still image and displaying it repeatedly</li> 
  <li>By using Pygame's built-in animation function</li>
  <li>By creating a series of still images and displaying them in a sequence</li>
  <li>By using Pygame's built-in collision detection function</li>
</ol>

<details>
<summary>Answer</summary>
Answer: c. By creating a series of still images and displaying them in a sequence
</details>

# Lesson 5

# 3.1 Dynamic Bounce

This is a simple pygame script that creates a circle and moves it around the window. The circle changes color when the "x" key is pressed.

The script first imports the necessary libraries: random and pygame. It then sets up some constants for the window size and colors.

In the main function, the script initializes pygame, sets up the window with a white background, and sets up some variables for the circle's position and movement. The script then enters a game loop that will run until the user quits the game by pressing the "q" key.

Inside the game loop, the script checks for inputs from the user. If the "q" key is pressed, the run variable is set to False and the game loop will end. If the "x" key is pressed, the circle's color is changed to a random selection from the available colors.

The script then checks if the circle has hit the edge of the window. If it has, the direction of movement is reversed. The circle's position is then updated based on its movement speed.

Finally, the script draws the circle on the window and updates the display. The game loop runs at 60 frames per second, as set by the clock.tick(60) statement.

Overall, this script is a simple example of using pygame to create graphics and handle user input.

### Sample Code

```python

# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_x:
                    c = random.choice(Selection)
                    Selection = [RED, GREEN, BLUE]
                    Selection.remove(c)

        if w < PADDING or w > WINDOW_WIDTH - PADDING:
            move_w *= -1

        if h < PADDING or h > WINDOW_HEIGHT - PADDING:
            move_h *= -1

        # UPDATE
        w += move_w
        h += move_h

        pygame.draw.circle(WINDOW, c, (w,h), 10)

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

# Color change?

```python


# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_x:
                    c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if w < PADDING or w > WINDOW_WIDTH - PADDING:
            move_w *= -1

        if h < PADDING or h > WINDOW_HEIGHT - PADDING:
            move_h *= -1

        # UPDATE
        w += move_w
        h += move_h

        pygame.draw.circle(WINDOW, c, (w,h), 10)

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

```

Rainbow move

```python

# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if w < PADDING or w > WINDOW_WIDTH - PADDING:
            move_w *= -1

        if h < PADDING or h > WINDOW_HEIGHT - PADDING:
            move_h *= -1

        # UPDATE
        w += move_w
        h += move_h

        pygame.draw.circle(WINDOW, c, (w,h), 10)

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

```

Transition

```python


# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    r,g,b = 100, 100, 100

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        if random.randint(0,1) != 0:
            if r < 255:
                r += 5
        else:
            if r > 0:
                r -= 5

        if random.randint(0,1) != 0:
            if b < 255:
                b += 5
        else:
            if b > 0:
                b -= 5

        if random.randint(0,1) != 0:
            if g < 255:
                g += 5
        else:
            if g > 0:
                g -= 5

        c = (r,g,b)
        print(c)

        if w < PADDING or w > WINDOW_WIDTH - PADDING:
            move_w *= -1

        if h < PADDING or h > WINDOW_HEIGHT - PADDING:
            move_h *= -1

        # UPDATE
        w += move_w
        h += move_h

        pygame.draw.circle(WINDOW, c, (w,h), 10)

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


```

Adding text

```python
# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    label = 'Moving Ball'
    font = pygame.font.Font('freesansbold.ttf', 32)
    TextLabel = font.render(str(label), True, (0,0,0), (255,255,255))
    TextRect = TextLabel.get_rect(center=(WINDOW_WIDTH//2, 45))

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_x:
                    c = random.choice(Selection)
                    Selection = [RED, GREEN, BLUE]
                    Selection.remove(c)

        if w < PADDING or w > WINDOW_WIDTH - PADDING:
            move_w *= -1

        if h < PADDING or h > WINDOW_HEIGHT - PADDING:
            move_h *= -1

        # UPDATE
        w += move_w
        h += move_h

        WINDOW.blit(TextLabel, TextRect)
        pygame.draw.circle(WINDOW, c, (w,h), 10)

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

```

```python

# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3

    label = 'Moving Ball'
    font = pygame.font.Font('freesansbold.ttf', 32)
    TextLabel = font.render(str(label), True, (0,0,0), (255,255,255))
    TextRect = TextLabel.get_rect(center=(WINDOW_WIDTH//2, 45))

    freeze = False

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_x:
                    c = random.choice(Selection)
                    Selection = [RED, GREEN, BLUE]
                    Selection.remove(c)
                if event.key == pygame.K_f:
                    freeze = not(freeze)
        if not freeze:
            if w < PADDING or w > WINDOW_WIDTH - PADDING:
                move_w *= -1

            if h < PADDING or h > WINDOW_HEIGHT - PADDING:
                move_h *= -1

            # UPDATE
            w += move_w
            h += move_h


            WINDOW.blit(TextLabel, TextRect)
            pygame.draw.circle(WINDOW, c, (w,h), 10)

            #pygame.display.update()
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()

```

```python

# Creating shapes
import random
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True
    c = RED
    Selection = [GREEN, BLUE]

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    move_w = 3
    move_h = 3



    freeze = False

    while run :

        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_x:
                    c = random.choice(Selection)
                    Selection = [RED, GREEN, BLUE]
                    Selection.remove(c)
                if event.key == pygame.K_f:
                    freeze = not(freeze)
        if not freeze:
            if w < PADDING or w > WINDOW_WIDTH - PADDING:
                move_w *= -1

            if h < PADDING or h > WINDOW_HEIGHT - PADDING:
                move_h *= -1

            # UPDATE
            w += move_w
            h += move_h

            label = f'{w}, {h}'
            font = pygame.font.Font('freesansbold.ttf', 24)
            TextLabel = font.render(str(label), True, (0,0,0), (255,255,255))
            TextRect = TextLabel.get_rect(center=(WINDOW_WIDTH//2, 45))

            WINDOW.blit(TextLabel, TextRect)
            pygame.draw.circle(WINDOW, c, (w,h), 10)

            #pygame.display.update()
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()

```
