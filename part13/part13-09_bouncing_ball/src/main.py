# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

diameter = ball.get_width()  #diameter = 50

x = 320 - (diameter / 2)
y = 240 - (diameter / 2)
x_velocity = 2
y_velocity = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity

    if y + diameter >= 480 or y < 0:
        y_velocity *= -1
    
    if x + diameter >= 640 or x < 0:
        x_velocity *= -1

    clock.tick(60)