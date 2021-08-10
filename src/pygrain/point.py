from .component import Component
import pygame


class Point(Component):
    """
    Component to represent a point.
    """
    def __init__(self, parent, radius=5, center_x=0, center_y=0, **kwargs):
        self.center_x = center_x
        self.center_y = center_y
        center_x = self.get_property('center_x')
        center_y = self.get_property('center_y')
        x, y = center_x - radius, center_y - radius
        self.center_x = lambda: self.get_x() + self.get_property('radius')
        self.center_y = lambda: self.get_y() + self.get_property('radius')
        super().__init__(parent, x=x, y=y, **kwargs)
        self.radius = radius

    def draw(self, screen):
        """
        Draw circle representing point.
        :param screen: pygame screen
        :return: None
        """
        if self.get_property('invisible'):
            return
        pygame.draw.circle(screen,
                           color=self.get_property('colour'),
                           center=(self.get_abs_x(), self.get_abs_y()),
                           radius=self.get_property('radius'))

    def get_abs_x(self):
        return super().get_abs_x() + self.radius

    def get_abs_y(self):
        return super().get_abs_y() + self.radius

    def mouseover(self):
        """
        Return if mouse is inside circle representing point.
        :return: bool
        """
        x, y = self.get_abs_x(), self.get_abs_y()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (((x - mouse_x) ** 2 + (y-mouse_y) ** 2) ** 0.5) < self.radius