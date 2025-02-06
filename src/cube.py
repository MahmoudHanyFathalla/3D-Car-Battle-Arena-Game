# cube.py
# cube.py

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time
import random
# cube.py
class Cube:
    def __init__(self, position,is_static = False):
        self.position = position
        self.is_static = is_static
      
    def move_towards_nearest_car(self, car1_position, car1_health, car2_position, car2_health, car3_position, car3_health, speed,car4_health,car4_position,car5_health,car5_position):
        # Convert positions to NumPy arrays
        car1_position = np.array(car1_position)
        car2_position = np.array(car2_position)
        car3_position = np.array(car3_position)
        car4_position = np.array(car4_position)
        car5_position = np.array(car5_position)

        # Calculate distances to all cars
        distance_to_car1 = np.linalg.norm(self.position - car1_position)
        distance_to_car2 = np.linalg.norm(self.position - car2_position)
        distance_to_car3 = np.linalg.norm(self.position - car3_position)
        distance_to_car4 = np.linalg.norm(self.position - car4_position)
        distance_to_car5 = np.linalg.norm(self.position - car5_position)

        # Determine the nearest car
        nearest_car_position = None
        nearest_car_health = None
        nearest_car_index = None

        min_distance = min(distance_to_car1, distance_to_car2, distance_to_car3,distance_to_car4,distance_to_car5)

        if min_distance == distance_to_car1:
            nearest_car_position = car1_position
            nearest_car_health = car1_health
            nearest_car_index = 1
        elif min_distance == distance_to_car2:
            nearest_car_position = car2_position
            nearest_car_health = car2_health
            nearest_car_index = 2
        elif min_distance == distance_to_car4:
            nearest_car_position = car4_position
            nearest_car_health = car4_health
            nearest_car_index = 4
        elif min_distance == distance_to_car5:
            nearest_car_position = car5_position
            nearest_car_health = car5_health
            nearest_car_index = 5        
        else:
            nearest_car_position = car3_position
            nearest_car_health = car3_health
            nearest_car_index = 3

        # Move towards the nearest car
        direction_to_nearest_car = nearest_car_position - self.position
        direction_to_nearest_car /= np.linalg.norm(direction_to_nearest_car)  # Normalize direction vector
        self.velocity = direction_to_nearest_car * speed
        self.position += self.velocity

        # Check for collision
        if np.linalg.norm(self.position - nearest_car_position) < 0.2:  # Adjust collision distance as needed
            return True, nearest_car_index  # Collision occurred with nearest car
        else:
            return False, None  # No collision

    def check_collision(self, car_position, car_health):
            # Check if the cube is close enough to a car to cause a collision
            dist_to_car = ((self.position[0] - car_position[0]) ** 2 +
                        (self.position[1] - car_position[1]) ** 2 +
                        (self.position[2] - car_position[2]) ** 2) ** 0.5
            if dist_to_car < 0.2:  # Adjust collision distance as needed
                car_health -= 1  # Decrease car's health
                if car_health <= 0:
                    # If car's health reaches zero, make it disappear
                    car_position[0] = 1000  # Move car out of the scene
                    car_position[1] = 1000
                    car_position[2] = 1000
        
  
    def move_away_from_cubes(self, car3_position, cubes):
        # Define boundaries for movement
        min_x, max_x = -2.5, 2.5
        min_z, max_z = -5, 0.1
        grid_size = 0.5  # Size of each grid cell
        threshold_distance = 1.0  # Threshold distance for considering a cube "near"
        movement_speed = 0.1  # Adjust movement speed

        # Default angle (no movement)
        angle = 0

        # Check if any cube is "near" and adjust movement accordingly
        near_cube_found = False
        for cube in cubes:
            cube_position = np.array(cube.position)
            distance_to_cube = np.linalg.norm(car3_position - cube_position)
            if distance_to_cube < threshold_distance:
                near_cube_found = True
               # print("Near cube found!")
                # Calculate direction to move away from the cube
                direction = np.sign(car3_position - cube_position)
               # print("Direction:", direction)
                # Adjust car position to move away from the cube
                car3_position[0] += direction[0] * movement_speed
                car3_position[2] += direction[2] * movement_speed

                # Determine the angle based on the direction of movement
                if direction[0] == 0 and direction[2] == 1:
                    angle = 90  # Up
                elif direction[0] == 0 and direction[2] == -1:
                    angle = -90  # Down
                elif direction[0] == 1 and direction[2] == 1:
                    angle = 45  # Up-right diagonal
                elif direction[0] == -1 and direction[2] == -1:
                    angle = -135  # Down-left diagonal
                elif direction[0] == 1 and direction[2] == -1:
                    angle = -45  # Down-right diagonal
                elif direction[0] == -1 and direction[2] == 1:
                    angle = 135  # Up-left diagonal
                elif direction[0] == 1 and direction[2] == 0:
                    angle = 180  # Right
                elif direction[0] == -1 and direction[2] == 0:
                    angle = 0  # Left
               # print("Angle:", angle)

        # If a near cube is found, clip the position to stay within the boundaries
        if near_cube_found:
            car3_position[0] = max(min_x, min(max_x, car3_position[0]))
            car3_position[2] = max(min_z, min(max_z, car3_position[2]))

        return car3_position, angle
  
    def draw_cube(self, size=0.2):
        # Draw cube at the cube's position with gradient colors for each face
        x, y, z = self.position
        half_size = size / 2.0

        glBegin(GL_QUADS)

        # Front face (mix of red and black)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(x - half_size, y - half_size, z + half_size)
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z + half_size)

        # Back face (mix of red and black)
        glColor3f(0.5, 0, 0)  # Dark red
        glVertex3f(x - half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y - half_size, z - half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x + half_size, y + half_size, z - half_size)
        glVertex3f(x - half_size, y + half_size, z - half_size)

        # Top face (mix of red and black)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(x - half_size, y + half_size, z + half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x + half_size, y + half_size, z - half_size)
        glColor3f(0.5, 0, 0)  # Dark red
        glVertex3f(x - half_size, y + half_size, z - half_size)

        # Bottom face (mix of red and black)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(x - half_size, y - half_size, z + half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glVertex3f(x + half_size, y - half_size, z - half_size)
        glColor3f(0.5, 0, 0)  # Dark red
        glVertex3f(x - half_size, y - half_size, z - half_size)

        # Right face (mix of red and black)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x + half_size, y + half_size, z - half_size)
        glColor3f(0.5, 0, 0)  # Dark red
        glVertex3f(x + half_size, y - half_size, z - half_size)

        # Left face (mix of red and black)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(x - half_size, y - half_size, z + half_size)
        glColor3f(0, 0, 0)  # Black
        glVertex3f(x - half_size, y + half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z - half_size)
        glColor3f(0.5, 0, 0)  # Dark red
        glVertex3f(x - half_size, y - half_size, z - half_size)

        glEnd()

def handle_cubes(cubes, last_cube_time, boundary_left, boundary_right, boundary_down, car1_position, car1_health, car2_position, car2_health, car3_position, car3_health,car4_health,car4_position,car5_health,car5_position):
    if time.time() - last_cube_time >= 3:
        # Create a new cube object with a random position within the bounds of the screen
        cube_position = [random.uniform(boundary_left, boundary_right), -1.9 , random.uniform(-5, boundary_down)]
        # Randomly decide whether the cube should be static or moving
        is_static = random.choice([True, False])
        new_cube = Cube(cube_position, is_static)
        cubes.append(new_cube)  # Add the new cube to the list
        last_cube_time = time.time()  # Update the last cube creation time
        print("New cube created at position:", cube_position) 

    # Move each moving cube towards the nearest car
    for cube in cubes:
        if not cube.is_static:  # Check if the cube is moving  
            cube_speed = random.uniform(0.01, 0.1)
            collision, collided_car_index = cube.move_towards_nearest_car(car1_position, car1_health, car2_position, car2_health, car3_position, car3_health, cube_speed,car4_health,car4_position,car5_health,car5_position)
            if collision:
                if collided_car_index == 1:
                    car1_health -= 1
                elif collided_car_index == 2:
                    car2_health -= 1
                elif collided_car_index == 3:
                    car3_health -= 1
                elif collided_car_index == 4:
                    car4_health -= 1
                elif collided_car_index == 5:
                    car5_health -= 1        
            
        else:  # Check if the cube is static
            # Check if any car is near the position of a static cube (within a certain threshold)
            near_threshold = 0.2  # Adjust as needed
            car1_pos_np = np.array(car1_position)
            car2_pos_np = np.array(car2_position)
            car3_pos_np = np.array(car3_position)
            car4_pos_np = np.array(car4_position)
            car5_pos_np = np.array(car5_position)
            cube_pos_np = np.array(cube.position)
            if np.linalg.norm(car1_pos_np - cube_pos_np) < near_threshold:
                car1_health -= 5
            if np.linalg.norm(car2_pos_np - cube_pos_np) < near_threshold:
                car2_health -= 5
            if np.linalg.norm(car3_pos_np - cube_pos_np) < near_threshold:
                car3_health -= 5    
            if np.linalg.norm(car4_pos_np - cube_pos_np) < near_threshold:
                car4_health -= 5 
            if np.linalg.norm(car5_pos_np - cube_pos_np) < near_threshold:
                car5_health -= 5             
                
        cube.draw_cube()  # Draw each cube

    # Handle cube-car collisions only for moving cubes
    for cube in cubes:
        cube.check_collision(car1_position, car1_health)
        cube.check_collision(car2_position, car2_health)
        cube.check_collision(car3_position, car3_health)
        cube.check_collision(car4_position, car4_health)
        cube.check_collision(car5_position, car5_health)

    return cubes, last_cube_time, car1_health, car2_health, car3_health,car4_health,car5_health
