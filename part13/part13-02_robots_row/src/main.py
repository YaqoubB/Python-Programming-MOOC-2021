# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
window.blit(robot, (50 , 86))
window.blit(robot, (100 , 86))
window.blit(robot, (150 , 86))
window.blit(robot, (200 , 86))
window.blit(robot, (250 , 86))
window.blit(robot, (300 , 86))
window.blit(robot, (350 , 86))
window.blit(robot, (400 , 86))
window.blit(robot, (450 , 86))
window.blit(robot, (500 , 86))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()