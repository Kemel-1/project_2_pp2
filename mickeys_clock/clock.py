import pygame
import time

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen

        # загрузка картинки руки
        self.hand_image = pygame.image.load("images/mickey_hand.png").convert_alpha()

        # центр экрана
        self.center = (300, 300)

        # масштаб (если нужно уменьшить/увеличить)
        self.hand_image = pygame.transform.scale(self.hand_image, (150, 150))

    def get_time(self):
        t = time.localtime()
        return t.tm_min, t.tm_sec

    def draw_hand(self, image, angle, offset):
        # вращаем изображение
        rotated = pygame.transform.rotate(image, angle)

        rect = rotated.get_rect(center=(
            self.center[0] + offset[0],
            self.center[1] + offset[1]
        ))

        self.screen.blit(rotated, rect)

    def update(self):
        self.min, self.sec = self.get_time()

    def draw(self):
        # перевод времени в углы

        # 60 секунд = 360°
        sec_angle = -self.sec * 6

        # 60 минут = 360°
        min_angle = -self.min * 6

        # левая рука = секундная
        self.draw_hand(self.hand_image, sec_angle, (-50, 0))

        # правая рука = минутная
        self.draw_hand(self.hand_image, min_angle, (50, 0))