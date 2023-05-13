# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# 1. Objective

- Development Strategy
- Countdown Transition

# 2. User Requirements

A digital countdown is a timer that displays the amount of time left until an event or deadline. It is often used in a variety of settings, such as in sporting events, academic exams, or in cooking and baking to ensure that food is cooked for the appropriate amount of time. A digital countdown can also be used as a visual aid to keep track of time and to create a sense of urgency. With the help of technology, digital countdowns can be easily created and customized to suit different needs and applications. They can be displayed on a variety of devices, including smartphones, computers, and specialized timers, making them a versatile and useful tool in many different contexts.

# 3. Development Guide

## 3.1 Screen

The screen for the digital countdown should display the remaining time in a clear and easy-to-read format. Here's an example of how the screen could look like.

The top of the screen could display a title such as "COUNTDOWN TIMER". The remaining time could be displayed in the center of the screen using a large font size with leading zeros for minutes and seconds. The background color of the screen could be black to provide high contrast against the white text, and the font color could be white for maximum visibility. Depending on the enhancements made to the project, additional elements such as progress bars or animations could be added to the screen.

## 3.2 Behaviour

The expected behavior of the digital countdown code is to display a countdown timer on the screen, starting from a predetermined time and counting down to zero. The time is displayed in minutes and seconds format with leading zeros, i.e. "05:30" for five minutes and thirty seconds.

The program initializes the Pygame module and sets up a full-screen window with a caption of "Countdown". It defines the colors black and white and sets up a font to be used for rendering text. The starting time is defined in seconds, and the countdown start time is set using the time module.

The program then enters a main game loop, where it calculates the elapsed time since the start of the countdown, subtracts it from the starting time, and displays the remaining time on the screen in the format of minutes and seconds with leading zeros. If the countdown reaches zero, the program exits the main loop and quits Pygame.

During the countdown, the program updates the display every second, by filling the screen with black, rendering the remaining time text using the previously defined font, centering it on the screen, and blitting it onto the window. Finally, the program pauses for one second using the time module.

## 3.3 Timer

### 3.3.1 Sample Code written without using Classes

https://replit.com/@tlcDataScience/DigitalCountdown#main.py

### 3.3.2 Explanation

Sure, here are some instructions to create the digital countdown using Pygame:

1. Import Pygame and Time: Once Pygame is installed, you need to import it at the beginning of your code. You also need to import the Time module, which provides access to the system clock, which you will use to keep track of the time remaining in the countdown.

```python
import pygame
import time
```

2. Initialize Pygame: Before you can use Pygame, you need to initialize it by calling the pygame.init() function.

```python
pygame.init()
```

3. Set up the window display: To create the window for the countdown, you need to define the size of the window and set its caption. You can use the pygame.display.Info() function to get the size of the user's screen and then create a window that fills the screen using the pygame.display.set_mode() function.

```python
infoObject = pygame.display.Info()
window_width = infoObject.current_w
window_height = infoObject.current_h
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
pygame.display.set_caption('Countdown')
```

4. Define the colors and font: To display the countdown timer, you will need to define some colors and choose a font. You can use the RGB color model to define colors as tuples of three integers ranging from 0 to 255.

```python
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 100)
```

5. Define the starting time and countdown start time: You need to define the starting time in seconds for the countdown and the time at which the countdown should start. You can use the time.time() function to get the current time in seconds.

```python
time_left = 10
start_time = time.time()
```

6. Create the main game loop: To run the countdown timer, you will need to create a main game loop that will update the display and pause for one second in each iteration. The loop should continue until the time_left variable becomes zero or negative.
   python

```python
running = True
while running:
    # main game loop code goes here
```

7. Calculate the time remaining: In each iteration of the loop, you need to calculate the time remaining in the countdown by subtracting the elapsed time from the starting time. You can use the time.time() function to get the current time and then subtract the start_time from it to get the elapsed time.

```python
elapsed_time = time.time() - start_time
time_left = max(0, 10 - int(elapsed_time))
```

8. Clear the window and render the text: In each iteration of the loop, you need to clear the window, render the time remaining as text using the Pygame font, center the text in the window, and update the display.

```python
window.fill(black)
minutes = time_left // 60
seconds = time_left % 60
time_str = "{:02d}:{:02d}".format(minutes, seconds)
text = font.render(time_str, True, white)
text_rect = text.get_rect(center=(window_width/2, window_height/2))
window.blit(text, text_rect)
pygame.display.update()
```

# 4. Enhancement

There are several enhancements that could be made to this project to improve its functionality and user experience. Using Classes & creating new screen, you're to enhance the existing code.

1. Allow the user to set the countdown time: Currently, the countdown time is hard-coded in the program. To make the program more flexible and customizable, it could be modified to prompt the user to input the desired countdown time.

2. Add a pause/resume feature: Adding the ability to pause and resume the countdown would make the program more useful in real-world situations where interruptions may occur.

3. Add a visual indicator for progress: A progress bar or a visual indicator that shows the progress of the countdown could make it easier for the user to quickly gauge how much time is left.
