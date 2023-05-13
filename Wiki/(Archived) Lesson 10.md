# Table of contents

| Content             | Remark                 |
| ------------------- | ---------------------- |
| 1. Objective        | ---                    |
| 2. Recap            | ---                    |
| 3. Lesson           | ---                    |
| 4. Review Questions | To check understanding |
| 5. Mini Project     | Bonus Task             |

# 1. Objective

- Creating a countdown - Basic Timer
- Creating a countdown - Advance Timer with different color themes

# 2. Recap on Pygame Basics

# 3. Creating a timer

## 3.1 Creating a basic timer

## 3.1.1 What is a basic timer?

## 3.1.2 Step-by-step guide

Here is a step-by-step guide to create the timer:

1. Import Pygame: Add the following line at the beginning of your script to import Pygame:

```python
import pygame
```

2. Initialize Pygame: Before using Pygame, you need to initialize it by adding the following code:

```python
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Timer")
```

3. Define variables: Define the timer duration and start time:

```python
duration = 10
start_time = pygame.time.get_ticks()
```

4. Create a font: You will use this font to display the timer on the screen:

```python
font = pygame.font.Font(None, 36)
```

5. Main loop: This is the main loop that will run until the timer runs out. Add the following code:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    remaining_time = duration - elapsed_time

    text = font.render("Time remaining: " + str(int(remaining_time)), True, (255, 0, 0))
    screen.blit(text, (100, 100))

    pygame.display.update()
```

6. End the timer: After the timer runs out, add the following code to end the timer:

```python
if remaining_time <= 0:
    running = False
```

7. Quit Pygame: Finall,y add the following line to quit Pygame:

```python
pygame.quit()
```

This should create a timer in Pygame that counts down from the specified duration and displays the remaining time in red on the screen. You can adjust the duration, screen

## 3.2 Creating an advance timer with different color themes

## 3.2.1 What is an advance timer?

## 3.2.2 Step-by-step guide

Step-by-Step Guide:

1. Import the pygame library.

```python
import pygame
```

2. Initialize Pygame using pygame.init().

```python
pygame.init()
```

3. Define the screen size and title using screen = pygame.display.set_mode((400, 300)) and pygame.display.set_caption("Pygame Timer").

```python
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Timer")
```

4. Define the timer font using timer_font = pygame.font.Font(None, 36).

```python
timer_font = pygame.font.Font(None, 36)
```

5. Define color themes using a dictionary, themes = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}.

```python
themes = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}
```

6. Set the default theme using theme = "red".

```python
theme = "red"
```

7. Set the timer duration in seconds using duration = 10.

```python
duration = 10
```

8. Set the start time using start_time = pygame.time.get_ticks().

```python
start_time = pygame.time.get_ticks()
```

9. Start the game loop using while running:.

```python
running = True
while running:
```

10. Handle events using `for event

```python

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

11. Within the handler, it is able to change the theme by pressing "r" for red, "g" for green, or "b" for blue on your keyboard.

```python
        # Check for key events to switch themes
        if event.type == pygame.KEYDOWN:
            if event.unicode == "r":
                theme = "red"
            elif event.unicode == "g":
                theme = "green"
            elif event.unicode == "b":
                theme = "blue"
```

12. Main logic for the timer

```python

        # Check for key events to switch themes
        if event.type == pygame.KEYDOWN:
            if event.unicode == "r":
                theme = "red"
            elif event.unicode == "g":
                theme = "green"
            elif event.unicode == "b":
                theme = "blue"

    # Clear the screen
    screen.fill((255, 255, 255))

    # Calculate the time remaining
    time_remaining = duration - (pygame.time.get_ticks() - start_time) / 1000

    # Render the timer text
    timer_text = timer_font.render(str(time_remaining), True, themes[theme])
    timer_rect = timer_text.get_rect()
    timer_rect.center = (200, 150)

    # Draw the timer
    screen.blit(timer_text, timer_rect)

    # Update the display
    pygame.display.update()
```

13. End the timer: After the timer runs out, add the following code to end the timer:

```python
    if time_remaining <= 0:
        running = False
```

# Advance Timer with input

Here is a step-by-step guide to create the timer:

1. Import the Pygame module:

```python
import pygame
```

2. Initialise Pygame:

```python
pygame.init()
```

3. Set the size of the window:

```python
window_size = (400, 300)
```

4. Create the window:

```python
screen = pygame.display.set_mode(window_size)
```

5. Set the font for the timer:

```python
font = pygame.font.Font(None, 36)
```

6. Define the Timer class:

```python
class Timer:
    def __init__(self, initial_value):
        # Convert the initial value from seconds to milliseconds
        self.initial_value = initial_value * 1000
        self.start_time = pygame.time.get_ticks()

    # Method to update the timer value
    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        return self.initial_value - elapsed_time

    # Method to display the timer on the screen
    def display(self, screen):
        timer_text = font.render(str(self.update() // 1000), True, (0, 0, 0))
        screen.blit(timer_text, (150, 150))
```

7. Get the initial value for the timer from the user:

```python
initial_value = int(input("Enter the initial value for the timer (in seconds): "))
```

8. Create an instance of the Timer class:

```python
timer = Timer(initial_value)
```

9. Start the game loop:

```python
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the timer has reached 0
    if timer.update() <= 0:
        running = False

    # Display the timer
    timer.display(screen)

    pygame.display.update()
```

10. Quit Pygame:

```python
pygame.quit()
```

# Review Question

```python
import pygame

# Initialize Pygame and create a display window
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Timer")

# Set the duration of the timer and get the start time
duration = 10  # seconds
start_time = pygame.time.get_ticks()

# Create a font object for displaying the timer
font = pygame.font.Font(None, 36)

# Main loop that runs until the timer runs out
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the elapsed time and remaining time on the timer
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # convert to seconds
    remaining_time = duration - elapsed_time

    # Render the updated timer text onto the screen
    text = font.render("Time remaining: " + str(int(remaining_time)), True, (255, 0, 0))
    screen.blit(text, (100, 100))

    # Update the display window
    pygame.display.update()

    # End the timer when the remaining time reaches zero
    if remaining_time <= 0:
        running = False

# Quit Pygame when the timer ends
pygame.quit()
```

## Question 1

What does the function pygame.time.get_ticks() return in relation to the Pygame timer?

<li>The duration of the timer in milliseconds
<li>The elapsed time since Pygame was initialized in milliseconds
<li>The remaining time on the timer in milliseconds
<li>The time at which the timer will end in milliseconds

</ol>
<details>
  <summary>Answer</summary>b) The elapsed time since Pygame was initialized in milliseconds. The get_ticks() function returns the number of milliseconds that have passed since Pygame was initialized. In the context of the Pygame timer, this value is used to calculate the elapsed time since the timer was started.
</details>

---

## Question 2

How is the timer ended in the code for basic timer?

<ol type="a">
<li>By calling the pygame.quit() function
<li>By setting running to False when remaining_time is less than or equal to zero
<li>By calling the pygame.time.get_ticks() function
<li>By calling the pygame.display.set_caption() function
</ol>
<details>
  <summary>Answer</summary> b) By setting running to False when remaining_time is less than or equal to zero. This stops the main loop and ends the timer.
</details>

---

## Question 3

What is the purpose of the pygame.font.Font() function in the Pygame timer code?

<ol type="a">
<li>To import a font into Pygame
<li>To create a font object to display text on the screen
<li>To set the font size for the timer display
<li>To specify the font color for the timer display
</ol>
<details>
  <summary>Answer</summary>b) To create a font object to display text on the screen. The pygame.font.Font() function is used to create a font object that can be used to render text on the screen. In the Pygame timer code, this font object is used to display the remaining time in red on the screen.
</details>

---

## Question 4

How is the remaining time on the Pygame timer calculated?

<ol type="a">
<li>By subtracting the current time from the start time
<li>By adding the duration to the elapsed time
<li>By dividing the duration by the elapsed time
<li>By multiplying the elapsed time by the duration
</ol>
<details>
  <summary>Answer</summary> a) By subtracting the current time from the start time. The remaining time on the Pygame timer is calculated by subtracting the elapsed time (i.e., the difference between the current time and the start time) from the total duration of the timer.
</details>

---

## Question 5

How is the Pygame timer display updated in the code?

<ol type="a">
<li>By calling the pygame.time.get_ticks() function
<li>By calling the pygame.display.set_caption() function
<li>By creating a new Font object for each update
<li>By rendering the updated text onto the screen surface
</ol>
<details>
  <summary>Answer</summary>d) By rendering the updated text onto the screen surface. The Pygame timer display is updated by rendering the updated text (i.e., the remaining time on the timer) onto the screen surface using the screen.blit() method. This method takes a surface object (in this case, the text object created with the updated remaining time) and adds it to the screen at the specified coordinates.
</details>

# 5. Mini Project - Toggling between different feature v2
