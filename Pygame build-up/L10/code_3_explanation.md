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
