# Overview

| Lesson | Topic                             | Review Questions Available |
| :----- | :-------------------------------- | :------------------------- |
| 1      | Pygame Basics and Keyboard Inputs | Yes                        |
| 2      | Pygame Input and Text             | Yes                        |
| 3      | Project                           | No                         |
| 4      | Pygame Draw                       | Yes                        |
| 5      | Pygame Images                     | Yes                        |
| 6      | Project                           | No                         |
| 7      | Creating Interactive Objects      | Yes                        |
| 8      | Creating Transition States        | Yes                        |
| 9      | Project                           | No                         |
| 10     | Creating Menu Navigation          | Yes                        |
| 11     | Creating Timer Screen             | Yes                        |
| 12     | Project                           | No                         |

---

# Lesson 1

## Concepts

- Introduction to Pygame and its features
- Pygame setup and creating a window
- Handling keyboard inputs with Pygame

---

## Review Questions

### Question 1

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

### Question 2

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

### Question 3

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

### Question 4

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

### Question 5

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

---

# Lesson 2

## Concepts

- Handling keyboard inputs
- Understanding Pygame events
- Creating Text Objects in Pygame
  - Different sizes
  - Different fonts
  - Different position

## Review Questions

### Question 1

Which of the following is a benefit of using OOP for rendering screens in Pygame?

<ol type="a">
  <li>Allows for easier management of screen elements</li>
  <li>Makes it easier to organize code</li>
  <li>Makes it easier to add new screens to the game</li>
  <li>All of the above</li>
</ol>

<details>
  <summary>Answer</summary>
  d. All of the above

Explanation: OOP allows for a more organized and modular approach to building games, making it easier to manage and add new elements as needed.

</details>

---

### Question 2

Which Pygame module is used for rendering text objects?

<ol type="a">
  <li>pygame.text</li>
  <li>pygame.font</li>
  <li>pygame.display</li>
  <li>pygame.event</li>
</ol>

<details>
  <summary>Answer</summary>
  b. pygame.font
  
  Explanation: The pygame.font module provides functions for rendering text objects in Pygame.
</details>

---

### Question 3

How can you change the font size of a text object in Pygame?

<ol type="a">
  <li>Using the set_size() function</li>
  <li>Using the set_bold() function</li>
  <li>Using the set_italic() function</li>
  <li>Using the set_height() function</li>
</ol>

<details>
  <summary>Answer</summary>
  d. Using the set_height() function
  
  Explanation: The set_height() function can be used to set the font size of a text object in Pygame.
</details>

---

### Question 4

How can you set the position of a text object in Pygame?

<ol type="a">
  <li>Using the set_position() function</li>
  <li>Using the set_rect() function</li>
  <li>Using the set_anchor() function</li>
  <li>Using the set_xy() function</li>
</ol>

<details>
  <summary>Answer</summary>
  b. Using the set_rect() function
  
  Explanation: The set_rect() function can be used to set the position of a text object in Pygame.
</details>

---

### Question 5

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

# Lesson 3 - Project

No Questions

# Lesson 4

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

# Lesson 5

---

# Lesson 6

No Questions

---

# Lesson 7

---

# Lesson 8

---

# Lesson 9

No Questions

---

# Lesson 10

---

# Lesson 11

---

# Lesson 12

No Questions
