from component import *
import pygame
pygame.init()

class Panel(Component):
    def __init__(self, rect):
        Component.__init__(self, rect)
        self.buttons = []

    def update(self, events, mousepos):
        for b in self.buttons:
            b.update(events, (mousepos[0] - self.rect.x, mousepos[1] - self.rect.y))

    def draw(self, screen):
        for b in self.buttons:
            b.draw(self.image)
        screen.blit(self.image, self.rect)

    def add(self, b):
        self.buttons.append(b)

    def remove(self, b):
        self.buttons.remove(b)

    def get_component(self, index):
        return(self.buttons[index])

    def get_component_count(self):
        return(len(self.buttons))