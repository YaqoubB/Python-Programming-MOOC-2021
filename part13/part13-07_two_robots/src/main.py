
# WRITE YOUR SOLUTION HERE:

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
 
x1 = 0
y1 = 0
x2 = 0
y2 = 0
speed = 1
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot1, (x1, y1 + 86))
    screen.blit(robot2, (x2, y2 + 172))
    pygame.display.flip()

    x1 += velocity
    x2 += speed * 2

    if x1+robot1.get_width() >= width:
        velocity = -velocity
    if velocity < 0 and x1 <= 0:
        velocity = -velocity

    if x2+robot2.get_width() >= width:
        speed = -speed 
    if speed < 0 and x2 <= 0:
        speed = -speed

    clock.tick(60)