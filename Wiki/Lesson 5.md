# Table of contents

| Content             | Remark                 |
| ------------------- | ---------------------- |
| 1. Objective        | ---                    |
| 2. Recap            | ---                    |
| 3. Lesson           | ---                    |
| 4. Review Questions | To check understanding |
| 5. Mini Project     | Bonus Task             |

# Objective

- Creating an Interactive Bar in Pygame

## 2. Recap on Pygame Basics

Let's begin by running a sample code using Python pygame in the previous lessons focusing on keyboard input

## 2.1 Creating Pygame Window & Background Color

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

## 2.2 Mini Refresher

```python
# Create a red rectangle with a top-left corner at (10, 30), a width of 50 pixels, and a height of 70 pixels
rectangle1 = pygame.Rect(10, 30, 50, 70)
pygame.draw.rect(WINDOW, RED, rectangle1)

# Create a blue rectangle with a top-left corner at (50, 70), a width of 50 pixels, and a height of 70 pixels
rectangle2 = pygame.Rect(50, 70, 50, 70)
pygame.draw.rect(WINDOW, BLUE, rectangle2)

# Create a blue rectangle with a top-left corner at (100, 150), a width of 50 pixels, a height of 70 pixels, and a border thickness of 3 pixels
rectangle3 = pygame.Rect(100, 150, 50, 70)
pygame.draw.rect(WINDOW, BLUE, rectangle3, 3)
```

To check your understanding of Pygame mechanics, here are some questions

- What library is being used in this code?
- What does the pygame.Rect() function do?
- How many rectangles are being created in this code?
- What are the dimensions of the first rectangle?
- What color is the second rectangle?

# 3. Lesson

# 3.1 Creating a Interactive Bar

Pygame is a popular Python library used for creating video games and multimedia applications. In this section, we will be learning how to create an interactive rectangle in Pygame using variables to hold its width.

To get started, we will break down the code into smaller steps:

1. Import the Pygame library and initialize the game:

```python
import pygame

pygame.init()

# Create a display window
screen = pygame.display.set_mode((640, 480))
```

2. Define the variables for the rectangle:

```python
# Set the initial width of the rectangle
rect_width = 50

# Set the position of the rectangle on the screen
rect_x = 100
rect_y = 100

# Define the color of the rectangle
rect_color = (255, 255, 255)
```

3. Draw the rectangle on the screen:

```python
# Draw the rectangle on the screen
pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, 50))

# Refresh the screen to show the rectangle
pygame.display.flip()
```

4. Set up an event loop to respond to user input:

```python
# Set up an event loop to respond to user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Increase or decrease the width of the rectangle in response to user input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_width -= 10
            elif event.key == pygame.K_RIGHT:
                rect_width += 10
```

5. Update the rectangle width and refresh the screen in response to user input:

```python
    # Update the rectangle width and refresh the screen
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, 50))
    pygame.display.flip()
```

By using a variable to hold the value of the rectangle's width, we can easily adjust the shape in response to user input. For example, when the user presses the left arrow key, the rectangle's width will decrease by 10 pixels, and when they press the right arrow key, the width will increase by 10 pixels.

### Activity

Write a pygame code using the above

## 3.2 Percentage

We are able to create adjust the width with absolute values. Can we do better with percentage?

1. Import the Pygame library and initialize the game:

```python
import pygame

pygame.init()

# Create a display window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
```

2. Define the variables for the rectangle as percentages of the screen width:

```python
# Set the initial width of the rectangle as a percentage of the screen width
rect_width_pct = 0.2
rect_width = int(screen_width * rect_width_pct)

# Set the position of the rectangle on the screen as percentages of the screen height and width
rect_x_pct = 0.2
rect_x = int(screen_width * rect_x_pct)
rect_y_pct = 0.2
rect_y = int(screen_height * rect_y_pct)

# Define the color of the rectangle
rect_color = (255, 255, 255)
```

3. Draw the rectangle on the screen:

```python
# Draw the rectangle on the screen
pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, int(screen_height * 0.1)))

# Refresh the screen to show the rectangle
pygame.display.flip()
```

4. Set up an event loop to respond to user input:

```python
# Set up an event loop to respond to user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Increase or decrease the width of the rectangle in response to user input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_width_pct -= 0.02
            elif event.key == pygame.K_RIGHT:
                rect_width_pct += 0.02
            rect_width = int(screen_width * rect_width_pct)
```

5. Update the rectangle width and refresh the screen in response to user input:

```python
    # Update the rectangle width and refresh the screen
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, int(screen_height * 0.1)))
    pygame.display.flip()
```

By using a variable to hold the percentage value of the rectangle's width, we can easily adjust the shape in response to user input as a proportion of the screen width. For example, when the user presses the left arrow key, the rectangle's width will decrease by 2% of the screen width, and when they press the right arrow key, the width will increase by 2% of the screen width.

# 3.3 Adding the border

Adding a border to a rectangle in Pygame involves drawing two rectangles on the screen: one for the border and one for the rectangle itself.

To draw the border, we first need to calculate its dimensions based on the dimensions of the rectangle. We do this by adding the thickness of the border to both the width and height of the rectangle. For example, if the rectangle has a width of 100 pixels and the border thickness is 2 pixels, then the width of the border rectangle will be 104 pixels.

Once we have the dimensions of the border rectangle, we can draw it using the pygame.draw.rect() function. We pass the function the color of the border, the dimensions of the border rectangle, and the thickness of the border.

Next, we draw the actual rectangle on top of the border. We pass the function the color of the rectangle and the dimensions of the rectangle without the border thickness.

To ensure that the border appears around the rectangle, we draw the border rectangle before we draw the rectangle itself.

Calculate the dimensions of the border rectangle and then draw the border using pygame.draw.rect() with the border_color variable, border_thickness variable, and the adjusted dimensions of the border rectangle. We draw the border rectangle first and then draw the actual rectangle on top of it using the rect_color variable and the original dimensions of the rectangle.

```python
import pygame
import sys

pygame.init()

# Create a display window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the initial width of the rectangle as a percentage of the screen width
rect_width_pct = 0.2
rect_width = int(screen_width * rect_width_pct)

# Set the position of the rectangle on the screen as percentages of the screen height and width
rect_x_pct = 0.2
rect_x = int(screen_width * rect_x_pct)
rect_y_pct = 0.2
rect_y = int(screen_height * rect_y_pct)

# Define the color of the rectangle and border
rect_color = (255, 255, 255)
border_color = (0, 0, 0)

# Define the thickness of the border
border_thickness = 2

# Draw the rectangle and border on the screen
pygame.draw.rect(screen, border_color, (rect_x - border_thickness, rect_y - border_thickness, rect_width + border_thickness * 2, int(screen_height * 0.1) + border_thickness * 2))
pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, int(screen_height * 0.1)))

# Refresh the screen to show the rectangle
pygame.display.flip()

# Set up an event loop to respond to user input
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Increase or decrease the width of the rectangle in response to user input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_width_pct -= 0.02
            elif event.key == pygame.K_RIGHT:
                rect_width_pct += 0.02
            rect_width = int(screen_width * rect_width_pct)

        # Draw the rectangle and border with the updated width and refresh the screen
        pygame.draw.rect(screen, border_color, (rect_x - border_thickness, rect_y - border_thickness, rect_width + border_thickness * 2, int(screen_height * 0.1) + border_thickness * 2))
        pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, int(screen_height * 0.1)))
        pygame.display.flip()
```

# 4. Review Question

## Question 1

What is Pygame?

<ol type="a">
<li>A programming language
<li>A game development library for Python
<li>A video game console
<li>A type of game engine
</ol>
<details>
  <summary>Answer</summary>
  B. Pygame is a game development library for Python that provides functionality for creating games and other multimedia applications.
  </details>

---

## Question 2

Which Pygame function is used to draw a rectangle?

<ol type="a">
<li>pygame.draw.line()
<li>pygame.draw.circle()
<li>pygame.draw.rect()
<li>pygame.draw.polygon()
</ol>
<details>
  <summary>Answer</summary>
  C. The pygame.draw.rect() function is used to draw a rectangle in Pygame.
  </details>

---

## Question 3

What is the purpose of using variables instead of hardcoding values in Pygame?

<ol type="a">
<li>To make the code easier to read and understand
<li>To make the code more efficient and faster
<li>To make the code more flexible and adaptable
<li>To prevent errors from occurring in the code
</ol>
<details>
  <summary>Answer</summary>
  C. Using variables instead of hardcoding values in Pygame makes the code more flexible and adaptable because the values can be easily changed without having to modify the code itself.
  </details>

---

## Question 4

How do you add a border to a rectangle in Pygame?

<ol type="a">
<li>By drawing two rectangles, one for the border and one for the rectangle itself
<li>By using the pygame.draw.border() function
<li>By adjusting the color and thickness parameters of the pygame.draw.rect() function
<li>By using the pygame.draw.line() function to draw lines around the rectangle
</ol>
<details>
  <summary>Answer</summary>
   A. To add a border to a rectangle in Pygame, you need to draw two rectangles: one for the border and one for the rectangle itself.
  </details>

---

## Question 5

What does pygame.display.flip() do in Pygame?

<ol type="a">
<li>Closes the Pygame window
<li>Refreshes the Pygame window to display any changes made to the screen
<li>Plays a sound effect in the Pygame window
<li>Resets the Pygame window to its default state
</ol>
<details>
  <summary>Answer</summary>
B. The pygame.display.flip()

Explantion
function refreshes the Pygame window to display any changes made to the screen. This is necessary to update the screen after drawing shapes or making other changes to the display.

  </details>

# 5. Mini Project - Growing Circle

Enhance the code above by trying the following;

- Use a Circle instead of Rectangle
- Draw multiple circles with different positions, sizes, colors, and borders to create a more complex image or animation.
- Use loops and variables to create a pattern or grid of circles on the screen.
