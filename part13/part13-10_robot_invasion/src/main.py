# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

height = robot.get_height()
width = robot.get_width()

robot_quantity = 18
robot_list = []

for i in range(25):   #random x and y coordinates
    robot_list.append([random.randint(0, 590), random.randint(-1 * height * 5,  -1 * height)])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(robot_quantity):
        if robot_list[i][1] + height < 480:
            robot_list[i][1] += 1 

        else:
            if robot_list[i][0] + width < 0 or robot_list[i][0] > 640:
                robot_list[i] = [random.randint(0, 590), random.randint(-1 * height * 5,  -1 * height)]
            elif robot_list[i][0] > 320:
                robot_list[i][0] += 1
            else:
                robot_list[i][0] -= 1
    
        
    window.fill((0, 0, 0))
    for i in range(robot_quantity):
        window.blit(robot, (robot_list[i][0], robot_list[i][1]))
    pygame.display.flip()

    clock.tick(60)