from button import *
from text_box import *
from slider import *
from radiobutton import *
from panel import *
from radiobutton_group import *
from text_label import *
from number_box import *
from input_manager import *
from utils import *

class ButtonManager():
    def __init__(self, background_color=(50, 50, 50), background_image=None):
        self.input_manager = input_manager
        self.screenpanel = Panel((0, 0, pygame.display.Info().current_w, pygame.display.Info().current_h), background_color=background_color, background_image=background_image)

    def update(self, screen, events):
        self.screenpanel.update_component(events, pygame.mouse.get_pos())
        self.screenpanel.draw(screen)
        self.input_manager.update(events)

    def add(self, b):
        self.screenpanel.add(b)

    def remove(self, b):
        self.screenpanel.remove(b)

    def get_component(self, index):
        return(self.screenpanel.buttons[index])

    def get_component_count(self):
        return(len(self.screenpanel.buttons))