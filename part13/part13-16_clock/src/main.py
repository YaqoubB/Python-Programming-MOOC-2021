# WRITE YOUR SOLUTION HERE:


import pygame
import math
import datetime

pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))
red = (255, 0, 0)
dark_blue = (0, 51, 204)
blue = (0, 102, 204)
light_blue =  (51, 153, 255)

center = (320, 240)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.set_caption(f'{datetime.datetime.now().strftime("%H:%M:%S")}')

    second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    hour = datetime.datetime.now().hour

    window.fill((0,0,0))
    pygame.draw.circle(window, red, center, 10)  #center circle
    pygame.draw.circle(window, red, center, 200, 4)  #outer circle

    #second
    pygame.draw.line(window, dark_blue, center, (320 + math.cos(math.pi/2 - (second/60 * 2 * math.pi)) * 190, 240 + math.sin(3 * math.pi/2 + (second/60 * 2 * math.pi)) * 190), 1)

    #minute
    pygame.draw.line(window, blue , center, (320 + math.cos(math.pi/2 - (minute/60 * 2 * math.pi)) * 170, 240 + math.sin(3 * math.pi/2 + (minute/60 * 2 * math.pi)) * 180), 2)

    #hour
    pygame.draw.line(window, light_blue, center, (320 + math.cos(math.pi/2 - (hour/12 * 2 * math.pi)) * 150, 240 + math.sin(3 * math.pi/2 + (hour/12 * 2 * math.pi)) * 150), 3)

    pygame.display.flip()

    clock.tick(60)