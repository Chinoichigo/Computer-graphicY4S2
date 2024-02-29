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

trivertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
    

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


def triangle(trivertices):
    glBegin(GL_TRIANGLES)

    for vertex in trivertices:
        glVertex3fv(vertex)




    glEnd()


def set_vert(max_distance):
    x_value_change = random.randrange(-10,10)
    y_value_change = random.randrange(-10,10)
    z_value_change = random.randrange(-1*max_distance,-20)
    new_verts = []
    for verts in vertices:
       
        new_vert = []

        new_x = verts[0]  + x_value_change
        new_y = verts[1] + y_value_change
        new_z = verts[2]  + z_value_change 
           

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)
            
           

        new_verts.append(new_vert)
    return new_verts

def set_vertt(max_distance):

    tx_value_change = random.randrange(-30,30)
    ty_value_change = random.randrange(-20,20)
    z_value_change = random.randrange(-1*max_distance,-20)


    new_vertexts =[]
    for vertex in trivertices:
        new_vert = []

        newtx = vertex[0] + tx_value_change
        newty = vertex[1] + ty_value_change
        newtz = vertex[2] + z_value_change
        new_vert.append(newtx)
        new_vert.append(newty)
        new_vert.append(newtz)
        new_vertexts.append(new_vert)
    return new_vertexts

def cube(vertices):
    glBegin(GL_QUADS)
    for surfaces in surface:
        x = 0
        for vertex in surfaces:
            x += 1
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

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    object_passed = 0

    
    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)

  
    x_move = 0
    y_move = 0

    max_distance = 300
    tri_dict = {}
    for x in range(200):
        tri_dict[x] = set_vertt(max_distance)
    cube_dict = {}
    for x in range(200):
        cube_dict[x] = set_vert(max_distance)

    while True:
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

        camera_z = x[3][2]

           

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move, y_move, 0.5)
        for each_cube in cube_dict:
                cube(cube_dict[each_cube])
        for each_tri in tri_dict:
                triangle(tri_dict[each_tri])
        pygame.display.flip()
        pygame.time.wait(10)

        

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
