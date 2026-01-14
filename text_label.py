from utils import *
from component import *

class TextLabel(Component):
    def __init__(self, text, pos, font=None, font_name=None, font_size=30, color=(0, 0, 0), font_alpha=1):
        if font == None: font = pygame.font.SysFont(font_name, font_size)
        img = font.render(text, font_alpha, color)
        Component.__init__(self, img.get_rect())
        self.image = img
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #
        self.font = font
        self.text = text
        self.color = color
        self.font_alpha = font_alpha
        self.update_text = None

    def add_update_text(self, upd):
        self.update_text = upd

    def set_text(self, text):
        self.text = text

    def update(self, events, mousepos):
        if self.update_text != None:
            self.text = self.update_text()

    def draw(self, screen):
        self.image = self.font.render(self.text, self.font_alpha, self.color)
        screen.blit(self.image, self.rect)