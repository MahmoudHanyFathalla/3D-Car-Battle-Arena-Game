import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import random
from car import draw_car
from control import handle_input
from cube import *
from health_bar import *
from init import *
import math
from sphere import *

# Global variables
car1_position = [-1.0, -1.9, 0.0]
car2_position = [1.0, -1.9, 0.0]

car4_position = [2, -1.9, 0.0]
car5_position = [-2, -1.9, 0.0]

boundary_right = 2.3
boundary_right2 = 2.35
boundary_left = -2.3
boundary_left2 = -2.35
boundary_down = 0.1

boundary_right4 = 2.3
boundary_right5 = 2.35
boundary_left4 = -2.3
boundary_left5 = -2.35

cube = Cube([0.0, -1.0, 0.0])
car1_health = 300
car2_health = 300

car4_health = 300
car5_health = 300
car3_position = [0.0, -1.9, 0.0]
car3_health = 300

def main():
    global car1_position, car2_position, boundary_left, boundary_right, boundary_left2, boundary_right2, boundary_down, car1_health, car2_health, car3_position, car3_health, car4_health,car4_position,car5_health,car5_position,boundary_left4, boundary_right4, boundary_left5, boundary_right5

    init_display()
    #draw_background()
    #load_background()
    #load_background_music()

    view_angle = 0
    view_angle2 = 0
    view_angle3 = 0

    view_angle4 = 0
    view_angle5 = 0

    cubes = []
    last_cube_time = time.time()

    orange_rect_position = [0.2, 2.5, -3.0]
    orange_rect_speed = 0.01
    orange_rect_moving_up = True

    num_spheres = 20
    initial_y_positions = [-1.0, -0.8, -0.6, -0.4, -0.2, 0, -0.2, -0.4, -0.6, -0.8, -1, -0.8, -0.6, -0.4, -0.2, 0, -0.2, -0.4, -0.6, -0.8, -1]
    initial_velocities = [0.05] * num_spheres
    initial_x = -4.7

    spheres = [{'position': [initial_x + 0.5 * i, initial_y_positions[i], -4], 'velocity': initial_velocities[i]} for i in range(num_spheres)]

    rotat = 0

    while True:
        car1_position, car2_position, boundary_left, boundary_right, boundary_left2, boundary_right2, view_angle, view_angle2, car4_position, car5_position, boundary_left4, boundary_right4, boundary_left5, boundary_right5, view_angle4, view_angle5 = handle_input(car1_position, car2_position, boundary_left, boundary_right, boundary_left2, boundary_right2, view_angle, view_angle2, car4_position, car5_position, boundary_left4, boundary_right4, boundary_left5, boundary_right5, view_angle4, view_angle5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        background()
        #load_background()
        #draw_background()

        if car1_health > 0:
            draw_car(car1_position, car1_health, view_angle, body_color=(0, 0.0, 0.0), roof_color=(1.0, 0.0, 0))

        if car2_health > 0:
            draw_car(car2_position, car2_health, view_angle2, body_color=(0.0, 0.8, 0.0), roof_color=(0.8, 0, 0.8))

        if car4_health > 0:
            draw_car(car4_position, car4_health, view_angle4, body_color=(1, 1, 0.0), roof_color=(0, 0, 0))


        if car5_health > 0:
            draw_car(car5_position, car5_health, view_angle5, body_color=(0.6, 0.3, 0.0), roof_color=(0, 0, 0)  )
    

        if car1_health <= 0:
            draw_car([-20.0, -20.9, 20.0], car1_health, view_angle, body_color=(0.8, 0.0, 0.0), roof_color=(0.0, 0.0, 0.8))
            car1_position = [-20.0, -20.9, 20.0]

        if car2_health <= 0:
            draw_car([-20.0, -20.9, 20.0], car2_health, view_angle2, body_color=(0.0, 0.8, 0.0), roof_color=(0.8, 0, 0.8))
            car2_position = [-20.0, -20.9, 20.0]

        if car4_health <= 0:
            draw_car([-20.0, -20.9, 20.0], car4_health, view_angle4, body_color=(0.8, 0.0, 0.0), roof_color=(0.0, 0.0, 0.8))
            car4_position = [-20.0, -20.9, 20.0]

        if car5_health <= 0:
            draw_car([-20.0, -20.9, 20.0], car5_health, view_angle5, body_color=(0.0, 0.8, 0.0), roof_color=(0.8, 0, 0.8))
            car5_position = [-20.0, -20.9, 20.0]    

        cubes, last_cube_time, car1_health, car2_health, car3_health, car4_health,car5_health = handle_cubes(cubes, last_cube_time, boundary_left, boundary_right, boundary_down, car1_position, car1_health, car2_position, car2_health, car3_position, car3_health,car4_health,car4_position,car5_health,car5_position)

        rotat += 2
        draw_spheres(spheres, rotat)
        draw_orange_rectangle(orange_rect_position, rotat)
        draw_health_bars(car1_health, car2_health, car3_health,car4_health,car5_health )

        cube = Cube([0.0, -1.0, 0.0])
        car3_position, view_angle3 = cube.move_away_from_cubes(car3_position, cubes)
        draw_car(car3_position, 300, 0, body_color=(1.0, 0.0, 1.0), roof_color=(0.0, 1.0, 1.0))

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
