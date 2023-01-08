# WRITE YOUR SOLUTION HERE:


import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
height = robot.get_height()
width = robot.get_width()

x = random.randint(0, 640 - width)
y = random.randint(0, 480 - height)

window.blit(robot, (x , y))
pygame.display.flip()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x = event.pos[0]
            m_y = event.pos[1]
            if  x <= m_x <= (x + width)  and y <= m_y <= (y + height):
                window.fill((0, 0, 0))
                x = random.randint(0, 640 - width)
                y = random.randint(0, 480 - height)
                window.blit(robot, (x, y))
                pygame.display.flip()

    clock.tick(60)


