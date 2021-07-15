from .PygameComponent import PygameComponent


class PygameFrame(PygameComponent):
    def __init__(self, parent):
        super().__init__(parent)
        self.components = []

    def event(self, name):
        for component in self.components:
            component.event(name)

    def draw(self, screen):
        for component in self.components:
            component.draw(screen)

    def add_component(self, component):
        self.components.append(component)

