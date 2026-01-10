from image_factory import *
import pygame
pygame.init()

class RadioButton():
    def __init__(self, rect, selected=0, offset=3, **kwargs):
        self.input_manager = None
        self.rect = pygame.Rect(rect)
        self.offset = offset
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_text_box_image(self.rect.w, self.rect.h, (80, 80, 80), ch=20)
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_text_box_image(self.rect.w, self.rect.h, (110, 110, 110), ch=20)
        #
        self.c_inactive_image = kwargs.get("c_inactive_image") if kwargs.get("c_inactive_image") != None else get_button_image(self.rect.w - offset*2, self.rect.h - offset*2, 0, (110, 110, 110))
        self.c_hover_image = kwargs.get("c_hover_image") if kwargs.get("c_hover_image") != None else get_button_image(self.rect.w - offset*2, self.rect.h - offset*2, 0, (140, 140, 140))
        self.image = self.inactive_image
        self.c_image = self.c_inactive_image
        self.onclick = kwargs.get("onclick")
        self.onclick_params = kwargs.get("onclick_params")
        self.onrelease = kwargs.get("onrelease")
        self.onrelease_params = kwargs.get("onrelease_params")
        self.selected = selected

    def update(self, events):
        mousedown = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.input_manager.mousetag_object[0] = self
                    self.selected = not self.selected
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
                    self.input_manager.mousetag_object[0] = None
                self.image = self.hover_image
                self.c_image = self.c_hover_image
        else:
            if not mousedown:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
                self.image = self.inactive_image
                self.c_image = self.c_inactive_image

    def get_selected(self):
        return(bool(self.selected))

    def set_selected(self, num):
        self.selected = num

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.selected:
            screen.blit(self.c_image, (self.rect.x + self.offset, self.rect.y + self.offset))