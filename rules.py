import sys

import pygame

class Rules:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.rules_text = [
            "Правила игры Бункер:",
            "1. Каждый игрок получает карточку персонажа с уникальными характеристиками.",
            "2. Игроки по очереди открывают свои карточки и рассказывают о своем персонаже.",
            "3. После этого начинается обсуждение, кого из персонажей взять в бункер.",
            "4. Происходит голосование. Игрок, набравший больше всего голосов, выбывает.",
            "5. Игра продолжается до тех пор, пока не останется "
            "необходимое количество игроков.",
            "6. Цель игры — убедить других игроков в полезности своего персонажа в бункере.",
            "7. Побеждает тот, кто сможет остаться в бункере до конца игры.",
            "8. Будьте убедительны и стратегичны!"
        ]
        self.new_state = 'rules'

    def draw(self):
        self.screen.fill((30, 30, 30))
        y = 50
        for line in self.rules_text:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y))
            y += 40
        font = pygame.font.Font(None, 36)
        text = font.render('Нажмите ESC для возврата', True, (255, 255, 255))
        self.screen.blit(text, (200, 500))
        self.new_state = 'rules'


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.new_state = 'menu'
                    print(self.new_state)
                    return 'menu'
        return self.new_state
