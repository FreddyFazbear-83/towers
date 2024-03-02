import pygame
import sys

# Инициализация pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Передвижение предмета по клику мыши")

# Загрузка изображения
image = pygame.image.load('nefrit.ico')
image_rect = image.get_rect()

# Установка начальной позиции предмета
image_rect.center = (200, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            image_rect.center = event.pos

    # Отрисовка
    screen.fill(WHITE)
    screen.blit(image, image_rect)
    
    pygame.display.flip()

# Завершение работы pygame
pygame.quit()
sys.exit()
