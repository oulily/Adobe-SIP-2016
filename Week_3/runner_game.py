from city_scroller import Scroller
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
LIGHTYELLOW = (255, 255, 100)
colors = [BLACK, GREEN, BLUE, RED]

# def random_color():
#     return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
# pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# road
def white_line(rect_x):
    pygame.draw.rect(screen, WHITE, (rect_x, 540, 60, 7))


#Character
class RunnerSprite(pygame.sprite.Sprite):

    def __init__(self, color, size, width, height, position):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = size
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = position)

    def update(self, sprite_x, sprite_y):
        self.rect = self.image.get_rect(x = sprite_x + 5)


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 475, (SCREEN_HEIGHT - 50), FRONT_SCROLLER_COLOR, 1.5)
middle_scroller = Scroller(SCREEN_WIDTH, 425, (SCREEN_HEIGHT - 100), MIDDLE_SCROLLER_COLOR, 1)
back_scroller = Scroller(SCREEN_WIDTH, 375, (SCREEN_HEIGHT - 150), BACK_SCROLLER_COLOR, 0.5)

back_scroller.create_buildings()
middle_scroller.create_buildings()
front_scroller.create_buildings()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    #RUNNER
    player1 = RunnerSprite(GREY, 50, 50, 50, pygame.mouse.get_pos())
    goodsprite1 = RunnerSprite(GREY, 50, 50, 50, (random.randint(0, 800), random.randint(0, 600)))
    goodsprite2 = RunnerSprite(GREY, 50, 50, 50, (random.randint(0, 800), random.randint(0, 600)))
    goodsprite3 = RunnerSprite(GREY, 50, 50, 50, (random.randint(0, 800), random.randint(0, 600)))

    # List of all sprites
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player1, goodsprite1, goodsprite2, goodsprite3)
    good_sprites_list = pygame.sprite.Group()
    good_sprites_list.add(goodsprite1, goodsprite2, goodsprite3)

    # moon
    pygame.draw.circle(screen, LIGHTYELLOW, (725, 75), 50)
    # street
    pygame.draw.rect(screen, BLACK, (0, 475, 800, 125))
    for i in range(10):
        white_line(20 + 105 *i)
    # curb
    pygame.draw.rect(screen, (238, 221, 130), (0, 475, 800, 8))

    #drawing scrollers
    back_scroller.draw_buildings()
    back_scroller.move_buildings()

    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
 
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

    #drawing sprites
    all_sprites_list.draw(screen)
    good_sprites_list.update(random.randint(0, 800), random.randint(0, 600))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE