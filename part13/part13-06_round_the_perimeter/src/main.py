# # WRITE YOUR SOLUTION HERE:

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = 0
y = 0
speed = 0
velocity = 1
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity
    y += speed

    if x+robot.get_width() >= width:
        velocity = 0
        speed = 1
    if y+robot.get_height() >= height:
        speed = 0
        velocity = -1
    if x <= 0:
        speed = -1
        velocity = 0
    if y <= 0 and speed < 0:
        speed = 0
        velocity = 1

    clock.tick(60)
