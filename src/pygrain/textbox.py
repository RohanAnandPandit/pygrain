from .component import Component
from .util import show_text, get_text_size


class TextBox(Component):
    """
    Component to display text.
    """
    def __init__(self, parent, text='', padding=None, pad_left=0, pad_right=0,
                 pad_top=0, pad_bottom=0, **kwargs):
        super().__init__(parent, **kwargs)
        self.text = text
        self.pad_left = pad_left
        self.pad_right = pad_right
        self.pad_top = pad_top
        self.pad_bottom = pad_bottom
        if padding is not None:
            self.pad_left = self.pad_right = self.pad_top = self.pad_bottom = padding

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

        pad_left, pad_right = self.get_properties(['pad_left', 'pad_right'])
        width += pad_left + pad_right

        pad_top, pad_bottom = self.get_properties(['pad_top', 'pad_bottom'])
        height += pad_top + pad_bottom

        self.set_property('width', width)
        self.set_property('height', height)

        super().draw(screen)

        show_text(screen, text, x + pad_left, y + pad_top,
                  font_size=font_size, center=False)

        return self

    def get_text(self):
        """
        Return text if it is a string or call function that returns text.
        :return:
        """
        return self.get_property('text')


