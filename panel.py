from component import *
import pygame
pygame.init()

class Panel(Component):
    def __init__(self, rect, background_color=(50, 50, 50), **kwargs):
        Component.__init__(self, rect)
        self.background_image = kwargs.get("background_image")
        if kwargs.get("background_image") == None:
            self.background_image = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
            self.background_image.fill(background_color)
        self.buttons = []

    def update_component(self, events, mousepos):
        self.update(events, mousepos)
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    press_button = 0
                    for b in self.buttons:
                        mpos = (mousepos[0] - self.rect.x, mousepos[1] - self.rect.y)
                        m_c = (mpos[0] >= b.rect.x and mpos[0] <= b.rect.x + b.rect.w) and (mpos[1] >= b.rect.y and mpos[1] <= b.rect.y + b.rect.h)
                        press_button = m_c
                        if m_c:
                            break
                    if not press_button:
                        self.input_manager.mousetag_object[0] = self
            else:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
        else:
            if not mousedown:
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
        for b in self.buttons:
            b.update_component(events, (mousepos[0] - self.rect.x, mousepos[1] - self.rect.y))

    def update(self, events, mousepos):
        pass

    def draw(self, screen):
        self.image.blit(self.background_image, (0, 0))
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