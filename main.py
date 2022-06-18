
from pygame.constants import *
from pygame.locals import *
from generate_obj import *
from load_object import *
from OpenGL.GLU import *
from OpenGL.GL import *
from cmath import sin
import pygame
import time


def init():
    pygame.init()
    pygame.display.set_mode((1280,720), OPENGL | DOUBLEBUF |pygame.RESIZABLE)
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glMateriali(GL_FRONT, GL_SHININESS, 128)


def instantiateObj():
    global foundation,wall,sofa,shelf,table,waterTank
    global indoor,roof,outdoor,fan,text,drone,plant
    foundation = Object('foundation.obj')
    wall = Object('wall.obj')
    sofa = Object('sofa.obj')
    shelf = Object('shelf.obj')
    table = Object('foodTable.obj')
    roof = Object('roofFrame.obj')
    outdoor = Object('outdoor.obj')
    fan = Object('fan.obj')
    plant = Object('plant.obj')
    waterTank = Object('waterTank.obj')
    text= Object('text.obj')
    drone= Object('drone.obj')
    indoor = Object('indoor.obj')
    generate(foundation)
    generate(waterTank)
    generate(wall)
    generate(sofa)
    generate(table)
    generate(shelf)
    generate(roof)
    generate(drone)
    generate(fan)
    generate(text)
    generate(indoor)
    generate(outdoor)
    generate(plant)



def openOutDoor():
    glPushMatrix
    ct = time.time()
    for i in range(2000):
        glRotatef(abs(sin(ct)) * 0.005, 0, 500, 0)
    outdoor.render()
    glPopMatrix


def openInDoor():
    glPushMatrix
    ct = time.time()
    for i in range(2000):
        glRotatef(abs(sin(ct)) * 0.005, 0, 500, 0)
    indoor.render()
    glPopMatrix


def rotateFan():
    glPushMatrix
    ct = time.time()
    for i in range(2000):
        glRotatef(abs(sin(ct)) * 0.5, 0, 1.3, -0.7)
    fan.render()
    glPopMatrix


def main():
    init()
    instantiateObj()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = (1280,720)
    gluPerspective(90.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glMatrixMode(GL_MODELVIEW)

    rx, ry = (-90,10)
    tx, ty = (0,0)
    zpos = 35
    rotate = move = False
    running = True
    global angle 
    angle = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running  = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running  = False
            
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 4: zpos = max(1, zpos-1)
                elif event.button == 5: zpos += 1
                if event.button == 1: rotate = True
                elif event.button == 3: move = True
            
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1: rotate = False
                elif event.button == 3: move = False

            elif event.type == MOUSEMOTION:
                i, j = event.rel
                if rotate:rx += i ;ry += j 
                if move: tx += i ; ty -= j
    
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
                    zpos -=1
        elif keys_pressed[pygame.K_DOWN]:
                    zpos +=1

        elif keys_pressed[pygame.K_RIGHT]:
                    tx -=1
        elif keys_pressed[pygame.K_LEFT]:
                    tx +=1
      
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslate(tx/10, ty/10., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        foundation.render()
        # waterTank.render()
        wall.render()
        sofa.render()
        shelf.render()
        table.render()
        roof.render()
        text.render()
        plant.render()
        if rx <-90 and rx > -150 and ry > 20 and zpos <20:
            openInDoor()
        else:
            indoor.render()
        if ry  > 10 and rx < -60 and rx > -90 :
            openOutDoor()
        else: 
            outdoor.render()
            
        if event.type == KEYDOWN and event.key == K_TAB:
            rotateFan()
        else:
            fan.render()
        glPushMatrix()
        glRotatef(angle, 0, 500, 0)
        angle+=1
        drone.render()
        glPopMatrix()
        
        pygame.display.flip()



if __name__ == "__main__":
    main()