import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surface =(
(0,1,2,3),
(3,2,7,6),
(6,7,5,4),
(4,5,1,0),
(1,5,7,2),
(4,0,3,6),

)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,1),
    (0,1,1),
)


def cube():
    glBegin(GL_QUADS)
    
    for surfaces in surface:
        x = 0
        for vertex in surfaces:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()



    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # fov and clipping
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    object_passed = 0  # Counter to track the number of times the cube passes the depth

    while object_passed < 10:  # Run the cube rendering process 10 times
        glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)

        cube_passed = False  # Flag to track whether the cube passed the depth in this iteration
        x_move = 0 
        y_move = 0
        while not cube_passed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_move = 0.3
                    if event.key == pygame.K_RIGHT:
                        x_move = -0.3
                    if event.key == pygame.K_UP:
                        y_move = -0.3
                    if event.key == pygame.K_DOWN:
                        y_move = 0.3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_move = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_move = 0
                

            x = glGetDoublev(GL_MODELVIEW_MATRIX)

            camera_z = x[3][2]  # Z component is at index 2

            if camera_z < -1:
                cube_passed = True

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glTranslatef(x_move, y_move, 0.5)

            cube()
            pygame.display.flip()
            pygame.time.wait(10)

        object_passed += 1  # Increment the counter after the cube passes the depth

# Call the main function to start the program
main()
pygame.quit
quit()