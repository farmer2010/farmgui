from input_manager import *
from image_factory import *
from component import *
import pygame
pygame.init()

class Button(Component):
    def __init__(self, rect, **kwargs):
        Component.__init__(self, rect)
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_button_image(self.rect.w, self.rect.h, 0, (90, 90, 90))
        self.pressed_image = kwargs.get("pressed_image") if kwargs.get("pressed_image") != None else get_button_image(self.rect.w, self.rect.h, 1, (50, 50, 50))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_button_image(self.rect.w, self.rect.h, 2, (120, 120, 120))
        self.image = self.inactive_image
        self.onclick = kwargs.get("onclick")
        self.onclick_params = kwargs.get("onclick_params")
        self.onrelease = kwargs.get("onrelease")
        self.onrelease_params = kwargs.get("onrelease_params")

    def update(self, events, mousepos):
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.image = self.pressed_image
                    if str(type(self.onclick)) == "<class 'function'>":
                        if self.onclick_params != None:
                            self.onclick(*self.onclick_params)
                        else:
                            self.onclick()
            else:
                if self.input_manager.mousetag_object[0] == self:
                    if str(type(self.onrelease)) == "<class 'function'>":
                        if self.onrelease_params != None:
                            self.onrelease(*self.onrelease_params)
                        else:
                            self.onrelease()
                self.image = self.hover_image
        else:
            if self.input_manager.mousetag_object[0] == self:
                self.image = self.pressed_image
            if not mousedown:
                self.image = self.inactive_image

    def draw(self, screen):
        screen.blit(self.image, self.rect)