import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

# lets start this background with a non black-white color
window.fill((0, 80, 0))

running = True  # loop control variable(for the game loop)

# At each moment the mouse coordinates are known.
# We can get get access to these through the get_pos() function
# or like so:  event.pos
# This is in fact a very important feature since it marks a
# foundation for interaction between the mouse and various "objects"
# of our game.
# In this example we are going to draw a filled (poison)green circle
# with the center at the mouse position.  We are also going to print
# the coordinates to the Python console as a pre formatted string
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #window.fill((0, 80, 0))     # Try commenting this out and see what happens.
            pygame.draw.circle(window, (0, 255, 0), event.pos, 20, 0)
    pygame.display.flip()

pygame.quit()