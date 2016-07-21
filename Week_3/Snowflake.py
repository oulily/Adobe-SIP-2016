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

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

class SnowFlake():

    def __init__(self, size, x_pos, y_pos, x_speed, y_speed):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def fall(self):
        self.y_pos += self.y_speed
        
        
    def draw(self):
        pygame.draw.circle(screen, WHITE, [self.x_pos, self.y_pos], self.size)
        
        
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#INITIALIZE YOUR SNOWFLAKE HERE! 
for i in range(10):
    rand_x_pos = random.randint(0, 500)
    rand_size = random.randint(5, 10)
    rand_y_speed = random.randint(0, 5)
    rand_x_speed = random.randint(0, 5)
    snowflake_1 = SnowFlake(rand_size, rand_x_pos, 0, rand_x_speed, rand_y_speed)

# Snow List
snow_list = []


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
    screen.fill(BLUE)

    # --- Drawing code should go here
    # Begin Snow
        snowflake_1.fall()
        snowflake_1.draw()
    



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
