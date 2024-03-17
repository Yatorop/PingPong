import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
width = 800
height = 600

# Створення вікна
screen = pygame.display.set_mode((width, height))

# Білий колір
WHITE = (255, 255, 255)

# Головний цикл програми
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заповнення екрана білим кольором
    screen.fill(WHITE)

    # Оновлення відображення
    pygame.display.flip()

