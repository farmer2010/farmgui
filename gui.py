from button import *
from text_box import *
from slider import *
from radiobutton import *
from panel import *
from input_manager import *
from utils import *

class ButtonManager():
    def __init__(self):
        self.input_manager = input_manager
        self.screenpanel = Panel((0, 0, pygame.display.Info().current_w, pygame.display.Info().current_h))

    def update(self, screen, events):
        self.screenpanel.update_component(events, pygame.mouse.get_pos())
        self.screenpanel.draw(screen)
        render_text(str(self.input_manager.mousetag_object[0]), [0, 0], screen, color=(255, 255, 255))
        self.input_manager.update(events)

    def add(self, b):
        self.screenpanel.add(b)

    def remove(self, b):
        self.screenpanel.remove(b)