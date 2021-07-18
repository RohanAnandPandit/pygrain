import pygame
import sys
import os
import ctypes
import threading

pygame.init()

ctypes.windll.shcore.SetProcessDpiAwareness(1)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5, 60)

WHITE = 255, 255, 255


class App:
    def __init__(self, width=1000, height=800, frame=None):
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height))
        self.frame = frame
        self.frames = []

    def mainloop(self):
        self.update()
        while True:
            self.check_events()

    def update(self):
        self.screen.fill(WHITE)

        if self.frame:
            self.frame.draw(self.screen)

        pygame.display.update()

    def add_component(self, frame):
        self.frames.append(frame)
        return self

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.frame.event("left click")
                elif event.button == 2:
                    self.frame.event("middle click")
                elif event.button == 2:
                    self.frame.event("right click")

    def switch_frame(self, frame):
        self.frame = frame
        return self

    def run(self, func):
        window_thread = threading.Thread(target=func, args=tuple())
        window_thread.start()
        return self

    def set_title(self, title):
        pygame.display.set_caption(title)
        return self
