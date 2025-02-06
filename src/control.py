# controls.py
import pygame
import subprocess
def handle_input(car1_position, car2_position, boundary_left, boundary_right, boundary_left2, boundary_right2, view_angle, view_angle2, car4_position, car5_position, boundary_left4, boundary_right4, boundary_left5, boundary_right5, view_angle4, view_angle5):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    # Car 1 controls
    if keys[pygame.K_LEFT]:
        if car1_position[0] > boundary_left:
            car1_position[0] -= 0.1
            view_angle = 0

    if keys[pygame.K_RIGHT]:
        if car1_position[0] < boundary_right:
            car1_position[0] += 0.1
            view_angle = 180

    if keys[pygame.K_UP]:
        if car1_position[2] > -5:
            car1_position[2] -= 0.1
            boundary_right += 0.05
            boundary_left -= 0.05
            view_angle = 90

    if keys[pygame.K_DOWN]:
        if car1_position[2] < 0.1:
            if car1_position[0] > boundary_left and car1_position[0] < boundary_right:
                car1_position[2] += 0.1
                boundary_left += 0.05
                boundary_right -= 0.05
            else:
                if car1_position[0] < boundary_left:
                    car1_position[0] += 0.1
                    view_angle = 180
                    car1_position[2] += 0.1
                    boundary_left += 0.05
                    view_angle = -90
                    boundary_right -= 0.05
                elif car1_position[0] > boundary_right:
                    car1_position[0] -= 0.1
                    view_angle = 0
                    car1_position[2] += 0.1
                    boundary_left += 0.05
                    view_angle = -90
                    boundary_right -= 0.05
        view_angle = -90

    # Car 2 controls
    if keys[pygame.K_a]:
        if car2_position[0] > boundary_left2:
            car2_position[0] -= 0.1
            view_angle2 = 0

    if keys[pygame.K_d]:
        if car2_position[0] < boundary_right2:
            car2_position[0] += 0.1
            view_angle2 = 180

    if keys[pygame.K_w]:
        if car2_position[2] > -5:
            car2_position[2] -= 0.1
            boundary_right2 += 0.05
            boundary_left2 -= 0.05
            view_angle2 = 90

    if keys[pygame.K_s]:
        if car2_position[2] < 0.1:
            if car2_position[0] > boundary_left2 and car2_position[0] < boundary_right2:
                car2_position[2] += 0.1
                boundary_right2 -= 0.05
                boundary_left2 += 0.05
            else:
                if car2_position[0] < boundary_left2:
                    car2_position[0] += 0.1
                    view_angle2 = 180
                    car2_position[2] += 0.1
                    boundary_right2 -= 0.05
                    boundary_left2 += 0.05
                if car2_position[0] > boundary_right2:
                    car2_position[0] -= 0.2
                    view_angle2 = 0
                    car2_position[2] += 0.1
                    boundary_right2 -= 0.05
                    boundary_left2 += 0.05
        view_angle2 = -90
        
    # Car 4 controls
    if keys[pygame.K_j]:
        if car4_position[0] > boundary_left4:
            car4_position[0] -= 0.1
            view_angle4 = 0

    if keys[pygame.K_l]:
        if car4_position[0] < boundary_right4:
            car4_position[0] += 0.1
            view_angle4 = 180

    if keys[pygame.K_i]:
        if car4_position[2] > -5:
            car4_position[2] -= 0.1
            boundary_right4 += 0.05
            boundary_left4 -= 0.05
            view_angle4 = 90

    if keys[pygame.K_k]:
        if car4_position[2] < 0.1:
            if car4_position[0] > boundary_left4 and car4_position[0] < boundary_right4:
                car4_position[2] += 0.1
                boundary_right4 -= 0.05
                boundary_left4 += 0.05
            else:
                if car4_position[0] < boundary_left4:
                    car4_position[0] += 0.1
                    view_angle4 = 180
                    car4_position[2] += 0.1
                    boundary_right4 -= 0.05
                    boundary_left4 += 0.05
                if car4_position[0] > boundary_right4:
                    car4_position[0] -= 0.2
                    view_angle4 = 0
                    car4_position[2] += 0.1
                    boundary_right4 -= 0.05
                    boundary_left4 += 0.05
        view_angle4 = -90

    # Car 5 controls
    if keys[pygame.K_f]:
        if car5_position[0] > boundary_left5:
            car5_position[0] -= 0.1
            view_angle5 = 0

    if keys[pygame.K_o]:
        subprocess.run(["python", "C:Users\\hp\\Desktop\\Game\src\\main.py"])        

    if keys[pygame.K_h]:
        if car5_position[0] < boundary_right5:
            car5_position[0] += 0.1
            view_angle5 = 180

    if keys[pygame.K_t]:
        if car5_position[2] > -5:
            car5_position[2] -= 0.1
            boundary_right5 += 0.05
            boundary_left5 -= 0.05
            view_angle5 = 90

    if keys[pygame.K_g]:
        if car5_position[2] < 0.1:
            if car5_position[0] > boundary_left5 and car5_position[0] < boundary_right5:
                car5_position[2] += 0.1
                boundary_right5 -= 0.05
                boundary_left5 += 0.05
            else:
                if car5_position[0] < boundary_left5:
                    car5_position[0] += 0.1
                    view_angle5 = 180
                    car5_position[2] += 0.1
                    boundary_right5 -= 0.05
                    boundary_left5 += 0.05
                if car5_position[0] > boundary_right5:
                    car5_position[0] -= 0.2
                    view_angle5 = 0
                    car5_position[2] += 0.1
                    boundary_right5 -= 0.05
                    boundary_left5 += 0.05
        view_angle5 = -90

    return car1_position, car2_position, boundary_left, boundary_right, boundary_left2, boundary_right2, view_angle, view_angle2, car4_position, car5_position, boundary_left4, boundary_right4, boundary_left5, boundary_right5, view_angle4, view_angle5
