from src.pygrain.app import App
from src.pygrain.button import Button
from src.pygrain.frame import Frame
from src.pygrain.textbox import TextBox
from src.pygrain.point import Point
from src.pygrain.toggle_switch import ToggleSwitch
from src.pygrain.value_slider import ValueSlider
from src.pygrain.tkinter_window import TkinterWindow
from src.pygrain.vertical_scroll_bar import VerticalScrollBar
from src.pygrain.horizontal_scroll_bar import HorizontalScrollBar
# from src.pygrain.image import Image


def app_test():
    app = App(width=2000, height=1400)
    app.set_title('My App')

    def toggle_width(frm):
        if frm.get_property('width') == 500:
            frame.set_width(600)
        else:
            frm.set_width(500)
        # frame.update()
        return True

    def window():
        root = TkinterWindow(app, width=700, height=400)
        app.add_tkinter_window(root)

    frame = Frame(app, x=100, y=100, width=1500, height=1000,
                  border_thickness=3,
                  resizeable=True, draggable=True)

    button = Button(frame, x=100, y=100, width=250, height=250,
                    text="Click me", font_size=40, resizeable=True)
    button.on_left_click(lambda btn: toggle_width(frame))

    TextBox(frame, text="Text Box", x=100, y=800,
            border_thickness=3, min_x=0,
            max_x=lambda: frame.get_property('width'),
            padding=10, resizeable=True, draggable=True)

    Point(frame, center_x=200, center_y=200, draggable=True, radius=10) \
        .bind('left click', lambda target: print("Hello World"))

    ToggleSwitch(frame, values=['1', '2', '3'], x=600, y=600, width=100,
                 height=100,
                 border_thickness=5, font_size=50, bg_colour=(0, 0, 255),
                 draggable=True, fixed_y=True)

    ToggleSwitch(frame, values=['1', '2', '3'], x=600, y=800, width=100,
                 height=100,
                 border_thickness=5, font_size=50, bg_colour=(0, 0, 255),
                 draggable=True, fixed_y=True, resizeable=True)

    ValueSlider(frame, x=1000, y=800, width=500, height=80, draggable=True,
                step=1,
                default=2, resizeable=True)

    VerticalScrollBar(frame, scroll_height=frame.get_property('height') * 2)
    HorizontalScrollBar(frame, scroll_width=frame.get_property('width') * 2)

    app.switch_frame(frame)
    frame.bind("keydown return", lambda target: print('space'))
    for i in range(0):
        window()

    app.mainloop()


app_test()
