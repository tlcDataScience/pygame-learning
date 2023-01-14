# Adding Images

# Importing the library
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

IMAGE = 'Cute Cat.png'  # This is the image used in the exercise 

class Cat():

    def __init__(self, x=0, y=0, PADDING=0):
        self.image = IMAGE
        picture1 = pygame.image.load(IMAGE)
        self.image1 = pygame.transform.scale(picture1,(PADDING*2, PADDING*2))
        self.imageRect1 = self.image1.get_rect(center=(x,y))

# This is the main driver code
def main():
    
    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (107, 206, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    PADDING = 20

    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_a:
                    if w > PADDING:
                        w = w - 10
                if event.key == pygame.K_d:
                    if w < WINDOW_WIDTH-PADDING:
                        w = w + 10
                if event.key == pygame.K_w:
                    if h > PADDING:
                        h = h - 10
                if event.key == pygame.K_s:
                    if h < WINDOW_HEIGHT-PADDING:
                            h = h + 10

        cat1 = Cat(w,h, PADDING) # Move to the left 

        WINDOW.blit(cat1.image1, cat1.imageRect1)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()