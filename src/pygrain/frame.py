from .box import Box
from .component import Component
from .point import Point
from collections import defaultdict


class Frame(Component):
    """
    Class for a collection of components.
    """

    def __init__(self, parent, resizeable=False, **kwargs):
        super().__init__(parent, **kwargs)
        self.components = []
        parent.switch_frame(self)

        width, height = self.get_properties(['width', 'height'])
        self.resizeable = resizeable

        if resizeable:
            self.resize_point = Point(self, center_x=width, center_y=height,
                                      draggable=True, free_x=True, free_y=True,
                                      radius=10)

            self.bottom_bar = Box(self, x=0, y=self.height,
                                  fixed_x=True,
                                  width=lambda: self.get_property('width'),
                                  height=20,
                                  free_y=True,
                                  draggable=True)

            self.bind('always', lambda target: self.resize_frame())

    def mouseover(self):
        for component in self.components:
            if component.mouseover():
                return True

        return super().mouseover()

    def event(self, events, events_done=None):
        """
        Pass events to all sub-components inside the frame.
        :param events_done:
        :param events:
        :return: if events was valid for any component
        """
        if events_done is None:
            events_done = set()
        for component in self.components[::-1]:
            component.event(events, events_done=events_done)

        return super().event(events, events_done=events_done)

    def draw(self, screen):
        """
        Draw frame and all sub-components from bottom to top order.
        :param screen:
        :return: None
        """
        super().draw(screen)
        for component in self.components:
            component.draw(screen)

    def add_component(self, component):
        """
        Add new component to the front of list.
        :param component: Component
        :return: None
        """
        self.components.append(component)

    def get_components(self):
        return self.components

    def update(self):
        """
        Update parent component (or App).
        :return:
        """
        self.parent.update()

    def resize_frame(self):
        if self.resize_point.dragging:
            x, y = self.resize_point.x, self.resize_point.y
            self.width, self.height = x, y
            self.bottom_bar.y = y
            self.update()
            return True

        elif self.bottom_bar.dragging:
            y = self.bottom_bar.y
            self.height = y
            self.resize_point.y = y
            self.update()
            return True

        return False
