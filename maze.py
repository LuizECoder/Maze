from pygame import *

window = display.set_mode((700, 500))
background = transform.scale(image.load("background.jpg"), (700, 500))
display.set_caption("Maze Game")
window.blit(background, (0, 0))

class Game(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game):

    def movement(self):
        Pressed = key.get_pressed()

        if Pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if Pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
        if Pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if Pressed[K_d] and self.rect.x < 695:
            self.rect.x += self.speed

class Enemy(Game):
    side = "left"
    def Move_LR(self):
        if self.rect.x < 400:
            self.side = "right"
        if self.rect.x > 650:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        if self.side == "right":
            self.rect.x += self.speed

    side = "down"
    def Move_UD(self):
        if self.rect.y <= 10:
            self.side = "down"
        if self.rect.y >= win_height - 20:
            self.side = "up"
        if self.side == "down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

class wall(sprite.Sprite):
    def __init__(self ,color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color1, color2, color3))
 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    



Player = Player("hero.png", 50, 300, 5)
Enemy1 = Enemy("cyborg.png", 620, 300, 3)
treasure_chest = Game("treasure.png", 550, 450, 0)

wall1 = wall(154, 205, 50, 500, 300 , 10, 450)

font.init()
font = font.Font(None, 100)
win = font.render('Victory', True, (255, 215, 0))
lose = font.render('Game Over', True, (180, 0, 0))

clock = time.Clock()
fps = 60

mixer.init()
mixer.music.load("onrepeat.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

play = True
Finish = False
win_height = 500

while play:
    for i in event.get():
        if i.type== QUIT:
            play = False

    if Finish != True:
        window.blit(background, (0, 0))
        Player.movement()
        Enemy1.Move_LR()
        Player.draw()
        Enemy1.draw()
        wall1.draw()

        if sprite.collide_rect(Player, wall1):
            Finish = True
            window.blit(lose, (50, win_height/2))
            
            
        if sprite.collide_rect(Player, treasure_chest):
            Finish = True
            window.blit(win, (50, win_height/2))
            money.play()
    
    display.update()
    clock.tick(fps)




