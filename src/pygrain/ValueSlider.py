from .Frame import Frame
from .Point import Point
import pygame


class ValueSlider(Frame):
    def __init__(self, parent, start=0, end=10, increment=None, default=None,
                 **kwargs):
        super().__init__(parent, **kwargs)
        self.start = start
        self.end = end
        self.increment = increment
        self.default = default

        if self.default is None:
            self.default = (self.start + self.end) / 2

        self.point = Point(self, x=(self.width / 2), y=(self.height / 2),
                           draggable=True, fixed_y=True, min_x=0, max_x=self.width)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.line(screen, (0, 0, 0),
                         (self.get_x(), self.get_y() + self.height / 2),
                         (self.get_x() + self.width, self.get_y() + self.height / 2),
                         2)
        self.point.draw(screen)
        self.update()