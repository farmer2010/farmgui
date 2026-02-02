from input_manager import *
import pygame
pygame.init()

class Component():
    def __init__(self, rect, center=(0, 0)):
        self.rect = pygame.Rect(rect)
        self.center = center
        if self.center == None: self.center = (0, 0)
        self.input_manager = input_manager
        self.image = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
        self.parent = None
        self.rect.x -= self.rect.w * self.center[0]
        self.rect.y -= self.rect.h * self.center[1]

    def update_component(self, events):
        self.update(events)
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = self.collide()
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

    def get_mousepos(self):
        mousepos = pygame.mouse.get_pos()
        mpos = (mousepos[0] - self.parent.rect.x, mousepos[1] - self.parent.rect.y)#позиция мыши относительно родительского компонента
        return(mpos)

    def collide(self):
        mousepos = self.get_mousepos()
        return((mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h))

    def update(self, events):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))