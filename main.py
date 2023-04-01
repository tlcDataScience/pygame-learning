import pygame
import random

# initialize pygame
pygame.init()

# initialize the screen
screen = pygame.display.set_mode((600, 400))

# set the title of the window
pygame.display.set_caption("Wordle Game")

# list of words to use in the game
words = ["python", "java", "javascript", "ruby", "go", "perl"]

# randomly select a word from the list
word = random.choice(words)

# display the length of the word as underscores
hidden_word = "_" * len(word)

# set the font for the text
font = pygame.font.Font(None, 32)

# display the initial state of the game
text = font.render(hidden_word, True, (0, 0, 0))
screen.blit(text, (200, 200))
screen.fill((255, 255, 255))

# update the screen
pygame.display.update()

# flag to check if the game is over
game_over = False

# game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # get the key that was pressed
            key = pygame.key.name(event.key)
            if key in word:
                # replace the underscores with the correct letters
                for i in range(len(word)):
                    if word[i] == key:
                        hidden_word = hidden_word[:i] + key + hidden_word[i+1:]
            else:
                # display a message if the letter is not in the word
                message = font.render("Wrong letter!", True, (255, 0, 0))
                screen.blit(message, (200, 300))
                
            # update the screen with the new state of the game
            text = font.render(hidden_word, True, (0, 0, 0))
            screen.blit(text, (200, 200))
            pygame.display.update()
            
            # check if the word has been completely guessed
            if "_" not in hidden_word:
                message = font.render("You won!", True, (0, 255, 0))
                screen.blit(message, (200, 300))
                pygame.display.update()
                game_over = True
                
# quit pygame
pygame.quit()
