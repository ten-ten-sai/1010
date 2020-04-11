#import modules
import pygame
import random

# Initialize the game engine
pygame.init()
 
#all the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (211,211,211)

# Set the height and width of the screen
SIZE = (550, 600)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("1010!")

#pygame clock
clock = pygame.time.Clock()

#font -- Dan, you might want to change it from comicssans to something else
font = pygame.font.SysFont("comicsansms", 72)

done = False
score = 0

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35
 
# This sets the margin between each cell
MARGIN = 3

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

#all the shapes
one = 

two = 2

three = 3


four = 4


five = 5

six = 6

seven = 7



shapes = []

def game_over():
	pass

def block_placement():
	pass

def clearing():
	pass

def display_score():
	global score
	 = font.render("Hello, World", True, (0, 128, 0))

class Block():
	pass


#pygame main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with bliting the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # Draw the grid
    for row in range(10):
        for column in range(10):
            colour = GREY
            #if grid[row][column] == 0:
                #colour = GREEN#
                #pass
            pygame.draw.rect(screen,colour,[(MARGIN + WIDTH) * column + MARGIN +85,
                              (MARGIN + HEIGHT) * row + MARGIN +50,WIDTH,HEIGHT])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 40 frames per second
    clock.tick(40)
 
# Close the window and quit.
pygame.quit()
