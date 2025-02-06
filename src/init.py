import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import random
def draw_background():
    # Ground plane
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, -2, 5)
    glVertex3f(5, -2, 5)
    glVertex3f(5, -2, -5)
    glEnd()

    # Walls
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    # Front wall
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, 3, -5)
    glVertex3f(5, 3, -5)
    glVertex3f(5, -2, -5)
    # Left wall
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, 3, -5)
    glVertex3f(-5, 3, 5)
    glVertex3f(-5, -2, 5)
    # Right wall
    glVertex3f(5, -2, -5)
    glVertex3f(5, 3, -5)
    glVertex3f(5, 3, 5)
    glVertex3f(5, -2, 5)
    glEnd()


def init_display():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def load_background():
    background = pygame.image.load('C:\\Users\\hp\\Desktop\\Game\\assets\\images\\o.png')
    background = pygame.transform.scale(background, (800, 600))
    bg_texture = pygame.image.tostring(background, "RGB", 1)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, background.get_width(), background.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, bg_texture)
    glDisable(GL_TEXTURE_2D)

def load_background_music():
    pygame.mixer.music.load('D:\\estemation\\Estimation game\\WhatsApp-Audio-2022-01-14-at-8.36.16-AM.wav')
    pygame.mixer.music.play(-1)

def draw_background():
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-10, -10, -10)
    glTexCoord2f(1, 0); glVertex3f(10, -10, -10)
    glTexCoord2f(1, 1); glVertex3f(10, 10, -10)
    glTexCoord2f(0, 1); glVertex3f(-10, 10, -10)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def background():
    # Ground plane
    glColor3f(0.5, 0.5, 0)
    glBegin(GL_QUADS)
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, -2, 5)
    glVertex3f(5, -2, 5)
    glVertex3f(5, -2, -5)
    glEnd()

    # Draw white lines on the ground
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    for i in range(-5, 6):
        glVertex3f(i, -1.99, -5)  # Start point of the line
        glVertex3f(i, -1.99, 5)   # End point of the line
        glVertex3f(-5, -1.99, i)  # Start point of the line
        glVertex3f(5, -1.99, i)   # End point of the line
    glEnd()

    # Walls
    glColor3f(0, 0.8, 0.8)
    glBegin(GL_QUADS)
    # Front wall
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, 3, -5)
    glVertex3f(5, 3, -5)
    glVertex3f(5, -2, -5)
    # Left wall
    glVertex3f(-5, -2, -5)
    glVertex3f(-5, 3, -5)
    glVertex3f(-5, 3, 5)
    glVertex3f(-5, -2, 5)
    # Right wall
    glVertex3f(5, -2, -5)
    glVertex3f(5, 3, -5)
    glVertex3f(5, 3, 5)
    glVertex3f(5, -2, 5)
    glEnd()

    # Top roof
    glColor3f(0, 0.8, 0.8) # Yellow color
    glBegin(GL_QUADS)
    # Top
    glVertex3f(-5, 3, -5)
    glVertex3f(-5, 3, 5)
    glVertex3f(5, 3, 5)
    glVertex3f(5, 3, -5)
    glEnd()

    draw_rects_on_front_wall()

def draw_rects_on_front_wall():
    # Determine the size and position of the rectangles on the front wall
    rect_width = 0.2
    rect_height = 0.6
    gap_between_rects = 0.1
    num_rects = 55

    # Calculate the starting position of the first rectangle
    start_x = -6 + gap_between_rects
    start_y = -2 + gap_between_rects

    # Flag to toggle between white and black
    is_white = True

    # Draw rectangles on the front wall
    for i in range(num_rects):
        for j in range(num_rects):
            x = start_x + (rect_width + gap_between_rects) * i
            y = start_y + (rect_height + gap_between_rects) * j
            
            # Alternate between white and black
            if is_white:
                glColor3f(1.0, 1.0, 1.0)  # Set color to white
            else:
                glColor3f(0.0, 0.0, 0.0)  # Set color to black
            
            glBegin(GL_QUADS)
            glVertex3f(x, y, -5 + 0.001)  # Add a slight offset to prevent z-fighting
            glVertex3f(x + rect_width, y, -5 + 0.001)
            glVertex3f(x + rect_width, y + rect_height, -5 + 0.001)
            glVertex3f(x, y + rect_height, -5 + 0.001)
            glEnd()
            
            # Toggle color for the next rectangle
            is_white = not is_white

        # Toggle color for the next row
        is_white = not is_white
