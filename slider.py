from image_factory import *
from utils import *
import pygame
pygame.init()

class Slider():
    def __init__(self, rect, c_rect, input_manager, preset_value=0, min_value=0, max_value=100, **kwargs):
        self.rect = rect
        self.c_rect = c_rect
        self.input_manager = input_manager
        self.value = preset_value
        self.min_value = min_value
        self.max_value = max_value
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_slider_image(self.rect.w, self.rect.h, 0, (90, 90, 90))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_slider_image(self.rect.w, self.rect.h, 0, (120, 120, 120))
        self.image = self.inactive_image

    def update(self, events):
        pass

    def get_value(self):
        return(self.value)

    def set_value(self, value):
        self.value = value

    def draw(self, screen):
        pass