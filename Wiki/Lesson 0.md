# Replit - Online IDE

## Create an account

- https://replit.com/

<img width="1400" alt="image" src="https://user-images.githubusercontent.com/102406967/224486180-dbe1e2ac-51c1-4348-ad51-9512d24b7b89.png">

## Create a new replit

- Create new replit
- Use a pygame template

<img width="1400" alt="image" src="https://user-images.githubusercontent.com/102406967/224486112-bf79eabf-4061-4226-8889-5ff8be9a24b2.png">

# Local Setup

## Setting up

Download Visual Studio Code  
https://code.visualstudio.com/download

Download Python3  
https://www.python.org/downloads/

Once downloaded, open Visual Studio Code. Within Visual Studio Code navigate to a working folder & create a main.py as the file name. Inside `main.py` you may copy the following code

```python
print("Hello World")
```

To run the python file, go to terminal & run `python3 main.py` or `py main.py`

To download Pygame, go to terminal & run `pip3 install pygame`

# Sample Pygame

You may now run a sample Pygame code - Hello World

<img width="391" alt="image" src="https://user-images.githubusercontent.com/102406967/224486567-08d0c392-1b16-42bc-bddf-e63b887ddf7b.png">
<br>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, World!", 1, (0, 0, 0))
    screen.blit(text, (100, 150))
    pygame.display.update()

pygame.quit()
```
