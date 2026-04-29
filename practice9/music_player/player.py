import pygame
import os  # для работы с файлами и папками

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()  # включаем звуковую систему pygame
        
        # папка с музыкой
        self.music_folder = music_folder
        
        # загружаем список треков
        self.playlist = self.load_music()
        
        # индекс текущего трека
        self.current_index = 0
        
        # флаг: играет ли сейчас музыка
        self.is_playing = False

    def load_music(self):
        files = []
        
        # перебираем все файлы в папке
        for file in os.listdir(self.music_folder):
            
            # оставляем только mp3 и wav
            if file.endswith(".mp3") or file.endswith(".wav"):
                # сохраняем полный путь к файлу
                files.append(os.path.join(self.music_folder, file))
        
        return files  # возвращаем список треков

    def play(self):
        # если нет треков — ничего не делаем
        if not self.playlist:
            print("No music files found.")
            return

        # берём текущий трек
        track = self.playlist[self.current_index]
        
        # загружаем и запускаем музыку
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        
        self.is_playing = True
        
        # выводим название файла (без пути)
        print(f"Now playing: {os.path.basename(track)}")

    def stop(self):
        # останавливаем музыку
        pygame.mixer.music.stop()
        
        self.is_playing = False
        print("Playback stopped.")

    def next_track(self):
        # если список пуст — выходим
        if not self.playlist:
            return

        # переходим к следующему треку (с зацикливанием)
        # % len(...) — чтобы после последнего вернуться к первому
        self.current_index = (self.current_index + 1) % len(self.playlist)
        
        self.play()  # запускаем новый трек

    def prev_track(self):
        # если список пуст — выходим
        if not self.playlist:
            return

        # переходим к предыдущему треку (с зацикливанием)
        self.current_index = (self.current_index - 1) % len(self.playlist)
        
        self.play()  # запускаем новый трек