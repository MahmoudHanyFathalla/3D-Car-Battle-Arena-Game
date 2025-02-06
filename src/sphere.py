import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

def draw_sphere(radius, slices, stacks, position, rotation, colors, speed=0.0, offset=0.0):
    glPushMatrix()
    # Calculate translation based on speed
    translation = speed * (time.time() % 10)  # Adjust 10 based on desired speed
    glTranslatef(position[0] + offset + translation, position[1], position[2])
    glRotatef(rotation, 0, 1, 0)  # Rotate around the y-axis
    for i in range(slices):
        theta1 = i * math.pi * 2 / slices
        theta2 = (i + 1) * math.pi * 2 / slices
        glBegin(GL_QUAD_STRIP)
        for j in range(stacks + 1):
            phi = j * math.pi / stacks
            x1 = radius * math.cos(theta1) * math.sin(phi)
            y1 = radius * math.sin(theta1) * math.sin(phi)
            z1 = radius * math.cos(phi)
            x2 = radius * math.cos(theta2) * math.sin(phi)
            y2 = radius * math.sin(theta2) * math.sin(phi)
            z2 = radius * math.cos(phi)
            glColor3f(*colors[j % len(colors)])  # Change color dynamically
            glVertex3f(x1, y1, z1)
            glVertex3f(x2, y2, z2)
        glEnd()
    glPopMatrix()

def draw_spheres(spheres, rotat):
    colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
    for sphere in spheres:
        sphere['position'][1] += sphere['velocity']
        if sphere['position'][1] >= 2.0 or sphere['position'][1] <= -1.0:
            sphere['velocity'] *= -1.0
        draw_sphere(0.1, 20, 10, sphere['position'], rotat, colors)

def draw_orange_rectangle(position, rotat):
    draw_sphere(0.5, 80, 30, position, rotat, [(1.0, 0.0, 0.0), (1, 1.0, 0.0)])

def update_sphere_positions(spheres):
    for sphere in spheres:
        sphere['position'][1] += sphere['velocity']
        if sphere['position'][1] >= 2.0 or sphere['position'][1] <= -1.0:
            sphere['velocity'] *= -1.0
