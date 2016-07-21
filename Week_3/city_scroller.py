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
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREY = (129, 129, 129)
# colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# # initialize the pygame class
# pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# # Set the title of the window
# pygame.display.set_caption("CityScroller")

# # Loop until the user clicks the close button.
# done = False

# Used to manage how fast the screen updates
# clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x += speed


class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.build_list = []
        self.combined_width = 0

    def create_buildings(self):
        #until buildings fill >= width of scroller
            #call create_building
        while self.combined_width <= self.width:
            self.create_building(self.combined_width)
        """
        Will call create_building until there the buildings fill up the width of the
        scroller.
        """
        
    def create_building(self, x_location):
        width = random.randint(50, 100)
        self.combined_width += width
        building1 = Building(x_location, self.height, width, random.randint(-200, -80),  self.color)
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        self.build_list.append(building1)

    def draw_buildings(self):
        for building in self.build_list:
            building.draw()

    
        """
        This calls the draw method on each building.
        """

    def move_buildings(self):
        for building in self.build_list:
            building.move(self.speed)

        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        if self.build_list[-1].x > SCREEN_WIDTH:
            self.build_list.remove(self.build_list[-1])
        if self.build_list[0].x > 0:
            width = random.randint(20, 60)
            x_location = self.build_list[0].x - width
            building = Building(x_location, self.height, width, random.randint(-300, -90),  self.color)
            self.build_list.insert(0, building)



# FRONT_SCROLLER_COLOR = (0,0,30)
# MIDDLE_SCROLLER_COLOR = (30,30,100)
# BACK_SCROLLER_COLOR = (50,50,150)
# BACKGROUND_COLOR = (17, 9, 89)

# front_scroller = Scroller(SCREEN_WIDTH, 475, (SCREEN_HEIGHT - 50), FRONT_SCROLLER_COLOR, 1.5)
# middle_scroller = Scroller(SCREEN_WIDTH, 425, (SCREEN_HEIGHT - 100), MIDDLE_SCROLLER_COLOR, 1)
# back_scroller = Scroller(SCREEN_WIDTH, 375, (SCREEN_HEIGHT - 150), BACK_SCROLLER_COLOR, 0.5)

# back_scroller.create_buildings()
# middle_scroller.create_buildings()
# front_scroller.create_buildings()
# # -------- Main Program Loop -----------
# while not done:
#     # --- Main event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     # --- Game logic should go here

#     # --- Screen-clearing code goes here

#     # Here, we clear the screen to white. Don't put other drawing commands
#     # above this, or they will be erased with this command.

#     # If you want a background image, replace this clear with blit'ing the
#     # background image.
#     screen.fill(BACKGROUND_COLOR)

#     # --- Drawing code should go here

#     # street
#     # Rect(left, top, width, height) -> Rect
#     pygame.draw.rect(screen, BLACK,(0, 475, 800, 125))
#     pygame.draw.rect(screen, WHITE,(20, 530, 65, 8))

#     back_scroller.draw_buildings()
#     back_scroller.move_buildings()

#     middle_scroller.draw_buildings()
#     middle_scroller.move_buildings()
 
#     front_scroller.draw_buildings()
#     front_scroller.move_buildings()

#     # --- Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

#     # --- Limit to 60 frames per second
#     clock.tick(60)

# # Close the window and quit.
# pygame.quit()
# exit() # Needed when using IDLE
