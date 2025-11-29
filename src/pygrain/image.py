from .component import Component
# from .util import show_image
import pygame


class Image(Component):
    def __init__(self, parent, filepath, **kwargs):
        self.filepath = filepath
        image = pygame.image.load(filepath).convert()

        super().__init__(parent,
                         width=image.get_width(),
                         height=image.get_height(),
                         **kwargs)

    def draw(self, screen):
        super().draw(screen)
        filepath = self.get_property('filepath')
        width, height = self.get_properties('width', 'height')

        image = pygame.image.load(filepath).convert()
        image = pygame.transform.scale(image, (width, height))

        screen.blit(image, (self.get_abs_x(), self.get_abs_y()))
