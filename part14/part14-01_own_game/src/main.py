# Complete your game here

import pygame
import random

class Robot(pygame.Rect):  #avoided using Rect class properties
    def __init__(self):
        super().__init__(0, 394, 50, 86)
        self.to_right = False
        self.to_left = False
        self.speed = 4

class Monster(pygame.Rect):
    def __init__(self):
        super().__init__(0, 0, 50, 70)
        self.quantity = 3
        self.speed = 1

class Coin(pygame.Rect):
    def __init__(self):
        super().__init__(0, 0, 40, 40)
        self.quantity = 5
        self.speed = 1

class Door(pygame.Rect):
    def __init__(self):
        super().__init__(0, 0, 50, 70)
        self.portal_1 = (50, 410)
        self.portal_2 = (540, 410)
        self.open = False


class RainOfCoins:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.goal = 25
        self.robot = Robot()
        self.monster = Monster()
        self.coin = Coin()
        self.door = Door()
        self.game_state = False
        self.tips = False
        self.multiplier = 15     #used to determine how far an object can spawn vertically off screen

        self.object_list = self.spawner()
        self.coin_list = self.object_list[:self.coin.quantity] 
        self.monster_list = self.object_list[-self.monster.quantity:]

        self.load_images()

        self.window = pygame.display.set_mode((640, 530))
        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("A Rain of Coins")

        self.main_loop()


    def load_images(self):  #list containing images ready to be blit
        self.images = []
        for name in ["robot", "coin", "monster", "door"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        RainOfCoins()

    def game_solved(self):
        if self.score >= self.goal:
            return True
        return False
    
    def game_lost(self):
        if self.game_state:
            return True
        return False
    
    def teleport(self): #teleport from one portal to the other
        if self.game_solved():
            return
        if self.game_lost():
            return
        sky = (204, 229, 255)
        x = self.robot.left 
        y = self.robot.top
        portal_1 = self.door.portal_1
        portal_2 = self.door.portal_2
        r_width = self.robot.width
        if x <= portal_1[0] <= (x + r_width) or x <= portal_1[0] + self.door.width <= (x + r_width): #check if portal_1 width overlaps robot
            self.door.open = False
            self.robot.left = portal_2[0]
            self.window.fill(sky)
            self.window.blit(self.images[0], (x, y))

        elif x <= portal_2[0] <= (x + r_width) or x <= portal_2[0] + self.door.width <= (x + r_width): #check if portal_2 width overlaps robot
            self.door.open = False
            self.robot.left  = portal_1[0]
            self.window.fill(sky)
            self.window.blit(self.images[0], (x, y))


    def spawner(self): #generates coordinates for objects without overlaps
        m_width = Monster().width
        m_height = Monster().height
        quantity = self.coin.quantity + self.monster.quantity

        def spawn_xy():
            return [random.randint(0, 590), -1 * random.randint(m_height , self.multiplier * m_height)]
        list1 = []

        list1.append(spawn_xy())
        counter = 1
        while counter < quantity: 
            object = spawn_xy()
            for i in list1:
                if i[0] <= object[0] <= (i[0] + m_width) and i[1] <= object[1] <= (i[1] + m_height):#collision check on top left
                    break
                if i[0] <= (object[0] + m_width) <= (i[0] + m_width) and i[1] <= object[1] <= (i[1] + m_height): #collision check on top right
                    break
                if i[0] <= object[0] <= (i[0] + m_width) and i[1] <= (object[1] + m_height) <= (i[1] + m_height): #collision check on bottom left
                    break
                if i[0] <= (object[0] + m_width) <= (i[0] + m_width) and i[1] <= (object[1] + m_height) <= (i[1] + m_height): #collision check on bottom right
                    break

                list1.append(object)
                counter += 1
                break
        return list1

    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            self.draw_window()
            self.move()
            
            clock.tick(60)

    def check_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.robot.to_left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.robot.to_right = True

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.door.open = True
                    self.teleport()

                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_SPACE:
                    self.tips = True
                                               
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.robot.to_left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.robot.to_right = False

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.door.open = False

                if event.key == pygame.K_SPACE:
                    self.tips = False

    def move(self): #robot movement
        if self.game_solved():
            return
        if self.game_lost():
            return
        if self.robot.to_right and self.robot.left + self.robot.width <= 640:
            self.robot.left += 4
        if self.robot.to_left and self.robot.left >= 0:
            self.robot.left -= 4

    def draw_window(self):
        black = (0, 0, 0)
        sky = (204, 229, 255)
        respawner = self.spawner() #couldn't fix objects overlapping due to list being refreshed too quickly 
        x = self.robot.left     
        y = self.robot.top
        r_width = self.robot.width
        r_height = self.robot.height


        c_width = self.coin.width
        c_height = self.coin.height
        for i in range(self.coin.quantity):
            self.coin_list[i][1] += self.coin.speed 

            if self.coin_list[i][1] + c_height > 480:
                self.coin_list[i] = respawner.pop()
                self.game_state = True

            #robot coin collision                  
            if x <= self.coin_list[i][0] <= (x + r_width) and y <= self.coin_list[i][1] + c_height <= (y + r_height) or x <= self.coin_list[i][0] + c_width <= (x + r_width) and y <= self.coin_list[i][1] + c_height <= (y + r_height): #emphasis on bottom left and bottom right coin coordinates
                self.score += 1
                self.window.fill(sky)
                self.coin_list[i] = respawner.pop()
                self.window.blit(self.images[1], (self.coin_list[i][0], self.coin_list[i][1]))


        m_width = self.monster.width
        m_height = self.monster.height
        n1 = 6
        n2 = 12
        for i in range(self.monster.quantity):
            self.monster_list[i][1] += self.monster.speed 

            if self.monster_list[i][1] > 480:
                self.monster_list[i] = respawner.pop()

            #robot monster collision and lowering robot hitbox detection to reduce invisible contact with ghosts   
            top_left = x + n1 <= self.monster_list[i][0] <= (x + r_width - n1) and y + n2 <= self.monster_list[i][1] <= (y + r_height - n2)
            top_right = x + n1 <= self.monster_list[i][0] + m_width <= (x + r_width - n1) and y + n2 <= self.monster_list[i][1] <= (y + r_height - n2)
            bottom_left = x + n1 <= self.monster_list[i][0] <= (x + r_width - n1) and y + n2 <= self.monster_list[i][1] + m_height <= (y + r_height - n2)
            bottom_right = x + n1 <= self.monster_list[i][0] + m_width <= (x + r_width - n1)  and y + n2 <= self.monster_list[i][1] + m_height <= (y + r_height - n2)          
            if  top_left or top_right or bottom_left or bottom_right: 
                self.window.fill(sky)
                self.monster_list[i] = respawner.pop()
                self.window.blit(self.images[2], (self.monster_list[i][0], self.monster_list[i][1]))
                self.game_state = True


        self.window.fill(sky)
        self.window.blit(self.images[0], (x , y))
        self.window.blit(self.images[3], (self.door.portal_1[0], self.door.portal_1[1]))
        self.window.blit(self.images[3], (self.door.portal_2[0], self.door.portal_2[1]))

        for i in range(self.coin.quantity):
            self.window.blit(self.images[1], (self.coin_list[i][0], self.coin_list[i][1]))
        for i in range(self.monster.quantity):
            self.window.blit(self.images[2], (self.monster_list[i][0], self.monster_list[i][1]))

        text = self.game_font.render(f"Points: {self.score}/{self.goal}", True, (255, 0, 0))
        self.window.blit(text, (495, 10))

        pygame.draw.rect(self.window, black, (0, 480, 640, 50))
        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (25, 490))
        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (225, 490))
        game_text = self.game_font.render("Spacebar = tips", True, (255, 0, 0))
        self.window.blit(game_text, (420, 490))

        
        if self.game_solved():
            self.coin.speed = 0
            self.monster.speed = 0
            self.tips = False

            game_text = self.game_font.render("Congratulations, you have won!", True, (255, 0, 0))
            game_text_x = 320 - game_text.get_width() // 2
            game_text_y = 240 - game_text.get_height() // 2
            pygame.draw.rect(self.window, black, (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))

        if self.game_lost(): 
            self.coin.speed = 0
            self.monster.speed = 0
            self.tips = False

            game_text = self.game_font.render("You have lost!", True, (255, 0, 0))
            game_text_x = 320 - game_text.get_width() // 2
            game_text_y = 240 - game_text.get_height() // 2
            pygame.draw.rect(self.window, black, (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))

        text_height = 28
        if self.tips:
            height = 116
            game_text = self.game_font.render(f"Collect a total of {self.goal} coins to win!", True, (255, 0, 0))
            self.window.blit(game_text, (149, height))
            game_text = self.game_font.render(f"Left/Right/A/D keys to move, Up/W keys at portals", True, (255, 0, 0))
            self.window.blit(game_text, (54, height + text_height * 2))
            game_text = self.game_font.render(f"Use portals to avoid tricky situations!", True, (255, 0, 0))
            self.window.blit(game_text, (126, height + text_height * 4))  
            game_text = self.game_font.render(f"If a coin touches the floor, it's Game Over!", True, (255, 0, 0))
            self.window.blit(game_text, (96, height+ text_height * 6))
            game_text = self.game_font.render(f"Avoid touching the ghosts or you'll lose!", True, (255, 0, 0))
            self.window.blit(game_text, (111, height + text_height * 8))  

        pygame.display.flip()


if __name__ == "__main__":
    RainOfCoins()