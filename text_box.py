from image_factory import *
from utils import *
import pygame
pygame.init()

class TextBox():
    def __init__(self, rect, **kwargs):
        self.rect = pygame.Rect(rect)
        self.input_manager = None
        self.text = ""
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_text_box_image(self.rect.w, self.rect.h, (90, 90, 90))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_text_box_image(self.rect.w, self.rect.h, (120, 120, 120))
        self.image = self.inactive_image
        self.mouselast = 0
        self.size = kwargs.get("size")
        if self.size == None:
            self.size = 25
        self.color = kwargs.get("color")
        if self.color == None:
            self.color = (0, 0, 0)
        self.font = kwargs.get("font")
        if self.font == None:
            self.font = pygame.font.SysFont("times new roman", self.size)
        self.text_x = kwargs.get("text_x")
        if self.text_x == None:
            self.text_x = 10
        self.onclick = kwargs.get("onclick")
        self.onclick_params = kwargs.get("onclick_params")
        self.onchange = kwargs.get("onchange")
        self.onchange_params = kwargs.get("onchange_params")
        self.timer = 0
        self.cursor_pos = 0

    def update(self, events):
        self.timer += 1
        self.timer %= 60
        mousedown = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and (mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        last_text = self.text
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    self.input_manager.mousetag_object[0] = self
                    if str(type(self.onclick)) == "<class 'function'>":
                        if self.onclick_params != None:
                            self.onclick(*self.onclick_params)
                        else:
                            self.onclick()
            else:
                self.image = self.hover_image
                if self.mouselast and self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mouse_connect_object[0] = self
                if self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mousetag_object[0] = None
            self.mouselast = mousedown
        else:
            if self.input_manager.mousetag_object[0] == self:
                self.input_manager.mouse_connect_object[0] = self
                if not mousedown:
                    self.input_manager.mousetag_object[0] = None
            if not mousedown:
                self.image = self.inactive_image
            if mousedown and self.input_manager.mouse_connect_object[0] == self:
                self.input_manager.mouse_connect_object[0] = None
        if self.input_manager.mouse_connect_object[0] == self:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.cursor_pos >= 1:
                        self.cursor_pos -= 1
                    if event.key == pygame.K_RIGHT and self.cursor_pos < len(self.text):
                        self.cursor_pos += 1
                    if event.key == pygame.K_BACKSPACE and self.cursor_pos > 0:
                        self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]
                        self.cursor_pos -= 1
                    elif event.unicode != "" and event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB and event.key != pygame.K_DELETE and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and event.key != pygame.K_KP_ENTER:
                        text_img = self.font.render(self.text + event.unicode, True, self.color)
                        if text_img.get_width() < self.rect.w - self.text_x * 2:
                            self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                            self.cursor_pos += 1
        if last_text != self.text:
            if str(type(self.onchange)) == "<class 'function'>":
                if self.onchange_params != None:
                    self.onchange(*self.onchange_params)
                else:
                    self.onchange()

    def get_text(self):
        return(self.text)

    def set_text(self, text):
        self.text = text

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        render_text(self.text, (self.rect.x + self.text_x, self.rect.y + self.rect.h / 2), screen, centery="center", font=self.font, color=self.color)
        if self.timer < 30 and self.input_manager.mouse_connect_object[0] == self:
            text_img = self.font.render(self.text[:self.cursor_pos], True, self.color)
            pygame.draw.rect(screen, self.color, (self.rect.x + self.text_x + text_img.get_width(), self.rect.y + self.rect.h / 2 - text_img.get_height() / 2, 2, text_img.get_height()))
        #render_text(str(self.cursor_pos), (0, 0), screen)