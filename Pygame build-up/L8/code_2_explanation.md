Using Functional Programming

Here is a basic example of how you can use Pygame to switch between screens:

1. Import the Pygame library

```python
import pygame
```

2. Initialize the Pygame library and create a display window

```python
pygame.init()
screen = pygame.display.set_mode((800, 600))
```

3. Define a function for each screen you want to create. Each function should include all the necessary Pygame code to display that screen. For example:

```python
def menu_screen():
    # Code for displaying the menu screen goes here
    pass

def game_screen():
    # Code for displaying the game screen goes here
    pass

def game_over_screen():
    # Code for displaying the game over screen goes here
    pass
```

4. Create a variable to keep track of which screen is currently being displayed. For example:

```python
current_screen = "menu"
```

5. In the main game loop, use an if-elif statement to call the appropriate function for the current screen. For example:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_screen == "menu":
        menu_screen()
    elif current_screen == "game":
        game_screen()
    elif current_screen == "game_over":
        game_over_screen()

    pygame.display.update()
```

6. To switch between screens, simply change the value of the current_screen variable. For example:

```python
if current_screen == "menu" and user_clicks_start_button:
    current_screen = "game"

if player_loses_game:
    current_screen = "game_over"
```

7. Don't forget to quit Pygame when the game loop ends

```python
pygame.quit()
```
