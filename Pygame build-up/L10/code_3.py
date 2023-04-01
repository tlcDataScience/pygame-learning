import pygame

# initialize pygame
pygame.init()

# set the window size
window_size = (400, 300)

# create the window
screen = pygame.display.set_mode(window_size)

# set the font for the timer
font = pygame.font.Font(None, 36)

class Timer:
    def __init__(self, initial_value):
        self.initial_value = initial_value * 1000
        self.start_time = pygame.time.get_ticks()
    
    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        return self.initial_value - elapsed_time
    
    def display(self, screen):
        timer_text = font.render(str(self.update() // 1000), True, (0, 0, 0))
        screen.fill((255,255,255))
        screen.blit(timer_text, (150, 150))

# get the initial value for the timer
initial_value = int(input("Enter the initial value for the timer (in seconds): "))

# create the timer
timer = Timer(initial_value)

# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # check if the timer has reached 0
    if timer.update() <= 0:
        running = False
    
    # display the timer
    timer.display(screen)
    
    pygame.display.update()

# quit pygame
pygame.quit()
