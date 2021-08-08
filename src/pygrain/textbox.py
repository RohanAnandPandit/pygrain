from .component import Component
from .util import show_text, get_text_size


class TextBox(Component):
    """
    Component to display text.
    """
    def __init__(self, parent, text='', **kwargs):
        super().__init__(parent, **kwargs)
        self.text = text

    def draw(self, screen):
        """
        Draw textbox with text.
        :param screen:
        :return:
        """
        x, y = self.get_abs_x(), self.get_abs_y()
        text = self.get_text()
        font_size = self.get_property('font_size')
        width, height = get_text_size(self.get_text(), font_size=font_size)
        self.set_property('width', width)
        self.set_property('height', height)
        super().draw(screen)
        show_text(screen, text, x + width / 2, y + height / 2, font_size=font_size)
        return self

    def get_text(self):
        """
        Return text if it is a string or call function that returns text.
        :return:
        """
        text = self.text
        if callable(text):
            text = text()

        return text


