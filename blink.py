import pygame
from pygame.locals import *
import random

pygame.init()

window = pygame.display.set_mode((600, 600))
window.fill((0, 0, 0))

# Initialize the position of the rectangles
rect1_x, rect1_y = 100, 100
rect2_x, rect2_y = 100, 400

# Movement direction for the rectangles
rect1_direction = 1  # 1 for down, -1 for up
rect2_direction = -1  # -1 for up, 1 for down

# Main game loop
while True:  # Outer loop to repeat animation indefinitely
    # Generate random duration for the pause
    rand = random.randint(2, 6)  # randint() for generating random integers within a range
    print(rand)

    # Reset initial positions
    rect1_y, rect2_y = 100, 400
    rect1_direction = 1
    rect2_direction = -1

    while rect1_y >= 0 or rect2_y <= 600:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        # Move the rectangles
        rect1_y += 5 * rect1_direction
        rect2_y += 5 * rect2_direction

        # Fill the screen with black
        window.fill((0, 0, 0))

        # Draw the eye
        pygame.draw.circle(window, (255, 255, 255), [300, 300], 100, 0)
        pygame.draw.circle(window, (0, 0, 0), [300, 300], 25, 0)

        # Draw the rectangles at the updated positions
        pygame.draw.rect(window, (0, 0, 0), [rect1_x, min(rect1_y, 200), 400, 100], 0)
        pygame.draw.rect(window, (0, 0, 0), [rect2_x, max(rect2_y, 200), 400, 200], 0)

        # Update the display
        pygame.display.flip()

        # Set the frames per second
        pygame.time.Clock().tick(60)

        # Pause for half a second when rectangles reach certain positions
        if rect1_y >= 200:
            rect1_direction = -1
        if rect2_y <= 290:
            rect2_direction = 1

    # Wait for a random time before repeating animation
    pygame.time.delay(rand * 1000)