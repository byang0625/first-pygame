import pygame
from sys import exit
import random
from random import randint
#Bullet类
class Bullet():
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('blut.jpg').convert_alpha()
        self.active = False
    def move(self):
        # if self.y < 0:
        #     mousex,mousey = pygame.mouse.get_pos()
        #     self.x = mousex - self.image.get_width()/2
        #     self.y = mousey - self.image.get_height()/2
        # else:
        #     self.y -= 3
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False
    def restart(self):
        mousex,mousey = pygame.mouse.get_pos()
        self.x = mousex - self.image.get_width()/2
        self.y = mousey - self.image.get_height()/2
        self.active = True


#Enemy类
class Enemy():
    def restart(self):
        self.x = randint(30,370)
        self.y = randint(-200,-50)
        self.speed = random.random()+0.1
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('Enemy.jpg').convert_alpha()
    def move(self):
        if self.y < 700:
            self.y += self.speed
        else:
            self.restart()

#Plane类
class Plane():
    def restart(self):
        self.x = 200
        self.y = 600

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('plane.jpg').convert_alpha()

    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x
        self.y = y

pygame.init() #初始化pygame
screen = pygame.display.set_mode((400,700),0,32) #创建一个窗口
pygame.display.set_caption('Hello,World!') #设置窗口标题
background = pygame.image.load('bkimg.jpg') #加载并转换图像
# plane = pygame.image.load('plane.jpg')
# bullet = Bullet()
# enemy = Enemy()
bullets = [] #创建子弹的LIST
for i in range(5):
    bullets.append(Bullet())
count_b = len(bullets) #子弹总数
index_b = 0 #即将激活的子弹序号
interval_b = 0 #发射子弹的间隔

enemies = []
for i in range(5):
    enemies.append(Enemy())

#碰撞检测(子弹和敌机)
def checkHit(enemy,bullet):
    if(bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False

#碰撞检测（敌机和本机）
def checkCrash(enemy,plane):
    if (plane.x + 0.7*plane.image.get_width() > enemy.x) and (plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + 0.7*plane.image.get_height() > enemy.y ) and (plane.y + 0.3*plane.image.get_height() < enemy.y+ enemy.image.get_height()):
        return  True
    return False

score = 0
gameover = False
font = pygame.font.Font(None,32)

while True:
#游戏主循环
    plane = Plane()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     background = pygame.image.load('bkimg2.jpg')
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False
    screen.blit(background,(0,0))
    # bullet.move()
    # screen.blit(bullet.image,(bullet.x,bullet.y))

    if not gameover:
        interval_b -= 1  # 发射时间递减
        if interval_b < 0:
            bullets[index_b].restart()  # 当时间间隔小于0时激活一颗子弹
            interval_b = 100  # 重置时间间隔
            index_b = (index_b + 1) % count_b  # 子弹序号周期性递增
        for b in bullets:
            if b.active:
                for e in enemies:
                     if checkHit(e, b):
                         score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))

        for e in enemies:
            if checkCrash(e,plane):
                gameover = True
            e.move()
            screen.blit(e.image,(e.x,e.y))
        plane.move()
        screen.blit(plane.image,(plane.x,plane.y))
        text = font.render("Score:%d" % score, 1, (0, 0, 0))
        screen.blit(text, (0, 0))
    else:
        text = font.render("Score:%d" % score, 1, (0, 0, 0))
        screen.blit(text, (190, 400))
    # enemy.move()
    # screen.blit(enemy.image,(enemy.x,enemy.y))


    pygame.display.update()
