import pygame

# Initialize Pygame
pygame.init()

# Set the window size
win_size = (400, 400)

# Create a window
screen = pygame.display.set_mode(win_size)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Draw the game board
def draw_board():
    pygame.draw.line(screen, black, [0, 133], [400, 133], 2)
    pygame.draw.line(screen, black, [0, 266], [400, 266], 2)
    pygame.draw.line(screen, black, [133, 0], [133, 400], 2)
    pygame.draw.line(screen, black, [266, 0], [266, 400], 2)

# Check if a player has won
def check_win(board):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True

    return False

# Initialize the game board
board = [["" for i in range(3)] for j in range(3)]

# Set the font
font = pygame.font.SysFont("comicsansms", 72)

# Set the player turn
turn = "X"

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // 133, pos[0] // 133

            if board[row][col] == "":
                board[row][col] = turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"

    screen.fill(white)
    
    if check_win(board):
        text = font.render("Player " + turn + " wins!", True, black)
        screen.blit(text, [50, 50])
        pygame.display.update()
        
    else:
        draw_board()

        for row in range(3):
            for col in range(3):
                text = font.render(board[row][col], True, black)
                screen.blit(text, [(col * 133) + 50, (row * 133) + 50])
    
    pygame.display.update()

    
