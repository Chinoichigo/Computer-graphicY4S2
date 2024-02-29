import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Ball parameters
radius = 0.5
segments = 50

# Animation parameters
stretch_factor = 1.5
squash_factor = 0.5
bounce_speed = 0.02
direction = [1, 1]  # [x_direction, y_direction]
position = [0, 0]   # [x_position, y_position]

def draw_ball():
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(segments + 1):
        theta = (2.0 * math.pi * float(i)) / float(segments)
        x = radius * stretch_factor * (math.cos(theta))
        y = radius * squash_factor * (math.sin(theta))
        glVertex2f(x, y)
    glEnd()

def update_position():
    global position, direction
    position[0] += bounce_speed * direction[0]
    position[1] += bounce_speed * direction[1]

    # Check for bouncing off walls
    if abs(position[0]) + radius >= 2.0:
        direction[0] *= -1
    if abs(position[1]) + radius >= 2.0:
        direction[1] *= -1

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

    print("OpenGL Version:", glGetString(GL_VERSION))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        update_position()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(position[0], position[1], -5.0)  # Move the ball away from the camera

        glColor3f(1.0, 1.0, 1.0)
        draw_ball()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
