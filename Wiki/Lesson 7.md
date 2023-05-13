# Table of contents

| Content             | Remark                 |
| ------------------- | ---------------------- |
| 1. Objective        | ---                    |
| 2. Recap            | ---                    |
| 3. Lesson           | ---                    |
| 4. Review Questions | To check understanding |
| 5. Mini Project     | Bonus Task             |

# 1. Objective

- Inserting Images

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

Here are some questions

- Explain what Pygame is?
- What benefits are there in using variables instead of hardcoding values when working with Pygame?
- How to add keybaord inputs?
- How do you change the dimensions of the window in the previous code?
- How do you change the background color?

# 3. Lesson

## 3.1 Opening an Image in Pygame

[Cute Cat](https://github.com/tlcDataScience/pygame-learning/blob/main/Pygame%20build-up/L7/Cute%20Cat.png)

### Sample Code

```python
import pygame

# Initialize Pygame
pygame.init()

# Load an image using Pygame
image = pygame.image.load("Cute Cat.png")

# Set the window size to match the size of the image
window_size = (image.get_width(), image.get_height())

# Create the window
window = pygame.display.set_mode(window_size)

# Display the image in the window
window.blit(image, (0, 0))
pygame.display.update()

# Set up the clock to control the frame rate
clock = pygame.time.Clock()
frame_rate = 60

# Wait for the user to close the window
running = True
while running:

    # Control the frame rate of the program
    clock.tick(frame_rate)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
```

### Explanation

`import pygame`

This line imports the Pygame library, which is a set of modules designed for game development.

`pygame.init()`

This line initializes Pygame and sets up its necessary subsystems.

`image = pygame.image.load("Cute Cat.png")`

This line loads an image file named "Cute Cat.png" using Pygame's image module and stores it in the variable `image`.

`window_size = (image.get_width(), image.get_height())`

This line creates a tuple of the width and height of the loaded image using the `get_width()` and `get_height()` methods of the `image` object, and stores it in the variable `window_size`.

`window = pygame.display.set_mode(window_size)`

This line creates a new display window with a size of `window_size` using the `set_mode()` method of the `display` module, and stores it in the variable `window`.

`window.blit(image, (0, 0))`

This line draws the `image` onto the `window` at the position `(0,0)` using the `blit()` method of the `Surface` object.

`pygame.display.update()`

This line updates the display to show the image that was just drawn using the `update()` method of the `display` module.

`clock = pygame.time.Clock()
frame_rate = 60`

These two lines create a Pygame clock object and set the frame rate to 60 frames per second.

`running = True
while running:`

This line initializes a boolean variable `running` as `True` and starts a while loop that will run as long as `running` is `True`.

## 3.2 Inserting image in Pygame

### Sample Code

```python
# Adding Images

# Importing the library
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

IMAGE = 'Cute Cat.png'  # This is the image used in the exercise

class Cat():

    def __init__(self, x=0, y=0):
        self.image = IMAGE
        picture1 = pygame.image.load(IMAGE)
        self.image1 = pygame.transform.scale(picture1,(100, 100))
        self.imageRect1 = self.image1.get_rect(center=(x,y))

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (107, 206, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                run = False

        cat1 = Cat(w-100,h) # Move to the left

        WINDOW.blit(cat1.image1, cat1.imageRect1)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

### Explanation

This code imports the Pygame library, sets up the game window, loads the image to display, scales the image to the desired size, defines the position of the image, and displays the image on the screen. It then runs the game loop, which updates the display and waits for the user to close the window.

## Step by Step

1.  Import the Pygame library at the beginning of your script:

    `import pygame`

2.  Load the image you want to display using the `pygame.image.load()` function:

    IMAGE = 'path/to/image.png'
    picture = pygame.image.load(IMAGE)

3.  Scale the image to the desired size using the `pygame.transform.scale()` function:

    scaled_picture = pygame.transform.scale(picture, (100, 100))

    In this example, the image is scaled to 100x100 pixels.

4.  Create an object to hold the image, such as a class:

    ```python
    class Cat():

        def __init__(self, x=0, y=0):
            self.image = IMAGE
            picture1 = pygame.image.load(IMAGE)
            self.image1 = pygame.transform.scale(picture1,(100, 100))
            self.imageRect1 = self.image1.get_rect(center=(x,y))
    ```

    In this example, the `Cat` class is created to hold the image, and the `__init__()` method is used to load the image and scale it to the desired size.

5.  Display the image on the Pygame window using the `blit()` function:

    ```python
    WINDOW.blit(cat1.image1, cat1.imageRect1)
    ```

    In this example, the image is displayed on the window using the `cat1.image1` and `cat1.imageRect1` attributes of the `Cat` object.

6.  Update the Pygame window to show the image using the `pygame.display.flip()` function:

    ```python
    pygame.display.flip()
    ```

7.  Run the game loop to keep the Pygame window open:

    ```python
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()
    ```

    This loop keeps the window open until the user closes it.

With these steps, you should be able to add an image to your Pygame window.

## 3.3 Controlling the position of image

### Sample Code

```python
# Importing the library
import pygame

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
PADDING = 20
BACKGROUND = (107, 206, 255)
IMAGE = 'Cute Cat.png'

class Cat():
    def __init__(self, x=0, y=0):
        picture = pygame.image.load(IMAGE)
        self.image = pygame.transform.scale(picture, (PADDING*2, PADDING*2))
        self.rect = self.image.get_rect(center=(x, y))

def game_loop():
    clock = pygame.time.Clock()
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2
    cat1 = Cat(w, h)

    run = True
    while run:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_a and w > PADDING:
                    w -= 10
                elif event.key == pygame.K_d and w < WINDOW_WIDTH-PADDING:
                    w += 10
                elif event.key == pygame.K_w and h > PADDING:
                    h -= 10
                elif event.key == pygame.K_s and h < WINDOW_HEIGHT-PADDING:
                    h += 10

        cat1.rect.center = (w, h)

        # Draw
        window.fill(BACKGROUND)
        window.blit(cat1.image, cat1.rect)
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
```

## Explanation

The first section of the code imports the pygame library and defines some constants that will be used throughout the program. The WINDOW_WIDTH and WINDOW_HEIGHT constants define the size of the game window, PADDING defines the size of the cat image, BACKGROUND defines the color of the background, and IMAGE is the filename of the cat image.

The next section of the code defines a Cat class that encapsulates the cat image and its position. The **init** method loads the cat image and scales it to the appropriate size using pygame.transform.scale(). It then creates a Rect object that represents the cat's position on the screen using the get_rect() method and sets its center to the specified coordinates (x, y).

The next section of the code defines the game_loop() function, which is the main driver code for the game. It creates a clock object using `pygame.time.Clock()` and initializes the pygame library using pygame.init(). It then creates a game window using pygame.display.set_mode() and sets the width and height of the window using the `WINDOW_WIDTH` and `WINDOW_HEIGHT` constants.

The w and h variables are initialized to the center of the screen, and a Cat object named cat1 is created at that position. The run variable is set to True to start the game loop.

Inside the game loop, the code handles events using pygame.event.get(). If the q key is pressed, the run variable is set to False to exit the loop. If the a, d, w, or s keys are pressed, the w and h variables are updated to move the cat image left, right, up, or down,

## Step-by-step

1. Import the necessary library: `pygame`.
2. Define the window dimensions `WINDOW_WIDTH` and `WINDOW_HEIGHT`.
3. Define the image path `IMAGE` and create a Cat class to represent the cat image.
4. In the Cat class, define an `__init__ ` method to initialize the cat object's attributes x, y, and PADDING.
5. In the **init** method, load the image using pygame.image.load() and scale it using `pygame.transform.scale()`. Assign the scaled image to the image1 attribute.
6. In the **init** method, get the rectangle of the image1 attribute using get_rect() method and assign it to the imageRect1 attribute.
7. Define a main function to handle the game loop.
8. Initialize Pygame and set the window dimensions using `pygame.display.set_mode()`.
9. Set the background color for the window using BACKGROUND variable.
10. Set the initial cat position to the center of the window by dividing the `WINDOW_WIDTH` and `WINDOW_HEIGHT` by 2 and assigning them to w and h variables respectively.
11. Define a PADDING variable to determine the padding around the cat image.
12. Start the game loop using a while loop.
13. Fill the window with the background color using `WINDOW.fill(BACKGROUND)`.
14. Get user inputs using a for loop for each event in pygame.event.get().
15. If the q key is pressed, set run variable to False to break out of the game loop.
16. If the a key is pressed and the cat position is greater than the padding, move the cat 10 pixels to the left by decreasing the w variable by 10.
17. If the d key is pressed and the cat position is less than the window width minus the padding, move the cat 10 pixels to the right by increasing the w variable by 10.
18. If the w key is pressed and the cat position is greater than the padding, move the cat 10 pixels up by decreasing the h variable by 10.
19. If the s key is pressed and the cat position is less than the window height minus the padding, move the cat 10 pixels down by increasing the h variable by 10.
20. Create a new Cat object with the updated w, h, and PADDING variables.
21. Blit the cat image onto the window using `WINDOW.blit(cat1.image1, cat1.imageRect1).`
22. Update the display using pygame.display.flip().
23. Set the clock to tick at 60 frames per second using `clock.tick(60)`.
24. Call the main() function to run the game loop.

# 4. Review Question

## Question 1

What does pygame.image.load() function do?

<ol type="a">
<li>Loads an image from a file into a Pygame Surface
<li>Saves an image to a file from a Pygame Surface
<li>Creates a new empty Pygame Surface
<li>Deletes an existing Pygame Surface
</ol>
<details>
  <summary>Answer</summary>
  A) Loads an image from a file into a Pygame Surface
Explanation: The pygame.image.load() function is used to load an image from a file into a Pygame Surface object.
  </details>
  
---

## Question 2

What is a Surface object in Pygame?

<ol type="a">
<li>A window that displays the game
<li>A container for images in Pygame
<li>A type of sprite in Pygame
<li>A module that handles sound in Pygame
</ol>

<details>
  <summary>Answer</summary>
  B) A container for images in Pygame
Explanation: A Surface object in Pygame is a container for images. It provides methods for drawing and manipulating images.
  </details>

---

## Question 3

What is the purpose of the Pygame function pygame.quit()?

<ol type="a">
<li>Closes the Pygame library and quits the game.
<li>Pauses the game until a key is pressed.
<li>Restarts the game from the beginning.
<li>Saves the game state to a file.
</ol>
<details>
  <summary>Answer</summary>
  A) Closes the Pygame library and quits the game.
Explanation: The pygame.quit() function is used for closing the Pygame library and quitting the game. It should be called at the end of the game loop to properly shut down the Pygame library and free up system resources.
  </details>

---

## Question 4

What is the difference between a Pygame Surface and a Pygame Rect?

<ol type="a">
<li>A Surface is a container for images, while a Rect is a graphical element that can be animated and moved on a Surface.
<li>A Surface is a type of sprite that can be animated and moved, while a Rect is a container for images.
<li>A Surface is a module that handles sound in Pygame, while a Rect is a module that handles images.
<li>A Rect is an object that defines a rectangular area on a Surface.
</ol>

<details>
  <summary>Answer</summary>D) A Rect is an object that defines a rectangular area on a Surface.
Explanation: A Pygame Rect object is an object that defines a rectangular area on a Surface. It is used for specifying the position and size of images and sprites on a Surface. A Surface is a container for images, and does not have the same positioning and sizing capabilities as a Rect.
  </details>

---

## Question 5

What is the Pygame function pygame.display.set_mode() used for?

<ol type="a">
<li>Creating a game window for display.
<li>Creating a new Pygame Surface object.
<li>Loading an image from a file into a Pygame Surface object.
<li>Playing a sound effect or music.
</ol>

<details>
  <summary>Answer</summary> A) Creating a game window for display.
Explanation: The pygame.display.set_mode() function is used for creating a game window for display. It takes a tuple as an argument that specifies the size of the window and returns a Surface object that represents the game window.
  </details>

# 5. Mini Project - Toggling between different images

Enhance the code above by trying the following;

- Toggling between different images
