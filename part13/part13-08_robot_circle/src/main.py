
# WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

angle = 0
clock = pygame.time.Clock()

flag1 = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if flag1:
        window.fill((0, 0, 0))
        for i in range(10):
            x = 320-robot.get_width()/2+math.cos(angle + (i * 0.628))*150
            y = 240-robot.get_height()/2+math.sin(angle + (i * 0.628))*150
            window.blit(robot, (x, y))

    pygame.display.flip()
    angle += 0.01
    clock.tick(60)