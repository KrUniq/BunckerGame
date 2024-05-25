import pygame

class Button:
    def __init__(self, text, pos, size, action):
        self.text = text
        self.pos = pos # Позиция кнопки (x, y)
        self.size = size
        self.action = action # Действие при клике
        self.color = (0, 0, 0) # Цвет кнопки
        self.hover_color = (50, 50, 50)
        self.font = pygame.font.Font(None, 36) # Шрифт текста кнопки
        self.rect = pygame.Rect(pos, size) # Прямоугольная область кнопки
        self.hovered = False  # Состояние наведения (изначально False)

    def click(self):
        self.action()

    def draw(self, screen):
        # Отрисовка кнопки на экране
        if self.hovered:
            # Если курсор на кнопке, использовать цвет наведения
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        # Отрисовка текста на кнопке
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, event_list):
        # Обновление состояния кнопки
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
                self.action()