
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    pygame.init()
    global windowPy
    windowPy = pygame.display.set_mode((800,650), DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Smart Home')
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)




    
def main():
    init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
        pygame.display.flip()
        pygame.time.wait(10)


main() 
