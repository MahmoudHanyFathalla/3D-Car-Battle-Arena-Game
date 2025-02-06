# car.py
import math
from OpenGL.GL import *


def draw_circle(radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


def draw_car(position, health, view_angle, body_color=(0.8, 0.0, 0.0), roof_color=(0.0, 0.0, 0.8)):
    if health <= 0:
        return  # Don't draw the car if its health is zero or below

    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glRotatef(view_angle, 0, 1, 0)  # Rotate around Y-axis for left/right view

    # Draw body
    glColor3f(*body_color)  # Use the provided body color
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-0.35, 0.1, 0.1)
    glVertex3f(-0.35, -0.1, 0.1)
    glVertex3f(0.35, -0.1, 0.1)
    glVertex3f(0.35, 0.1, 0.1)
    # Back face
    glVertex3f(-0.35, 0.1, -0.1)
    glVertex3f(-0.35, -0.1, -0.1)
    glVertex3f(0.35, -0.1, -0.1)
    glVertex3f(0.35, 0.1, -0.1)
    # Top face
    glVertex3f(-0.35, 0.1, 0.1)
    glVertex3f(-0.35, 0.1, -0.1)
    glVertex3f(0.35, 0.1, -0.1)
    glVertex3f(0.35, 0.1, 0.1)
    # Bottom face
    glVertex3f(-0.35, -0.1, 0.1)
    glVertex3f(-0.35, -0.1, -0.1)
    glVertex3f(0.35, -0.1, -0.1)
    glVertex3f(0.35, -0.1, 0.1)
    # Left face
    glVertex3f(-0.35, 0.1, 0.1)
    glVertex3f(-0.35, 0.1, -0.1)
    glVertex3f(-0.35, -0.1, -0.1)
    glVertex3f(-0.35, -0.1, 0.1)
    # Right face
    glVertex3f(0.35, 0.1, 0.1)
    glVertex3f(0.35, 0.1, -0.1)
    glVertex3f(0.35, -0.1, -0.1)
    glVertex3f(0.35, -0.1, 0.1)
    glEnd()

    # Draw smaller roof
    glColor3f(*roof_color)  # Use the provided roof color
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-0.2, 0.1, 0.1)
    glVertex3f(-0.2, 0.15, 0.05)
    glVertex3f(0.2, 0.15, 0.05)
    glVertex3f(0.2, 0.1, 0.1)
    # Back face
    glVertex3f(-0.2, 0.1, -0.1)
    glVertex3f(-0.2, 0.15, -0.05)
    glVertex3f(0.2, 0.15, -0.05)
    glVertex3f(0.2, 0.1, -0.1)
    # Top face
    glVertex3f(-0.2, 0.1, 0.1)
    glVertex3f(-0.2, 0.1, -0.1)
    glVertex3f(0.2, 0.1, -0.1)
    glVertex3f(0.2, 0.1, 0.1)
    # Bottom face
    glVertex3f(-0.2, 0.15, 0.1)
    glVertex3f(-0.2, 0.15, -0.1)
    glVertex3f(0.2, 0.15, -0.1)
    glVertex3f(0.2, 0.15, 0.1)
    # Left face
    glVertex3f(-0.2, 0.1, 0.1)
    glVertex3f(-0.2, 0.1, -0.1)
    glVertex3f(-0.2, 0.15, -0.1)
    glVertex3f(-0.2, 0.15, 0.1)
    # Right face
    glVertex3f(0.2, 0.1, 0.1)
    glVertex3f(0.2, 0.1, -0.1)
    glVertex3f(0.2, 0.15, -0.1)
    glVertex3f(0.2, 0.15, 0.1)
    glEnd()

    # Draw wheels
    glColor3f(0.3, 0.3, 0.3)  # Gray color for wheels
    draw_wheel(-0.25, -0.1, 0.1, 0.05, 0.05)  # Front left wheel
    draw_wheel(0.25, -0.1, 0.1, 0.05, 0.05)   # Front right wheel
    draw_wheel(-0.25, -0.1, -0.1, 0.05, 0.05) # Rear left wheel
    draw_wheel(0.25, -0.1, -0.1, 0.05, 0.05)  # Rear right wheel

    glPopMatrix()


def draw_wheel(x, y, z, radius, thickness):
    sides = 360
    height = thickness
    glBegin(GL_QUAD_STRIP)
    for i in range(sides+1):
        angle = 2.0 * math.pi * i / sides
        x1 = x + math.cos(angle) * radius
        y1 = y + math.sin(angle) * radius
        x2 = x + math.cos(angle) * (radius - height)
        y2 = y + math.sin(angle) * (radius - height)
        glVertex3f(x1, y1, z + thickness)
        glVertex3f(x1, y1, z)
        glVertex3f(x2, y2, z + thickness)
        glVertex3f(x2, y2, z)
    glEnd()