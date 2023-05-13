# Table of contents

| Content             | Remark                 |
| ------------------- | ---------------------- |
| 1. Objective        | ---                    |
| 2. Recap            | ---                    |
| 3. Lesson           | ---                    |
| 4. Review Questions | To check understanding |
| 5. Mini Project     | Bonus Task             |

# 1. Objective

- Text box Input

# 2. Recap on Pygame Basics

## 3.1 Creating a basic textbox input

## 3.2 Creating an advance textbox input with different color themes

Here is a step-by-step guide to create the textbox input:

1. Import the Pygame library.

```python
import pygame
```

2. Initialize Pygame using pygame.init().

```python
pygame.init()
```

3. Set up the display using `pygame.display.set_mode((width, height)), where widthandheightare the dimensions of the window.

```python
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Input Example")
```

4. Define a font for the text input usingpygame.font.Font(font, size)`.

```python
font = pygame.font.Font(None, 32)
```

5. Create a text input box using pygame.Rect(x, y, width, height).

```python
text_input = pygame.Rect(100, 150, 140, 32)
```

6. Set the inactive and active colors for the text input box using pygame.Color().

```python
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_active
active = False
text = ''
```

7. Start the main loop using while running:

```python
running = True
while running:
```

8. Handle Pygame events in the loop using for event in pygame.event.get():

```python
    for event in pygame.event.get(): ## <---
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You entered: ", text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) < 15:
                    text += event.unicode
```

9. If the event type is QUIT, set running to False to end the loop.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## <---
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You entered: ", text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) < 15:
                    text += event.unicode
```

10. If the event type is KEYDOWN, handle the input. Use if event.key == pygame.K_RETURN: to print the text entered. Use elif event.key == pygame.K_BACKSPACE: to handle backspace. For other keys, add the unicode character to the text variable.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: ## <---
            if event.key == pygame.K_RETURN:
                print("You entered: ", text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) < 15:
                    text += event.unicode
```

11. Render the text input box by filling the screen with a color, drawing the rect, and blitting the text surface on top.

```python
    screen.fill((30, 30, 30))
    txt_surface = font.render(text, True, (0,0,0))
    width = max(200, txt_surface.get_width()+10)
    text_input.w = width
    pygame.draw.rect(screen, color, text_input)
    screen.blit(txt_surface, (text_input.x+5, text_input.y+5))
```

12. Update the display using pygame.display.update().

```python
    pygame.display.update()
```

13. End the main loop.

14. Quit Pygame using pygame.quit().

```python
pygame.quit()
```

# 4. Review Questions

## Question 1

Which Pygame module is used to create text input in Pygame?

<ol type="a">
<li>pygame.input
<li>pygame.keyboard
<li>pygame.text
<li>pygame.font
</ol>

<details>
  <summary>Answer</summary> D) pygame.font

Explanation: The pygame.font module is used to create and manipulate fonts in Pygame, including rendering text to surfaces.

</details>

---

## Question 2

What is the purpose of the pygame.Rect class in Pygame text input?

<ol type="a">
<li>To represent the position and size of the text input box
<li>To hold the text input value
<li>To handle user input events
<li>None of the above
</ol>

<details>
  <summary>Answer</summary> A) To represent the position and size of the text input box

Explanation: The pygame.Rect class in Pygame is used to represent a rectangular area, including its position and size. It is often used in Pygame text input to define the position and size of the text input box on the screen.

</details>

---

## Question 3

How is user input handled in Pygame text input?

<ol type="a">
<li>Using the pygame.event.get() function to get user input events
<li>Using the pygame.keyboard.get_pressed() function to get the current keyboard state
<li>Using the pygame.text module to parse user input events
<li>Using the pygame.mouse.get_pos() function to get the current mouse position
</ol>

<details>
  <summary>Answer</summary> A) Using the pygame.event.get() function to get user input events

Explanation: In Pygame text input, user input is typically handled using the pygame.event.get() function to get all the events that have occurred since the last loop iteration. This allows the program to detect and respond to user input events, such as key presses or mouse clicks.

</details>

---

## Question 4

What is the purpose of the unicode attribute of a Pygame event?

<ol type="a">
<li>To store the current state of the keyboard
<li>To represent the current mouse position
<li>To hold the user input character for keyboard events
<li>None of the above
</ol>

<details>
  <summary>Answer</summary> C) To hold the user input character for keyboard events

Explanation: The unicode attribute of a Pygame event is used to hold the Unicode value of a character for keyboard events. This allows the program to capture and process the user's input text.

</details>

---

## Question 5

How can the Pygame font be customized in Pygame text input?

<ol type="a">
<li>By changing the size of the text input box
<li>By changing the font style and size
<li>By changing the font color
<li>By changing the font type
</ol>

<details>
  <summary>Answer</summary> B) By changing the font style and size

Explanation: The Pygame font can be customized in Pygame text input by changing the font style and size using the pygame.font.Font() function. This allows the program to display the input text in different styles and sizes.

# 5. Mini Project - Creating a login page
