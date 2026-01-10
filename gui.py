from button import *
from text_box import *
from slider import *
from radiobutton import *
from input_manager import *

class ButtonManager():
    def __init__(self):
        self.input_manager = InputManager()
        self.buttons = []

    def update(self, screen, events):
        for b in self.buttons:
            b.update(events)
        for b in self.buttons:
            b.draw(screen)
        self.input_manager.update(events)

    def add(self, b):
        self.buttons.append(b)
        b.input_manager = self.input_manager

    def remove(self, b):
        self.buttons.remove(b)