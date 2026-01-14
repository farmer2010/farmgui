from image_factory import *
from component import *
from utils import *
import pygame
pygame.init()

class Slider(Component):
    def __init__(self, rect, c_rect, preset_value=0, min_value=0, max_value=100, offset=3, value_type="int", font=None, font_name=None, font_size=30, font_color=(0, 0, 0), font_alpha=True, center=(0.5, 0.5, 0.5, 0.5), **kwargs):
        Component.__init__(self, rect)
        self.c_rect = c_rect
        self.value = preset_value
        self.min_value = min_value
        self.max_value = max_value
        self.offset = offset
        self.type = value_type
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_slider_image(self.rect.w, self.rect.h, (90, 90, 90))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_slider_image(self.rect.w, self.rect.h, (120, 120, 120))
        self.image = self.inactive_image
        #
        self.c_inactive_image = kwargs.get("c_inactive_image") if kwargs.get("c_inactive_image") != None else get_button_image(self.c_rect[0], self.c_rect[1], 0, (60, 60, 60))
        self.c_hover_image = kwargs.get("c_hover_image") if kwargs.get("c_hover_image") != None else get_button_image(self.c_rect[0], self.c_rect[1], 0, (90, 90, 90))
        self.c_image = self.c_inactive_image
        #
        self.update_text = None
        self.text = ""
        if font == None: font = pygame.font.SysFont(font_name, font_size)
        self.font = font
        self.font_color = font_color
        self.font_alpha = font_alpha
        self.update_text = None
        self.center = center

    def update(self, events, mousepos):
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.update_param()
            else:
                self.image = self.hover_image
                self.c_image = self.c_hover_image
        else:
            if not mousedown:
                self.image = self.inactive_image
                self.c_image = self.c_inactive_image
        if self.input_manager.mousetag_object[0] == self and mousedown:
            self.update_param()
        if self.update_text != None: self.text = self.update_text(self.value)

    def update_param(self):
        mousepos = pygame.mouse.get_pos()
        pos = (mousepos[0] - self.rect.x, mousepos[1] - self.rect.y)
        if pos[0] >= self.offset + self.c_rect[0] / 2 and pos[0] < self.rect.w - self.offset - self.c_rect[0] / 2:
            self.value = self.min_value + (pos[0] - self.offset - self.c_rect[0] / 2) / (self.rect.w - self.offset * 2 - self.c_rect[0]) * (self.max_value - self.min_value)
        elif pos[0] < self.offset + self.c_rect[0] / 2:
            self.value = self.min_value
        elif pos[0] >= self.rect.w - self.offset * 2 - self.c_rect[0] / 2:
            self.value = self.max_value
        if self.type == "int":
            self.value = round(self.value)

    def add_update_text(self, upd):
        self.update_text = upd

    def get_value(self):
        return(self.value)

    def set_value(self, value):
        self.value = value

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        x = (self.rect.w - self.offset * 2 - self.c_rect[0]) * (self.value / (self.max_value - self.min_value))
        screen.blit(self.c_image, (self.rect.x + self.offset + x, (self.rect.y + self.rect.h / 2) - (self.c_rect[1] / 2)))
        img = self.font.render(self.text, self.font_alpha, self.font_color)
        screen.blit(img, (self.rect.x + self.rect.w / 2 - img.get_width() / 2, self.rect.y + self.rect.h / 2 - img.get_height() / 2))
