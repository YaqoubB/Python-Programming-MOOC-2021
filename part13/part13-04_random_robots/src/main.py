# WRITE YOUR SOLUTION HERE:

import pygame
import random


pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
screen.fill((0, 0, 0))


for i in range(1000):
    screen.blit(robot, (random.randint(0, 590) , random.randint(0, 394)))
    pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()