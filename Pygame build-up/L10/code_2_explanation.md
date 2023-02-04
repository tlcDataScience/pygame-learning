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
