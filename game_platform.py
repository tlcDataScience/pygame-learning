import pygame
import sys

class Player:
    def __init__(self, x, y):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.velocity = 5
        self.jump_height = 10
        self.gravity = 1

    def move_left(self):
        self.x -= self.velocity

    def move_right(self):
        self.x += self.velocity

    def jump(self):
        self.y -= self.jump_height

    def apply_gravity(self):
        if self.y < HEIGHT - self.height - 10:
            self.y += self.gravity
        else:
            self.y = HEIGHT - self.height - 10

    def draw(self):
        pygame.draw.rect(WINDOW, (0, 0, 255), (self.x, self.y, self.width, self.height))

class Platform:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(WINDOW, (0, 255, 0), (self.x, self.y, self.width, self.height))

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Simple Platformer")

# Colors
WHITE = (255, 255, 255)

# Create player
player = Player(WIDTH // 2 - 25, HEIGHT - 60)

# Create multiple platforms
platforms = [
    Platform(50, HEIGHT - 100, 200, 20),
    Platform(300, HEIGHT - 150, 150, 20),
    Platform(600, HEIGHT - 200, 200, 20),
    # Add more platforms as needed
]

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.jump()

    player.apply_gravity()

    # Check for collision with platforms
    for platform in platforms:
        if (player.x < platform.x + platform.width and 
            player.x + player.width > platform.x and 
            player.y + player.height > platform.y and 
            player.y < platform.y + platform.height):
            player.y = platform.y - player.height

    # Draw everything
    WINDOW.fill(WHITE)
    for platform in platforms:
        platform.draw()
    player.draw()
    pygame.display.update()

    clock.tick(FPS)
