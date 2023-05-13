# Table of contents

| Content              | Remark |
| -------------------- | ------ |
| 1. Objective         | ---    |
| 2. User Requirements | ---    |
| 3. Development Guide | ---    |
| 4. Enhancement       | ---    |

# 1. Objective

- Development Strategy - Agar.io
- Creating a project

# 2. User Requirements

This code is a basic game created using the Pygame library in Python. The game includes a player controlled blob that can move around the screen, a target object that randomly moves around the screen, and collision detection between the two. The objective of the game is to grow the size of the blob by colliding with the target as many times as possible.

## 2.1 User Stories

| User Story                                                                                                                              | Acceptance Criteria                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want to move the blob left when I press the 'a' key on the keyboard, so that I can avoid obstacles and collect targets.  | The blob moves left by decreasing its x position by half its radius when the 'a' key is pressed, and it stops moving when it reaches the left edge of the screen.   |
| As a player, I want to move the blob right when I press the 'd' key on the keyboard, so that I can avoid obstacles and collect targets. | The blob moves right by increasing its x position by half its radius when the 'd' key is pressed, and it stops moving when it reaches the right edge of the screen. |
| As a player, I want to move the blob up when I press the 'w' key on the keyboard, so that I can avoid obstacles and collect targets.    | The blob moves up by decreasing its y position by half its radius when the 'w' key is pressed, and it stops moving when it reaches the top edge of the screen.      |
| As a player, I want to move the blob down when I press the 's' key on the keyboard, so that I can avoid obstacles and collect targets.  | The blob moves down by increasing its y position by half its radius when the 's' key is pressed, and it stops moving when it reaches the bottom edge of the screen. |
| As a player, I want the blob to grow when it collides with a target, so that I can reach a larger size and score more points.           | When the blob collides with a target, the target disappears and a new random target appears on the screen, and the blob's radius increases by 10.                   |
| As a player, I want to see my current size displayed on the screen, so that I can track my progress.                                    | The current size of the blob is displayed in the top left corner of the screen, and it updates in real time as the blob grows.                                      |
| As a player, I want to be able to quit the game by pressing the 'q' key on the keyboard, so that I can stop playing.                    | When the 'q' key is pressed, the game window closes and the program exits.                                                                                          |

## 2.2 Personas

### 2.2.1 Persona 1: Software Intern

**Name:** Alex

**Age:** 25

**Occupation:** Software Developer Intern

**Background:**

Alex is a software developer Intern who works remotely. As a work-from-home employee, he spends most of his time sitting in front of his computer. He likes to take breaks every few hours to refresh his mind and stretch his body. He is always looking for simple and entertaining games to play during his breaks.

**Goals:**

- To have fun and relax during breaks.
- To improve his hand-eye coordination.

**Challenges:**

Limited time to play games.
Wants games that can be played quickly and easily.

**How the game meets the persona's needs:**

- The game is simple and easy to understand, making it quick to start and play.
- The game requires hand-eye coordination, helping Alex to improve his skills.
- The game can be played in short bursts, making it perfect for Alex's limited break time.
- The game is entertaining and helps Alex relax during his breaks.

# 3. Development Guide

## 3.1 Screen

The screen will be a full-screen window with a black background. In the center of the screen, there will be a red circle representing the player's blob, which will grow in size as the player collects targets. The targets will be green circles that appear randomly on the screen. In the upper-left corner of the screen, there will be a white box displaying the size of the player's blob in real-time. The game can be quit by pressing the 'q' key. The player will move the blob using the 'w', 'a', 's', and 'd' keys on the keyboard.

## 3.2 Behaviour

The code represents a simple game where the player controls a red circle (the "blob") with arrow keys on their keyboard. The objective of the game is to touch a green circle (the "target") with the blob, which will cause the blob to grow in size. The target will then randomly relocate somewhere else on the screen, and the player must move the blob to touch it again to continue growing.

The player can quit the game at any time by pressing the "q" key on their keyboard. Additionally, the player can move the blob left, right, up, or down using the arrow keys. The blob will not move past the edges of the screen, which are marked by a small padding around the perimeter.

The game is rendered using the Pygame library in Python, with the size of the window dynamically set based on the size of the user's screen. The game loop is set to run at 60 frames per second, and the clock.tick(60) function is called to ensure that the game runs smoothly.

The user interface of the game includes a label in the top left corner of the screen that displays the current size of the blob. When the blob collides with the target, the target will randomly relocate to a new location on the screen, and the size of the blob will increase. If the blob collides with the edge of the screen or any other objects, nothing will happen.

## 3.3 Concepts

The coding concepts needed for this game include:

1.  **Pygame library:**

    Pygame is a set of Python modules designed for writing video games. It provides functionality for graphics, sound, user input, and timing.

2.  **Object-oriented programming:**

    The game is built using object-oriented programming (OOP) concepts. OOP allows us to create classes, which act as blueprints for creating objects. Each object has its own properties (attributes) and actions (methods).

3.  **Random module:**

    The game uses the random module to generate random positions for the target.

4.  **Event handling:**

    The game handles events such as key presses using the Pygame event loop. The event loop listens for events and responds accordingly.

5.  **Collision detection:**

    The game detects collisions between the player blob and the target using a simple distance formula. 6. **Rendering:** The game renders graphics to the screen using Pygame's rendering functions.

6.  **Control flow:**

    The game uses control flow statements such as if-else statements to control the logic of the game.

## 3.4 Code

[Replit Code V1](https://replit.com/@tlcDataScience/AgarioV1#main.py)

# 4. Enhancement

| User Story                                                                                                   | Acceptance Criteria                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a player, I want to be able to move my blob continuously, so that I can explore the game world with ease. | 1. The blob can move continuously in any direction without stopping. <br> 2. The blob should not move outside the game window. <br> 3. The player should be able to move the blob using either the arrow keys or the 'w', 'a', 's', and 'd' keys. |

[Replit Code V2](https://replit.com/@tlcDataScience/AgarioV2#main.py)

| User Story                                                                               | Acceptance Criteria                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| As a player, I want to be able to have bombs around the map to make it more challenging. | 1. It will be gameover when colliding with the blob. |

[Replit Code V3](https://replit.com/@tlcDataScience/AgarioV3#main.py)
