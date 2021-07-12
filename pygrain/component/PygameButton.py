from PygameComponent import PygameComponent


class PygameButton(PygameComponent):
    def __init__(self, app=None, x=0, y=0, width=0, height=0, text="",
                 down_actions=lambda: [lambda app: 0, lambda app: 0, lambda app: 0],
                 up_actions=lambda: [lambda app: 0, lambda app: 0, lambda app: 0],
                 font_color=(0, 0, 0), bg_colour=(255, 255, 255), border_color=(0, 0, 0),
                 border_thickness=2):
        super.__init__(app)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.down_actions = down_actions
        self.up_actions = up_actions

    def click(self, button_no):
        return self.down_actions[button_no - 1](self.app)

    def leave(self, button_no):
        return self.up_actions[button_no - 1](self.app)
