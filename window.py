from pygame import *
from pygame import image, transform

window = display.set_mode((500, 700))
display.set_caption('Пінг-Понг')
background = transform.scale(image.load("blue-clouds-day-fluffy-53594.webp"), (500, 700))

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, size_x, size_y, speed_x, speed_y=0):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(image_name), (size_x, size_y))
        self.speed_x = speed_x
        self.speed_y = speed_y
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        pass

class Player(GameSprite):
    def update(self):
        pass

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_x

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_x

class Ball(GameSprite):
    def update(self):
        global score_left, score_right

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > 700 - self.rect.height or self.rect.y < 0:
            self.speed_y *= -1

        
        if self.rect.colliderect(rakcet1.rect):
            self.speed_x *= -1

        if self.rect.colliderect(rakcet2.rect):
            self.speed_x *= -1

        
        if self.rect.x > 500 - self.rect.width:
            score_left += 1
            self.rect.x = 250
            self.rect.y = 350
            self.speed_x *= -1

        if self.rect.x < 0:
            score_right += 1
            self.rect.x = 250
            self.rect.y = 350
            self.speed_x *= -1

rakcet1 = Player("ice-cream-stick-72w51G6-600-removebg-preview.png", 30, 300, 20, 100, 5)
rakcet2 = Player("ice-cream-stick-72w51G6-600-removebg-preview.png", 450, 300, 20, 100, 5)
ball = Ball("ping-pong.png", 250, 350, 20, 20, 3, 3)

score_left = 0
score_right = 0

clock = time.Clock()
FPS = 60

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    rakcet1.update_l()
    rakcet2.update_r()
    rakcet1.reset()
    rakcet2.reset()

    ball.update()
    ball.reset()

   
    
    if score_left == 5 or score_right == 5:
        game_over_font = font.Font(None, 72)
        if score_left == 5:
            game_over_text = game_over_font.render("Left Player Wins!", True, (255, 255, 255))
        else:
            game_over_text = game_over_font.render("Right Player Wins!", True, (255, 255, 255))
        window.blit(game_over_text, (50, 300))

    display.update()
    clock.tick(FPS)

