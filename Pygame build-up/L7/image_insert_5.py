# Adding Images
import pygame

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
ORANGE = (255, 184, 107)
DARK_GREEN = (44, 66, 47)
BROWN = (117, 80, 27)

# The main game loop

image = 'Cute Cat.png'

class Cat():

    def __init__(self, x=0, y=0, PADDING=0):
        self.image = image
        picture1 = pygame.image.load(image)
        self.image1 = pygame.transform.scale(picture1,(PADDING*2, PADDING*2))
        self.imageRect1 = self.image1.get_rect(center=(x,y))
        

def main():
    
    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (107, 206, 255)

    run = True

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2

    PADDING = 30

    catList = []

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
                if event.key == pygame.K_p:
                    catList.append(Cat(w,h, PADDING))
                print(f'({w}, {h})')

        # Pasted 
        for i in range(len(catList)):
            WINDOW.blit(catList[i].image1, catList[i].imageRect1)
            
        # Cursor
        cat1 = Cat(w,h,PADDING) 
        WINDOW.blit(cat1.image1, cat1.imageRect1)



        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()