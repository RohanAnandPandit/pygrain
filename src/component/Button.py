from .Component import Component
import pygame
from .util import show_text


class Button(Component):
    def __init__(self, parent, x=0, y=0, text=lambda: '', **kwargs):
        super().__init__(parent, x=x, y=y, **kwargs)
        self.text = text
        self.actions = {}

    def on_left_click(self, func):
        self.actions['left click'] = func
        return self

    def on_right_click(self, func):
        self.actions['right click'] = func
        return self

    def on_middle_click(self, func):
        self.actions['middle click'] = func
        return self

    def draw(self, screen):
        x, y = self.get_x(), self.get_y()
        super().draw(screen)
        show_text(screen, self.get_text(), x + self.width / 2,
                  y + self.height / 2, font_size=self.font_size)

    def mouseover(self):
        x, y = pygame.mouse.get_pos()
        return (
                self.get_x() <= x <= self.get_x() + self.width and
                self.get_x() <= y <= self.get_x() + self.height
        )

    def event(self, name):
        if name in self.actions and self.mouseover():
            return self.actions[name](self)

    def set_text(self, text):
        self.set_property('text', text)

    def get_text(self):
        return self.get_property('text')
