import pygame
from game import Game
from menu import Menu
from rules import Rules
from settings import *

def main():
    # Инициализация библиотеки Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Bunker Game")
    clock = pygame.time.Clock() # Создание объекта часов для контроля FPS
    # Инициализация экземпляров для различных состояний игры
    menu = Menu(screen)
    game = Game(screen)
    rules = Rules(screen)
    game_state = 'menu'

    while True:
        # Ограничение FPS
        clock.tick(FPS)
        if game_state == 'menu':
            new_state = menu.process_events()

            if new_state == 'start_game':
                game_state = 'start_game'
            elif new_state == 'rules':
                game_state = 'rules'
            # Отрисовка меню
            menu.draw()

        elif game_state == 'start_game':
            new_state = game.process_events()
            game.update()
            game.draw() # Отрисовка игры
            if new_state == 'menu':
                game_state = 'menu'
            elif new_state == 'end_game':
                game_state = 'end_game'

        elif game_state == 'rules':
            new_state = rules.process_events()
            if new_state == 'menu':
                game_state = 'menu'
            rules.draw()  # Отрисовка правил
        elif game_state == 'end_game':
            game.end_game()
            # Обновление дисплея после всех изменений
        pygame.display.flip()

if __name__ == "__main__":
    main()