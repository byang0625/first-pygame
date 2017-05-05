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
