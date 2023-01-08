# WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x1 = robot.get_width()
y1 = robot.get_height()

x2 = 640 - robot.get_width() * 2
y2 = 480 - robot.get_height() * 2

to_right_p1 = False
to_left_p1 = False
to_up_p1 = False
to_down_p1 = False

to_right_p2 = False
to_left_p2 = False
to_up_p2 = False
to_down_p2 = False

speed = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left_p1 = True
            if event.key == pygame.K_a:
                to_left_p2 = True
            if event.key == pygame.K_RIGHT:
                to_right_p1 = True
            if event.key == pygame.K_d:
                to_right_p2 = True
            if event.key == pygame.K_UP:
                to_up_p1 = True
            if event.key == pygame.K_w:
                to_up_p2 = True
            if event.key == pygame.K_DOWN:
                to_down_p1 = True
            if event.key == pygame.K_s:
                to_down_p2 = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left_p1 = False
            if event.key == pygame.K_a:
                to_left_p2 = False
            if event.key == pygame.K_RIGHT:
                to_right_p1 = False
            if event.key == pygame.K_d:
                to_right_p2 = False
            if event.key == pygame.K_UP:
                to_up_p1 = False
            if event.key == pygame.K_w:
                to_up_p2 = False
            if event.key == pygame.K_DOWN:
                to_down_p1 = False
            if event.key == pygame.K_s:
                to_down_p2 = False


    if to_right_p1 and x1 + robot.get_width() <= 640:
        x1 += speed
    if to_right_p2 and x2 + robot.get_width() <= 640:
        x2 += speed
    if to_left_p1 and x1 >= 0:
        x1 -= speed
    if to_left_p2 and x2 >= 0:
        x2 -= speed
    if to_up_p1 and y1 >= 0:
        y1 -= speed
    if to_up_p2 and y2 >= 0:
        y2 -= speed
    if to_down_p1 and y1 + robot.get_height() <= 480:
        y1 += speed
    if to_down_p2 and y2 + robot.get_height() <= 480:
        y2 += speed

    window.fill((0,0,0))
    window.blit(robot, (x1 , y1))
    window.blit(robot, (x2 , y2))

    pygame.display.flip()
    
    clock.tick(60)