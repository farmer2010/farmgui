from image_factory import *
from utils import *
import pygame
pygame.init()

class Slider():
    def __init__(self, rect, c_rect, preset_value=0, min_value=0, max_value=100, **kwargs):
        self.rect = pygame.Rect(rect)
        self.c_rect = c_rect
        self.input_manager = None
        self.value = preset_value
        self.min_value = min_value
        self.max_value = max_value
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_slider_image(self.rect.w, self.rect.h, (90, 90, 90))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_slider_image(self.rect.w, self.rect.h, (120, 120, 120))
        self.image = self.inactive_image

    def update(self, events):
        mousedown = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.input_manager.mousetag_object[0] = self
            else:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
                self.image = self.hover_image
        else:
            if self.input_manager.mousetag_object[0] == self:
                self.input_manager.mouse_connect_object[0] = self
                if not mousedown:
                    self.input_manager.mousetag_object[0] = None
            if not mousedown:
                self.image = self.inactive_image

    def get_value(self):
        return(self.value)

    def set_value(self, value):
        self.value = value

    def draw(self, screen):
        screen.blit(self.image, self.rect)