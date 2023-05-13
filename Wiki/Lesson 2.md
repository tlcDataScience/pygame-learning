# Table of contents

| Content                           | Remark                 |
| --------------------------------- | ---------------------- |
| 1. Objective                      | ---                    |
| 2. Recap on Pygame Basics         | ---                    |
| 3. Pygame Text Objects            | ---                    |
| 4. Review Questions               | To check understanding |
| 5. Mini Project - Color Picker v2 | Bonus Task             |

# 1. Objective

- Handling keyboard inputs
- Understanding Pygame events
- Creating Text Objects in Pygame
  - Different sizes
  - Different fonts
  - Different position
- Mini Project - Color picker v2

# 2. Recap on Pygame Basics

## 2.1 Setting up the Pygame Window

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

## 2.2 Mini Refresher

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
- What is the purpose of setting "g" to 255?
- How is "g" set to 0?
- What happens when the pygame.K_d constant is detected?
- How does setting "b" to 255 affect the program?

# 3. Pygame Text Objects

## 3.1 Setting up the Pygame with a text object

In the previous lesson, we have learnt about what is Pygame and even created a simple color picker with keyboard controls. Let's now learn to insert text.

To insert text onto the screen, we will create a class that loads the screen with the text. In the code below, we have created a class `Screen` that will render a text in the middle of the screen.

`self.font = pygame.font.Font('freesansbold.ttf', 32)` loads the type of font used & the size of the font

`self.label = "TEXT"` loads the string value of the text

`self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))` renders the text based on the string value, color of font & color of background of font

`self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))` positions the textbox in the middle of the screen

```python
class Screen:
    def __init__(self) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "TEXT"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))   # Change position
```

An additional feature has also been added in this code to easily exit the program since there is a lot of navigation between the code and pygame.

```python
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
```

This is the sample code.

```python
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

class Screen:
    def __init__(self) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "TEXT"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))   # Change position

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)

    run = True

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        test_screen = Screen()
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

To formally explain what we have created in the sample code is using Object Oriented Programming, we have created a class for the screen. Within the screen class, we are able create a screen object that will load the text onto the window

```python
class Screen:
    def __init__(self) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "TEXT"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
```

Firstly, to define a new class, we will use `class` as the keyword along with the class name. We will next initialise the class value upon creation `def __init__(self):` which is essentially the attributes of the class. With that you will have

```python
class Screen:
    def __init__(self) :
        pass
```

To assign attributes belonging to class, we will include the `self.` in front of the variable name. `self.font` means that font variable will belong to the class.

Let's look at the line by line what is being done

1. Using pygame module, we will use the default font 'freesansbold.ttf'. 32 is the size of the font. The bigger the value, the bigger the size of the text

```python
self.font = pygame.font.Font('freesansbold.ttf', 32)
```

2. We can next store the data for the text within a label variable for easier manipulation

```python
self.label = "TEXT"
```

3. Now, we can render the text, with the color and fill. It is to draw text on a new Surface.
   **render(text, antialias, color, background=None)**

```python
self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
```

4. Lastly, we need to bound the textbox so that we can indicate the position of the textbox within the window

```python
self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
```

At this point, we have only created the class Screen. We have yet to use it within the main loop. This is where we will need to load it onto the surface.

pygame.Surface.blit -> draw one image onto another

```python
        test_screen = Screen()
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)
```

## 3.2 Changing the position of the text

Let's modify the screen class to shift the text. Currently if you run the sample code above, it will be in the middle of the screen. This is because we used relative positioning where we took the middle of the width & height.

```python
self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
```

We made a change for the center to

```python
self.TextRect = self.TextLabel.get_rect(center=(WINDOW_WIDTH//3, WINDOW_HEIGHT//3))
```

What will you expect?

Try adjusting the values of the `center =(width, height)` to see how you can shift the text around the screen. Maybe try shifting it to the bottom right? Or top right?

## 3.3 Shifting it dynamically

We can bring back the keyboard inputs from the previous lesson to adjust the text using WSAD where W - Up, S - Down, A - Left, D - Right.
Essentially what we are trying to do is to shift the position values and create a new screen to load. This gives the visual representation of the object moving.

```python
# Controlling positions

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


class Screen:
    def __init__(self, w, h) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "TEXT"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(w, h))   # Change position

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_a:
                    w = w - 10
                if event.key == pygame.K_d:
                    w = w + 10
                if event.key == pygame.K_w:
                    h = h - 10
                if event.key == pygame.K_s:
                    h = h + 10

        test_screen = Screen(w, h)
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

Did you find a bug with the dynamic shifting of text? Well, if you try to move the text off the screen, its possible. Maybe that isn't such a good idea. Can we fix it such that we can always have the full text within the screen? Yes, by adding border

## 3.4 Adding borders to dynamic shifting

We will restrict the amount that can be updated. This will provide a nice buffer between the edges and the text. Like a buffer.

```python
# Controlling positions

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


class Screen:
    def __init__(self, w, h) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "TEXT"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(w, h))   # Change position

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_a:
                    w = w - 10
                if event.key == pygame.K_d:
                    w = w + 10
                if event.key == pygame.K_w:
                    h = h - 10
                if event.key == pygame.K_s:
                    h = h + 10




        test_screen = Screen(w, h)
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

Let's challenge ourselves using what we have learnt with our mastery of python. We will change the text to 'O' and request for more functionality. Here's a sample code.

```python
# Controlling positions

import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


class Screen:
    def __init__(self, w, h) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = "O"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(w, h))   # Change position

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

                if event.key == pygame.K_a:
                    if w > PADDING:
                        w = w - 10
                if event.key == pygame.K_d:
                    if w < WINDOW_WIDTH-PADDING:
                        w = w + 10
                if event.key == pygame.K_w:
                    if h > PADDING:
                        h = h - 10
                if event.key == pygame.K_s:
                    if h < WINDOW_HEIGHT-PADDING:
                        h = h + 10




        test_screen = Screen(w, h)
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

## 3.5 Activity

Now, its your turn to add the functionality. Here's the user requirements

| User Story                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a user, I want to be able to see the exact location of my text on the screen and its dimensions (width and height) as I move it, so that I can better position and align my text.                                                           | To implement this, you could add a visual overlay or a tooltip that displays the coordinates and dimensions of the text as the user moves it around.                                                           |
| As a user, I want to be able to change the background color of my text while I'm moving it, so that I can see how it looks against different backgrounds. Additionally, I want the text color to update automatically to ensure good contrast. | To implement this, you could add a color picker tool that allows the user to select a new background color. You can then update the text color to ensure that it contrasts well with the new background color. |
| As a user, I want to be able to cycle through the alphabet characters when I'm editing my text, instead of only having the option to change it to the letter "O".                                                                              | To implement this, you could add a dropdown menu or                                                                                                                                                            |

# 4. Review Questions

## Question 1

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

## Question 2

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

## Question 3

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

## Question 4

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

## Question 5

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

# 5. Mini Project - Color Picker v2

Great job! Let's make some improvements to our color picker.
Our color picker can change the colors along a gradient. Instead of looking at the console, can we display the r,g,b on the screen itself? Even better, I can move the r,g,b values around the screen. In a nutshell, I want the best of both worlds.

[Replit Code](https://replit.com/@tlcDataScience/ColorPickerV2#main.py)
