from pygame import *
font.init()

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

speed_x = 3
speed_y = 3

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
        if key_pressed[K_w] :
            self.rect.y -= self.speed
        if key_pressed[K_s] :
            self.rect.y += self.speed
    def updatel(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] :
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]:
            self.rect.y += self.speed


player1 = Player('racket.png', 5, win_height-100,50,150, 10 )
player2 = Player('racket.png', 645, win_height-50,50,150, 10 )
ball = GameSprite('tenis_ball.png', 250, 250, 50,50,4 )

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSEEE!', True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSEEE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((200,255,255))
        player1.update()
        player2.updatel()
        player1.reset()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1 
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width-50:
            finish = True
            window.blit(lose2, (200, 200))   
        
    display.update()
    clock.tick(FPS)     


