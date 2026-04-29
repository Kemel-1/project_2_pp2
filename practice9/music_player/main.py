import pygame
from player import MusicPlayer
import os

pygame.init()  # инициализация pygame

# создаём окно
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Music Player")

# шрифт для текста
font = pygame.font.SysFont(None, 30)

# создаём плеер (папка music должна быть рядом с файлом)
player = MusicPlayer("music")

running = True
clock = pygame.time.Clock()

def format_time(ms):
    # перевод миллисекунд в минуты:секунды
    seconds = ms // 1000
    m = seconds // 60
    s = seconds % 60
    return f"{m}:{s:02}"  # формат 0:05, 1:23

# главный цикл
while running:
    # очищаем экран (чёрный фон)
    screen.fill((0, 0, 0))

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # управление с клавиатуры
            if event.key == pygame.K_p:
                player.play()         # воспроизведение
            elif event.key == pygame.K_s:
                player.stop()         # стоп
            elif event.key == pygame.K_n:
                player.next_track()   # следующий трек
            elif event.key == pygame.K_b:
                player.prev_track()   # предыдущий трек
            elif event.key == pygame.K_q:
                running = False       # выход

    # 🎵 текущий трек
    if player.playlist:
        # берём только имя файла без пути
        track = os.path.basename(player.playlist[player.current_index])
    else:
        track = "No music"

    # рисуем текст с названием трека
    text = font.render(f"Now Playing: {track}", True, (255, 255, 255))
    screen.blit(text, (50, 50))

    # ⏱️ текущее время воспроизведения
    pos = pygame.mixer.music.get_pos()  # время в миллисекундах

    time_text = font.render(f"Time: {format_time(pos)}", True, (255, 255, 0))
    screen.blit(time_text, (50, 100))

    # 📊 прогресс-бар
    bar_x = 50
    bar_y = 150
    bar_width = 500
    bar_height = 20

    # фон полоски (серый)
    pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))

    # рассчитываем прогресс
    # 180000 мс = 3 минуты (это просто условное значение)
    progress = (pos / 180000) * bar_width

    # зелёная часть (пройденное время)
    pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, progress, bar_height))

    # обновляем экран
    pygame.display.update()

    # ограничение FPS (30 кадров в секунду)
    clock.tick(30)

pygame.quit()  # корректное завершение pygame