import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up Pygame display
width, height = 400, 400
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up OpenGL perspective
gluOrtho2D(0, width, 0, height)

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

yello = (1, 0, 0)



# Function to draw the clipped polygon
def draw_clipped_polygon():
    glBegin(GL_POLYGON)
    glVertex2f(60.0, 90.0)
    glVertex2f(60.0, 120.0)
    glVertex2f(430.0/4.0, 120.0)
    glVertex2f(120.0, 70.0)
    glVertex2f(120.0, 90.0)
    glEnd()

# Function to draw the unclipped polygon
def draw_unclipped_polygon():
    glBegin(GL_POLYGON)
    glVertex2f(60, 90)
    glVertex2f(60, 120)
    glVertex2f(120, 120)
    glVertex2f(120, 90)
    glEnd()

# Function to draw the line segment
def draw_line_segment():
    
    glBegin(GL_LINES)
    glColor3fv = (yello)
    glVertex2i(100, 130)
    glVertex2i(130, 90)
    glEnd()

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw shapes
        glColor3f(*BLACK)
        draw_clipped_polygon()
        draw_line_segment()

        glColor3f(*RED)
        draw_unclipped_polygon()

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
