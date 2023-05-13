# Table of contents

| Content                           | Remark                 |
| --------------------------------- | ---------------------- |
| 1. Objective                      | ---                    |
| 2. Recap on Pygame Basics         | ---                    |
| 3. Pygame Drawing Shape Objects   | ---                    |
| 4. Review Questions               | To check understanding |
| 5. Mini Project - Color Picker v2 | Bonus Task             |

# 1. Objective

- Drawing Objects in Pygame
- Animating Drawn Objects in Pygame
- Mini Project - Digital Scoreboard v3 - making better themes with shapes

# 2. Recap on Pygame Basics

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

To check your understanding of Pygame mechanics, here are some questions

1. How do you define the width & height of Pygame Window?
2. How do you define the color of the Pygame Background?
3. Why do we need a `while True:` within the code?
4. If we want to exit from the Pygame Window by pressing 'Q', how should we modify the code?
5. What are the steps needed if we want to start a pygame project on a new computer?

# 3. Pygame Drawing Shape Objects

In this lesson, we will be having an end goal of creating drawings with pygame by introducing how to draw shapes. This tutorial focus more on the basic shapes like rectangle, squares, circles. However, with these shapes and deliberate overlaying of the images, we can create interesting shapes like Trees and Clouds in the images below.

**Example shapes to create**

<img width="396" alt="Screenshot 2022-12-24 at 11 55 45 AM" src="https://user-images.githubusercontent.com/102406967/209425137-66522ca8-a71a-4d8c-902f-1c2e9fb2bf5b.png">

<img width="403" alt="image" src="https://user-images.githubusercontent.com/102406967/209419802-62b2a86e-2be3-410d-83f0-6e0037659495.png">

## 3.1 Draw Rectangle

To create a rectangle using pygame, we first need to create a pygame.Rect object. A rectangle has four sides, and its sides are connected at 90-degree angles. To create a rectangle using pygame, we can use the following syntax: pygame.Rect(left, top, width, height). Here, we need to specify the position of the top-left corner of the rectangle, along with its width and height.

Once we have created a pygame.Rect object, we can draw the rectangle using `pygame.draw.rect()`. The syntax for `pygame.draw.rect()` is `pygame.draw.rect(surface, color, rect)`. Here, surface refers to the surface on which the rectangle will be drawn, color specifies the color of the rectangle, and rect refers to the pygame.Rect object we created earlier.

`pygame.draw.rect(surface, color, rect, width=0)` takes several parameters:

- `surface`: The surface on which to draw the rectangle. This can be a pygame.Surface object.
- `color`: The color of the rectangle in RGB format. This can be a tuple, list or any other sequence of three integers representing the red, green and blue components of the color. For example, (255, 0, 0) represents red, (0, 255, 0) represents green, and (0, 0, 255) represents blue.
- `rect`: A pygame.Rect object that specifies the dimensions of the rectangle. This can be created using the pygame.Rect() constructor or by passing a tuple containing the (x, y, width, height) coordinates of the rectangle.
- `width (optional)`: The width of the rectangle's outline in pixels. If 0 or not provided, the rectangle will be filled with the color.

For example, if we want to draw a red rectangle in the WINDOW surface, we can use the following code:

```python
# Create a pygame.Rect object
rectangle1 = pygame.Rect(100, 100, 50, 50)

# Draw the rectangle on the WINDOW surface
pygame.draw.rect(WINDOW, RED, rectangle1)

```

In this code, rectangle1 is a pygame.Rect object that represents a rectangle with a top-left corner at (`100, 100)`, a width of `50` pixels, and a height of `50` pixels. We then use `pygame.draw.rect()` to draw the rectangle on the WINDOW surface, using the color RED (which we defined earlier).

---

We can create different variations of a rectangle in pygame by changing its position, dimensions, and color. To do this, we can create new pygame.Rect objects with different parameters.

For example, if we want to create a red rectangle with a top-left corner at `(10, 30)`, a width of `50` pixels, and a height of `70` pixels, we can use the following code:

```python
rectangle1 = pygame.Rect(10, 30, 50, 70)
pygame.draw.rect(WINDOW, RED, rectangle1)
```

This will create a red rectangle at `(10, 30)` with a width of `50` pixels and a height of `70` pixels.

Similarly, if we want to create a blue rectangle with a top-left corner at `(50, 70)`, a width of `50` pixels, and a height of `70` pixels, we can use the following code:

```python
rectangle2 = pygame.Rect(50, 70, 50, 70)
pygame.draw.rect(WINDOW, BLUE, rectangle2)
```

This will create a blue rectangle at `(50, 70)` with a width of `50` pixels and a height of `70` pixels.

Additionally, we can also change the thickness of the rectangle by passing a third argument to `pygame.draw.rect()`. For example, if we want to create a blue rectangle with a top-left corner at `(100, 150)`, a width of `50` pixels, a height of `70` pixels, and a border thickness of `3` pixels, we can use the following code:

```python
rectangle3 = pygame.Rect(100, 150, 50, 70)
pygame.draw.rect(WINDOW, BLUE, rectangle3, 3)
```

This will create a blue rectangle at (100, 150) with a width of 50 pixels, a height of 70 pixels, and a border thickness of 3 pixels.

Here's a summarised code with comments:

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

### 3.1.1 Activity

Based on the code snippets, try writing out a complete pygame code for it. You may use the following sample code

```python
import pygame

# Initialize pygame
pygame.init()

# Define the colors we will use (RGB format)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Rectangles')

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a red rectangle with a top-left corner at (10, 30), a width of 50 pixels, and a height of 70 pixels
rectangle1 = pygame.Rect(10, 30, 50, 70)

# Create a blue rectangle with a top-left corner at (50, 70), a width of 50 pixels, and a height of 70 pixels
rectangle2 = pygame.Rect(50, 70, 50, 70)

# Create a blue rectangle with a top-left corner at (100, 150), a width of 50 pixels, a height of 70 pixels, and a border thickness of 3 pixels
rectangle3 = pygame.Rect(100, 150, 50, 70)

# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white
    WINDOW.fill((255, 255, 255))

    # Draw the rectangles
    pygame.draw.rect(WINDOW, RED, rectangle1)
    pygame.draw.rect(WINDOW, BLUE, rectangle2)
    pygame.draw.rect(WINDOW, BLUE, rectangle3, 3)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate to 60 fps
    clock.tick(60)

# Quit pygame
pygame.quit()
```

## 3.2 Draw Circle & Ellipses

Moving on.. to create a rectangle in Pygame, we can use the pygame.Rect class. The syntax for creating a pygame.Rect object is `Rect(left, top, width, height)`. We need to pass in the values of the top-left corner of the rectangle, followed by the width and height.

Once we have created a pygame.Rect object, we can draw it on the screen using the `pygame.draw.rect()` function. The function takes three arguments: the window to draw on, the color of the rectangle, and the pygame.Rect object representing the rectangle.

Similarly, we can create a circle in Pygame using the `pygame.draw.circle() `function. The function takes four arguments: the window to draw on, the color of the circle, the center point of the circle (specified as an (x, y) tuple), and the radius of the circle.

`pygame.draw.circle(surface, color, center, radius, width=0)` takes several parameters:

- `surface`: The surface on which to draw the circle. This can be a pygame.Surface object.
- `color`: The color of the circle in RGB format. This can be a tuple, list or any other sequence of three integers representing the red, green and blue components of the color. For example, (255, 0, 0) represents red, (0, 255, 0) represents green, and (0, 0, 255) represents blue.
- `center`: A tuple containing the (x, y) coordinates of the center of the circle.
- `radius`: The radius of the circle in pixels.
- `width (optional)`: The width of the circle's outline in pixels. If 0 or not provided, the circle will be filled with the color.

Here's an example code snippet that creates and displays a blue circle with a center point of (50, 70) and a radius of 10:

```python
# Define the colors we will use (RGB format)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create a red rectangle at position (10, 30) with width 50 and height 70
shape1 = pygame.Rect(10, 30, 50, 70)
pygame.draw.rect(WINDOW, RED, shape1)

# Create a blue circle with center at (50, 70) and radius 10
pygame.draw.circle(WINDOW, BLUE, (50,70), 10)

# Create a green ellipse at position (100, 150) with width 50 and height 70
shape3 = pygame.Rect(100, 150, 50, 70)
pygame.draw.ellipse(WINDOW, GREEN, shape3)
```

---

**Why `pygame.draw.circle` does not use `pygame.rect`?**

While the `pygame.draw.rect()` function draws a rectangle shape, the `pygame.draw.circle()` function draws a circle shape which requires a different set of parameters.

Specifically, the `pygame.draw.circle()` function takes a surface object, a color, a center point (as a tuple of (x, y) coordinates), and a radius value.

In the provided code snippet, the `pygame.Rect()` function is used to create a rectangle object rectangle2 which is then passed to the `pygame.draw.circle()` function as the second parameter (i.e., the color parameter). This is actually incorrect, as the color parameter should be a tuple of RGB values, not a `pygame.Rect()` object.

## 3.3 Draw Line

To draw a line in Pygame, you can use the pygame.draw.line() function. This function takes several parameters:

- `surface`: the surface on which to draw the line
- `color`: the color of the line, in RGB format
- `start_pos`: the starting position of the line, as a tuple of (x, y) coordinates
- `end_pos`: the ending position of the line, as a tuple of (x, y) coordinates
- `width`: the width of the line (in pixels)

Here's an example of how to draw a line in Pygame:

```python
import pygame

# Initialize pygame
pygame.init()

# Set up the display window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Line')

# Define the color we will use (RGB format)
BLACK = (0, 0, 0)

# Draw a black line from (0, 0) to (400, 400)
pygame.draw.line(WINDOW, BLACK, (0, 0), (400, 400), 5)

# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
```

This code will draw a black line from the top-left corner of the screen to the bottom-right corner, with a width of 5 pixels. You can adjust the `start_pos`, `end_pos`, and `width` parameters to create different line shapes and styles.

## 3.4 Draw Polygon

To draw a polygon in Pygame, you can use the pygame.draw.polygon() function. This function takes several parameters:

- `surface`: the surface on which to draw the polygon
- `color`: the color of the polygon, in RGB format
  points: a list of (x, y) tuples that define the vertices of the polygon
- `width`: the width of the polygon's outline (in pixels). If 0, the polygon will be filled.

Here's an example of how to draw a polygon in Pygame:

```python
import pygame

# Initialize pygame
pygame.init()

# Set up the display window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Polygon')

# Define the colors we will use (RGB format)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the vertices of the polygon as a list of (x, y) tuples
vertices = [(200, 50), (300, 200), (250, 300), (150, 300), (100, 200)]

# Draw the polygon with a green outline and a red fill
pygame.draw.polygon(WINDOW, GREEN, vertices, 2)
pygame.draw.polygon(WINDOW, RED, vertices, 0)

# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
```

This code will draw a polygon with five vertices on the screen, with a green outline and a red fill. You can adjust the `vertices`, `color`, and `width` parameters to create different polygon shapes and styles.

## 3.5 Activity

<img width="403" alt="image" src="https://user-images.githubusercontent.com/102406967/209419802-62b2a86e-2be3-410d-83f0-6e0037659495.png">

```python

# Creating shapes

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
ORANGE = (255, 184, 107)

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (107, 206, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    x = 100


    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                pass

        # CLOUD 1
        pygame.draw.circle(WINDOW, WHITE, (50,70), 20)
        pygame.draw.circle(WINDOW, WHITE, (75,70), 30)
        pygame.draw.circle(WINDOW, WHITE, (100,70), 20)

        # CLOUD 2
        pygame.draw.circle(WINDOW, WHITE, (50+x,70+x), 30)
        pygame.draw.circle(WINDOW, WHITE, (90+x,70+x), 50)
        pygame.draw.circle(WINDOW, WHITE, (130+x,70+x), 30)

        # SUN
        pygame.draw.circle(WINDOW, ORANGE, (75+x*2+15,70), 50)

        # CLOUD 3
        pygame.draw.circle(WINDOW, WHITE, (50+x*2,60), 20)
        pygame.draw.circle(WINDOW, WHITE, (75+x*2,60), 30)
        pygame.draw.circle(WINDOW, WHITE, (100+x*2,60), 20)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

<img width="396" alt="Screenshot 2022-12-24 at 11 55 45 AM" src="https://user-images.githubusercontent.com/102406967/209425136-09d53304-5495-4168-b641-c9394ce09476.png">

# Review Questions

## Question 1

Which of the following is the correct syntax for creating a Pygame Rect object?

<ol type="a">
  <li>pygame.rect(10, 20, 30, 40)</li>
  <li>pygame.Rect(10, 20, 30, 40)</li>
  <li>pygame.draw.rect(10, 20, 30, 40)</li>
  <li>rect(10, 20, 30, 40)</li>
</ol>
<details>
  <summary>Answer</summary>
b) pygame.Rect(10, 20, 30, 40)

Explanation: The correct syntax for creating a Pygame Rect object is pygame.Rect(left, top, width, height).

</details>

---

## Question 2

What is the purpose of the width parameter in the pygame.draw.line() function?

<ol type="a">
  <li>To set the thickness of the line</li>
  <li>To set the color of the line</li>
  <li>To set the length of the line</li>
   <li>To set the shape of the line</li>
</ol>

<details>
  <summary>Answer</summary>
  
a) To set the thickness of the line

Explanation: The width parameter in the pygame.draw.line() function is used to set the thickness of the line.

</details>

---

## Question 3

Which of the following is the correct syntax for drawing a circle in Pygame?

<ol type="a">
  <li>pygame.circle(SURFACE, color, center, radius)</li>
  <li>pygame.draw.circle(surface, color, center, radius)</li>
  <li>pygame.draw.circle(SURFACE, color, center, radius)</li>
  <li>pygame.draw.circle(color, center, radius)</li>
</ol>

<details>
  <summary>Answer</summary>

b) pygame.draw.circle(surface, color, center, radius)

Explanation: The correct syntax for drawing a circle in Pygame is pygame.draw.circle(surface, color, center, radius).

</details>

---

## Question 4

What is the difference between the pygame.draw.polygon() function with a width of 0 and a non-zero width?

<ol type="a">
  <li>There is no difference</li>
  <li>A width of 0 fills the polygon, while a non-zero width only outlines it</li>
  <li>A width of 0 only outlines the polygon, while a non-zero width fills it</li>
  <li>A width of 0 outlines the polygon and fills it</li>
</ol>

<details>
  <summary>Answer</summary>
  
 b) A width of 0 fills the polygon, while a non-zero width only outlines it

Explanation: The width parameter in the pygame.draw.polygon() function determines whether the polygon is filled or only outlined. A width of 0 fills the polygon, while a non-zero width only outlines it.

</details>

---

## Question 5

What are the parameters for the `pygame.draw.ellipse()` function?

<ol type="a">
  <li>surface, color, center, radius</li>
  <li>surface, color, rect</li>
  <li>surface, color, points</li>
  <li>color, points</li>
</ol>

<details>
  <summary>Answer</summary>
  
b) surface, color, rect

Explanation: The parameters for the pygame.draw.ellipse() function are surface, color, rect, where rect is a Pygame Rect object that defines the position and size of the ellipse.

</details>

---

# 5. Mini Project - Digital Scoreboard v3 - making better themes with shapes (Bonus)
