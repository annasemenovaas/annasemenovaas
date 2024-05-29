from pygame import *

win_width = 700
win_height = 500
background = (200, 255, 255)
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
window.fill(background)

clock = time.Clock()
FPS = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] :
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] :
            self.rect.y += self.speed
    def updatel(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] :
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed

player1 = Player('racket.png', 5, win_height-100,50,150, 10 )
player2 = Player('racket.png', 645, win_height+100,50,150, 10 )

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((200,255,255))
    player1.update()
    player2.updatel()
    player1.reset()
    player2.reset()
    display.update()
    clock.tick(FPS)        


