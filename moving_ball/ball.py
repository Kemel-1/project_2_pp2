import pygame  # подключаем библиотеку pygame для графики и игр

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        # начальная позиция мяча
        self.x = x
        self.y = y
        
        # радиус мяча
        self.radius = radius
        
        # скорость движения (на сколько пикселей двигается за шаг)
        self.speed = 20
        
        # размеры экрана (нужны, чтобы не выходить за границы)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, direction):
        # движение влево
        if direction == "LEFT":
            # проверяем, не выйдет ли мяч за левую границу
            if self.x - self.speed - self.radius >= 0:
                self.x -= self.speed

        # движение вправо
        elif direction == "RIGHT":
            # проверяем правую границу
            if self.x + self.speed + self.radius <= self.screen_width:
                self.x += self.speed

        # движение вверх
        elif direction == "UP":
            # проверяем верхнюю границу
            if self.y - self.speed - self.radius >= 0:
                self.y -= self.speed

        # движение вниз
        elif direction == "DOWN":
            # проверяем нижнюю границу
            if self.y + self.speed + self.radius <= self.screen_height:
                self.y += self.speed

    def draw(self, screen):
        # рисуем круг (мяч) на экране
        # (255, 0, 0) — это красный цвет (RGB)
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)