from input_manager import *
import pygame
pygame.init()

class Component():
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.input_manager = input_manager
        self.image = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
        #self.image.convert_alpha()

    def update_component(self, events, mousepos):
        self.update(events, mousepos)
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.input_manager.mousetag_object[0] = self
            else:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
        else:
            if not mousedown:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None

    def update(self, events, mousepos):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)