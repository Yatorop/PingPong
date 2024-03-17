from pygame import *

window = display.set_mode((500, 700))
display.set_caption('Пінг-Понг')
background = transform.scale(image.load("sky.jpg"), (500, 700))

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.init(self)
 
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_up(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 500 - 80:
            self.rect.x += self.speed

    def update_down(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 500 - 80:
            self.rect.x += self.speed


clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
