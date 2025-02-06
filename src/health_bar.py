from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_health_bar(x, y, width, height, health, color):
    # Calculate the width of the health bar based on health percentage
    health_width = (health / 300) * width

    glPushMatrix()
    glTranslatef(x, y, 0.0)

    # Draw background
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, height)
    glVertex2f(width, height)
    glVertex2f(width, 0)
    glEnd()

    # Draw health bar
    glColor3f(*color)  # Green color for healthy portion
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, height)
    glVertex2f(health_width, height)
    glVertex2f(health_width, 0)
    glEnd()

    glPopMatrix()

def draw_health_bars(car1_health,car2_health,car3_health,car4_health,car5_health):
    draw_health_bar(-2.6, 1.6, 1, 0.1, car1_health, (1.0, 0.0, 0.0))
    draw_health_bar(-2.6, 1.8, 1, 0.1, car2_health, (0.0, 1.0, 0.0))
    draw_health_bar(-2.6, 1.4, 1, 0.1, car3_health, (0, 1, 1))
    draw_health_bar(-2.6, 1.2, 1, 0.1, car5_health, (0.6, 0.3, 0.0) )
    draw_health_bar(-2.6, 1, 1, 0.1, car4_health, (1.0, 1.0, 0.0))
