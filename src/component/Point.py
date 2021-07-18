from .Component import Component
import pygame


class Point(Component):
    def __init__(self, parent, radius=5, **kwargs):
        super().__init__(parent, **kwargs)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,
                           color=self.get_property('colour'),
                           center=(self.get_x(), self.get_y()),
                           radius=self.get_property('radius'))

    def mouseover(self):
        x, y = self.get_x(), self.get_y()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (((x - mouse_x) ** 2 + (y-mouse_y) ** 2) ** 0.5) < self.radius