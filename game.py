import sys
import random
import pygame
from player import Player
from settings import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        # Загрузка и масштабирование фонового изображения
        self.background = pygame.image.load('assets/images/background.jpg')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))  # Масштабирование изоб

        self.players = []
        self.phase = "choose_players"
        self.chosen_catastrophe = None
        self.chosen_bunker = None
        self.new_state = 'start_game'
        self.players_chosen = False
        self.num_players = 0
        self.players_in_game = 0
        self.buttons = []

    def load_assets(self):
        # Загрузка ресурсов (изображений, звуков и т.д.)
        pass
    def update(self):  # Обновление состояния игры в зависимости от текущей фазы
        if self.phase == "choose_players":
            self.process_events()

    def draw(self):
        if self.phase == "choose_players":
            self.draw_choose_players_screen()

    def draw_choose_players_screen(self):
        # Отрисовка фона и запроса выбора количества игроков
        self.screen.fill((30, 30, 30))
        self.screen.blit(self.background, (0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("Выберите количество игроков (4-10):", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(text, text_rect)

        # Отображение кнопок выбора количества игроков
        button_width, button_height = 100, 50
        button_spacing = 20
        start_x = (self.screen.get_width() - (button_width + button_spacing) * 3) // 2
        start_y = 200
        for i in range(4, 11):  #
            button_rect = pygame.Rect(start_x + (button_width + button_spacing) * ((i - 4) % 3),
                                      start_y + (button_height + button_spacing) * ((i - 4) // 3), button_width,
                                      button_height)
            pygame.draw.rect(self.screen, (100, 100, 100), button_rect)
            button_text = font.render(str(i), True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.screen.blit(button_text, button_text_rect)

    def process_events(self):  # Обработка событий выхода из игры или нажатия мышью
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.phase == "choose_players":
                    self.handle_player_selection(event.pos)
                else:
                    self.handle_button_click(event.pos)

    def handle_player_selection(self, pos):
        #получение количества игроков по клику на кнопку
        button_width, button_height = 100, 50
        button_spacing = 20
        start_x = (self.screen.get_width() - (button_width + button_spacing) * 3) // 2
        start_y = 200
        for i in range(4, 11):
            button_rect = pygame.Rect(start_x + (button_width + button_spacing) * ((i - 4) % 3),
                                      start_y + (button_height + button_spacing) * ((i - 4) // 3), button_width,
                                      button_height)
            if button_rect.collidepoint(pos):
                self.num_players = i
                self.players_in_game = i
                self.phase = "draw_catastrophe_and_bunсker"
                self.choose_catastrophe()
                self.choose_bunker()
                self.start_game()
    def draw_catastrophe_and_bunker(self):
        self.screen.fill((30, 30, 30))
        # Отображение фонового изображения
        self.screen.blit(self.background, (0, 0))
        black_rect = pygame.Rect(30, 80, 800, 500)
        pygame.draw.rect(self.screen, (0, 0, 0), black_rect)
        font = pygame.font.Font(None, 24)

        # Отображение количества игроков
        players_text = font.render(f"Количество игроков: {self.num_players}", True, (255, 255, 255))
        players_text_rect = players_text.get_rect(center=(self.screen.get_width() // 2, 20))
        self.screen.blit(players_text, players_text_rect)

        # Отображение карточки катастрофы
        catastrophe_text = font.render(f"Описание катастрофы: {self.chosen_catastrophe}", True, (255, 255, 255))
        catastrophe_text_rect = catastrophe_text.get_rect(center=(self.screen.get_width() // 2, 40))
        self.screen.blit(catastrophe_text, catastrophe_text_rect)

        # Отображение карточки описания бункера
        bunker_text = font.render(f"Описание бункера: {self.chosen_bunker}", True, (255, 255, 255))
        bunker_text_rect = bunker_text.get_rect(center=(self.screen.get_width() // 2, 60))
        self.screen.blit(bunker_text, bunker_text_rect)


    def choose_catastrophe(self): # Случайный выбор сценария катастрофы
        self.chosen_catastrophe = random.choice([f"Катастрофа N{i}" for i in range(1,7)])

    def choose_bunker(self): # Случайный выбор описания бункера
        self.chosen_bunker = random.choice([f"Бункер N{i}" for i in range(1,7)])
        self.phase = "start_game"
        self.start_game()

    def start_game(self):
        # Добавляем выбранное количество игроков в список
        for i in range(self.num_players):
            player_name = f"Player {i + 1}"
            self.add_player(player_name)

        # Начинаем игру
        self.phase = "round"
        # Отображаем таблицу игроков
        self.draw_player_table()

    def draw_player_table(self):  # Подготовка к отображению таблицы игроков
        font = pygame.font.Font(None, 20)

        player_font = pygame.font.Font(None, 30)
        charc_font = pygame.font.Font(None, 26)

        self.draw_catastrophe_and_bunker()
        # Создаем список кнопок
        self.buttons = []

        # Отображение имен игроков в горизонтальной строке сверху
        player_x = 180
        for player_index in range(self.num_players):
            player_name_text = player_font.render(self.players[player_index].name, True, (255, 255, 255))
            player_name_text_rect = player_name_text.get_rect(center=(player_x, 150))
            self.screen.blit(player_name_text, player_name_text_rect)

            button_text = f"Показать N{player_index + 1}"
            button_rect = pygame.Rect(player_x - 50, 100, 100, 25)
            pygame.draw.rect(self.screen, (100, 100, 100), button_rect)
            button_text_surf = font.render(button_text, True, (255, 255, 255))
            button_text_rect = button_text_surf.get_rect(center=button_rect.center)
            self.screen.blit(button_text_surf, button_text_rect)

            self.buttons.append((button_rect, {"command": "show_all", "player_index": player_index}))
            player_x += 100

        # Отображение характеристик игроков в вертикальной колонке слева
        pygame.draw.line(self.screen, (128, 128, 128), [125, 150], [125, 510], 3)
        characteristic_y = 180
        for characteristic in ["Профессия", "Биология", "Здоровье", "Фобия", "Багаж", "Хобби", "Факт"]:
            characteristic_text = charc_font.render(characteristic, True, (255, 255, 255))
            characteristic_text_rect = characteristic_text.get_rect(center=(75, characteristic_y))
            self.screen.blit(characteristic_text, characteristic_text_rect)
            characteristic_y += 50

        # Отображение значений профессий для каждого игрока
        player_x = 180
        for player_index in range(self.num_players):
            player_y = 180
            characteristic_value = getattr(self.players[player_index], "profession")
            characteristic_text = font.render(characteristic_value, True, (255, 255, 255))
            characteristic_text_rect = characteristic_text.get_rect(center=(player_x, player_y))
            self.screen.blit(characteristic_text, characteristic_text_rect)
            player_y += 50
            player_x += 100
        self.show_characteristics()
        self.show_vote_buttons()
        self.show_votes()
        self.show_next_round()

        pygame.display.update()


    #  Отображение кнопок голосования
    def show_vote_buttons(self):
        if (self.players_in_game // 2) >= self.num_players:
            self.end_game()
            return
        pygame.draw.line(self.screen, (128, 128, 128), [150, 510], [1000, 510], 3)
        font = pygame.font.Font(None, 20)
        player_x = 130
        for player_index in range(self.num_players):
            vote_button_text = "vote"
            vote_button_rect = pygame.Rect(player_x+20, 520, 50, 30)
            pygame.draw.rect(self.screen, (150, 150, 150), vote_button_rect)
            vote_button_surf = font.render(vote_button_text, True, (255, 255, 255))
            vote_button_text_rect = vote_button_surf.get_rect(center=vote_button_rect.center)
            self.screen.blit(vote_button_surf, vote_button_text_rect)
            self.buttons.append((vote_button_rect, {"command": "vote", "player_index": player_index}))
            player_x += 100

    # Отображение кнопки Следующий раунд
    def show_next_round(self):
        if (self.players_in_game // 2) >= self.num_players:
            self.end_game()
            return

        font = pygame.font.Font(None, 20)
        next_round_button_text = "Следующий раунд"
        next_round_button_rect = pygame.Rect(130, 620, 150, 30)
        pygame.draw.rect(self.screen, (150, 150, 150), next_round_button_rect)
        next_round_button_surf = font.render(next_round_button_text, True, (255, 255, 255))
        next_round_button_text_rect = next_round_button_surf.get_rect(center=next_round_button_rect.center)
        self.screen.blit(next_round_button_surf, next_round_button_text_rect)
        self.buttons.append((next_round_button_rect, {"command": "next_round"}))


    # Отображение отданных голосов
    def show_votes(self):
        if (self.players_in_game // 2) >= self.num_players:
            self.end_game()
            return
        font = pygame.font.Font(None, 20)
        player_x = 175
        for player_index in range(self.num_players):
            black_rect = pygame.Rect(player_x - 50, 580 - 20, 100, 40)
            pygame.draw.rect(self.screen, (0, 0, 0), black_rect)
            votes_text = font.render(str(self.players[player_index].votes), True, (255, 255, 255))
            votes_text_rect = votes_text.get_rect(center=(player_x, 580))
            self.screen.blit(votes_text, votes_text_rect)
            player_x += 100

    # показ всех характеристик
    def show_characteristics(self):
        font = pygame.font.Font(None, 20)
        # Отображение значений профессий для каждого игрока
        player_x = 180
        for player_index in range(self.num_players):
            player_y = 180
            player_y += 50

            if self.players[player_index].details_visible["profession"]:
                for characteristic in ["biology", "health", "phobia", "baggage", "hobby", "fact"]:
                    black_rect = pygame.Rect(player_x - 50, player_y-20, 100, 40)
                    pygame.draw.rect(self.screen, (0, 0, 0), black_rect)
                    if (self.players[player_index].opened_characteristics[characteristic]
                        | self.players[player_index].details_visible[characteristic]):
                        characteristic_value = getattr(self.players[player_index], characteristic)
                        characteristic_text = font.render(characteristic_value, True, (255, 255, 255))
                        characteristic_text_rect = characteristic_text.get_rect(center=(player_x, player_y))
                        self.screen.blit(characteristic_text, characteristic_text_rect)
                    else:
                        show_button_text = "show"
                        show_button_rect = pygame.Rect(player_x - 30, player_y-20, 50, 30)
                        pygame.draw.rect(self.screen, (150, 150, 150), show_button_rect)
                        show_button_surf = font.render(show_button_text, True, (255, 255, 255))
                        show_button_text_rect = show_button_surf.get_rect(center=show_button_rect.center)
                        self.screen.blit(show_button_surf, show_button_text_rect)
                        self.buttons.append((show_button_rect, {"command": "show", "player_index": player_index, "characteristic": characteristic}))

                    player_y += 50

            player_x += 100

    #обработчик кнопок
    def handle_button_click(self, pos):
        for button_rect, command in self.buttons:
            if button_rect.collidepoint(pos):
                match command["command"]:
                    case "show_all":
                        player = self.players[command["player_index"]]
                        all_hidden_except_profession = all(
                            not visible for key, visible in player.details_visible.items() if key != "profession")

                        if all_hidden_except_profession:
                            # Открыть все характеристики, кроме профессии
                            player.last_opened.clear()  # Очистить список последних открытых
                            for key in player.details_visible:
                                if key != "profession":
                                    player.details_visible[key] = True
                                    player.last_opened.add(key)
                        else:
                            # Закрыть только что открытые характеристики
                            for key in list(player.last_opened):
                                player.details_visible[key] = False
                                player.last_opened.clear()  # Очистить список, так как все закрыто
                        self.show_characteristics()  # Перерисовка экрана с таблицей игроков
                    case "show":
                        self.players[command["player_index"]].opened_characteristics[command["characteristic"]] = True
                        self.show_characteristics()  # Перерисовка экрана с таблицей игроков
                    case "vote":
                        self.players[command["player_index"]].vote_against()
                        self.show_votes()
                    case "next_round":
                        selected_player = Player("")
                        max_votes = 0
                        for index in range(self.num_players):
                            player = self.players[index]
                            if player.votes > max_votes:
                                selected_player = player
                                max_votes = player.votes
                            player.reset_votes()
                        if max_votes == 0:
                            font = pygame.font.Font(None, 20)
                            hint_text = font.render(f"Проголосуйте, кто не попадет в бункер", True, (255, 0, 0))
                            hint_text_rect = hint_text.get_rect(center=(450,630))
                            self.screen.blit(hint_text, hint_text_rect)
                        else:
                            self.players.remove(selected_player)
                            self.num_players -= 1
                            self.draw_player_table()

    #добавление игроков
    def add_player(self, name):
        self.players.append(Player(name))

    #результат игры
    def end_game(self):

        self.screen.fill((30, 30, 30))
        font = pygame.font.Font(None, 30)
        self.background = pygame.image.load('assets/images/Winning.jpeg')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))  # Масштабирование изоб
        self.screen.blit(self.background, (0, 0))
        for player in self.players:
            player.open_characteristics()

        # Отображение имен игроков в горизонтальной строке сверху
        player_x = 180
        for player_index in range(self.num_players):
            black_rect = pygame.Rect(player_x - 50, 180- 20, 100, 40)
            pygame.draw.rect(self.screen, (0, 0, 0), black_rect)
            player_name_text = font.render(self.players[player_index].name, True, (255, 255, 255))
            player_name_text_rect = player_name_text.get_rect(center=(player_x, 180))
            self.screen.blit(player_name_text, player_name_text_rect)
            player_x += 100
        self.show_characteristics()
