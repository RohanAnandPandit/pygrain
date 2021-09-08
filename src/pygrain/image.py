from .component import Component
from .util import show_image
import pygame


class Image(Component):
    """
    Component to display jpeg or png images.
    """
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

        # Load image using file path
        image = pygame.image.load(filepath).convert()
        # Resize image based on width and height of component
        image = pygame.transform.scale(image, (width, height))

        # Display image on screen
        screen.blit(image, (self.get_abs_x(), self.get_abs_y()))
