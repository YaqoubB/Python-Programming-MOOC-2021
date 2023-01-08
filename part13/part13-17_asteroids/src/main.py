# WRITE YOUR SOLUTION HERE:


import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")
game_font = pygame.font.SysFont("Arial", 24)

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

black = (0, 0, 0)
window.fill(black)

robot_height = robot.get_height() #86
robot_width = robot.get_width() #50
rock_height = rock.get_height() #40
rock_width = rock.get_width() #40    

x = 0
y = 480 - robot_height


to_right = False
to_left = False

speed = 4
score = 0

multiplier = -30
rock_quantity = 5



def rock_xy():
    return [random.randint(0, 600), random.randint(multiplier * rock_height,  -1 * rock_height)]

def rock_spawner():
    list1 = []
    list1.append(rock_xy())
    counter = 0
    while counter < rock_quantity:
        rock = rock_xy()
        for i in list1:
            if i[0] <= rock[0] <= (i[0] + rock_width) and i[1] <= rock[1] <= (i[1] + rock_height) or i[0] <= (rock[0] + rock_width) <= (i[0] + rock_width) and i[1] <= (rock[1] + rock_height) <= (i[1] + rock_height): #emphasis on top left and bottom right
                break

            list1.append(rock)
            counter += 1
            break
    return list1

rock_list = rock_spawner()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if to_right and x + robot.get_width() <= 640:
        x += speed
    if to_left and x >= 0:
        x -= speed
    
    rock_respawner = rock_spawner()
    for i in range(rock_quantity):
        rock_list[i][1] += 1 

        if rock_list[i][1] + rock_height > 480:
            rock_list[i] = rock_respawner.pop()
            exit()
                                                                    
        if x <= rock_list[i][0] <= (x + robot_width) and y <= rock_list[i][1] + rock_height <= (y + robot_height) or x <= rock_list[i][0] + rock_width <= (x + robot_width) and y <= rock_list[i][1] + rock_height <= (y + robot_height): #emphasis top left and top right
            score += 1
            window.fill((0, 0, 0))
            rock_list[i] = rock_respawner.pop()
            window.blit(rock, (rock_list[i][0], rock_list[i][1]))
            pygame.display.flip()


    window.fill((0,0,0))
    window.blit(robot, (x , y))
    for i in range(rock_quantity):
        window.blit(rock, (rock_list[i][0], rock_list[i][1]))
    text = game_font.render(f"Points: {score}", True, (255, 0, 0))
    window.blit(text, (500, 10))
    pygame.display.flip()
    
    clock.tick(60)