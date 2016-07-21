
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
game_over = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE






# -------- Main Program Loop -----------

circle_x = 350
circle_y = 250

speed_x = random.randint(-10, 10)
speed_y = random.randint(-10, 10)

circle_dir = [-1, 1]
rand_dir = random.randint(0, 1)

circle_size = random.randint(20, 80)

color = [BLACK, WHITE, GREEN, RED, BLUE, GREY]
while not game_over:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
           


    # --- Drawing code should go here
    
    
    screen.fill(GREEN)
    rand_color = random.randint(0, 5)    
    pygame.draw.circle(screen, color[rand_color], [circle_x, circle_y], circle_size, 0)
    
    circle_x += speed_x * circle_dir[rand_dir]
    circle_y += speed_y * circle_dir[rand_dir]
    
    if circle_x > 700 - circle_size:
        speed_x = -speed_x

    if circle_x < 0 + circle_size:
        speed_x = -speed_x

    if circle_y > 500 - circle_size:
        speed_y = -speed_y

    if circle_y < 0 + circle_size:
        speed_y = -speed_y
    
            

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
