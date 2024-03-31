from pygame import *
from pygame import image, transform, font

# Ініціалізація Pygame та шрифтів
init()
font.init()

window = display.set_mode((1366, 768))
display.set_caption('Пінг-Понг')
background = transform.scale(image.load("bakaka.png"), (1366, 768))

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
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed_x
            
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_x
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed_x

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

# Створення гравців та м'яча
rakcet1 = Player("aratata-removebg-preview.png", 10, 300, 90, 100, 5)
rakcet2 = Player("aratata-removebg-preview.png", 430, 300, 90, 100, 5)
ball = Ball("djumaysimba-removebg-preview.png", 1050, 350, 30, 40, 6, 3)

# Ініціалізація змінних для лічильників очок
score_left = 0
score_right = 0

# Ініціалізація годинника та FPS
clock = time.Clock()
FPS = 60

# Змінна для стану гри
game_over = False

game_over = False

# Головний цикл гри
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()  # Завершуємо програму при натисканні на кнопку закриття вікна

    window.blit(background, (0, 0))

    # Оновлення гравців та м'яча
    rakcet1.update_l()
    rakcet2.update_r()
    rakcet1.reset()
    rakcet2.reset()
    ball.update()
    ball.reset()

    # Відображення кінцевого екрану, якщо хтось виграв
    if score_left == 5 or score_right == 5:
        game_over_font = font.Font(None, 72)
        if score_left == 5:
            game_over_text = game_over_font.render("Left Player Wins! Натисніть SPACE щоб продовжити", True, (255, 255, 255))
        else:
            game_over_text = game_over_font.render("Right Player Wins! Натисніть SPACE щоб продовжити", True, (255, 255, 255))
        window.blit(game_over_text, (10, 300))
        display.update()

        # Очікуємо натискання SPACE для початку нової гри
        wait_for_space = True
        while wait_for_space:
            for e in event.get():
                if e.type == KEYDOWN and e.key == K_SPACE:
                    score_left = 0
                    score_right = 0
                    rakcet1 = Player("aratata-removebg-preview.png", 10, 300, 90, 100, 5)
                    rakcet2 = Player("aratata-removebg-preview.png", 430, 300, 90, 100, 5)
                    ball = Ball("djumaysimba-removebg-preview.png", 250, 350, 30, 20, 3, 3)
                    wait_for_space = False  # Закінчити очікування
                    game_over = False  # Почати нову гру

    display.update()
    clock.tick(FPS)
