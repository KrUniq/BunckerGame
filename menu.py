import sys

import pygame
from button import Button
from settings import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        # Загрузка и масштабирование фонового изображения
        self.background = pygame.image.load('assets/images/bunker_menu.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))  # Масштабирование изображения под размер окна
        # Вычисление центра экрана
        screen_center_x = WIDTH // 2

        # Определение размеров и положения кнопок
        button_width = 300
        button_height = 100
        button_spacing = 20

        button_y = 200
        self.buttons = [
            Button("Начать игру", (screen_center_x - button_width // 2, button_y), (button_width, button_height),
                   self.start_game),
            Button("Правила", (screen_center_x - button_width // 2, button_y + button_height + button_spacing),
                   (button_width, button_height), self.show_rules),
            Button("Выйти из игры",
                   (screen_center_x - button_width // 2, button_y + 2 * (button_height + button_spacing)),
                   (button_width, button_height), self.exit_game)
        ]
        # Состояние по умолчанию
        self.new_state = 'menu'

    def draw(self):
        # Отрисовка фона и кнопок
        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(self.screen)
            self.new_state = 'menu'

    def process_events(self):
        # Обработка ввода событий
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Изменение размера окна при его растягивании
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        for button in self.buttons:
            button.update(event_list)
        return self.new_state

    def start_game(self):
        self.new_state = 'start_game'

    def show_rules(self):
        self.new_state = 'rules'

    def exit_game(self):
        pygame.quit()
        sys.exit()