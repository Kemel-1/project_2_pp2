import pygame  # библиотека для создания игр
import sys     # нужен для корректного выхода из программы
from ball import Ball  # импортируем наш класс мяча из файла ball.py

pygame.init()  # инициализация всех модулей pygame

# размеры окна
WIDTH, HEIGHT = 800, 600

# создаём игровое окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# создаём объект мяча (по центру экрана)
ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT)

# объект для контроля FPS (частоты кадров)
clock = pygame.time.Clock()

# главный игровой цикл (работает бесконечно)
while True:
    # обрабатываем события (нажатия, закрытие окна и т.д.)
    for event in pygame.event.get():
        
        # если нажали крестик (закрытие окна)
        if event.type == pygame.QUIT:
            pygame.quit()  # закрываем pygame
            sys.exit()     # полностью завершаем программу

        # если нажата клавиша
        if event.type == pygame.KEYDOWN:
            
            # проверяем, какая именно клавиша нажата
            if event.key == pygame.K_LEFT:
                ball.move("LEFT")   # двигаем мяч влево

            elif event.key == pygame.K_RIGHT:
                ball.move("RIGHT")  # вправо

            elif event.key == pygame.K_UP:
                ball.move("UP")     # вверх

            elif event.key == pygame.K_DOWN:
                ball.move("DOWN")   # вниз

    # заливаем экран белым цветом (очистка кадра)
    screen.fill((255, 255, 255))

    # рисуем мяч
    ball.draw(screen)

    # обновляем экран (показываем всё, что нарисовали)
    pygame.display.flip()

    # ограничиваем до 60 кадров в секунду
    clock.tick(60)