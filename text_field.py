from image_factory import *
from utils import *
from component import *
import pygame
pygame.init()

class TextField(Component):
    def __init__(self,
                 rect,
                 text="",
                 font=None,
                 font_name="times new roman",
                 font_size=30,
                 font_color=(0, 0, 0),
                 text_x=10,
                 text_y=10,
                 enabled_symbols=None,
                 disabled_symbols=[],
                 **kwargs
                 ):
        Component.__init__(self, rect)
        #
        self.inactive_image = kwargs.get("inactive_image") if kwargs.get("inactive_image") != None else get_text_box_image(self.rect.w, self.rect.h, (90, 90, 90))
        self.hover_image = kwargs.get("hover_image") if kwargs.get("hover_image") != None else get_text_box_image(self.rect.w, self.rect.h, (120, 120, 120))
        self.image = self.inactive_image
        #
        self.text = text
        self.text_lines = []
        self.text_x = text_x
        self.text_y = text_y
        if font == None: font = pygame.font.SysFont(font_name, font_size)
        self.font = font
        self.font_color = font_color
        #
        self.enabled_symbols = enabled_symbols
        self.disabled_symbols = disabled_symbols
        #
        self.timer = 0
        self.cursor = 0
        self.cursor_pos = [0, 0]
        self.mouselast = 0
        self.w = self.font.render("W", 1, self.font_color).get_height()
        #
        self.onclick = kwargs.get("onclick")
        self.onclick_params = kwargs.get("onclick_params")
        self.onchange = kwargs.get("onchange")
        self.onchange_params = kwargs.get("onchange_params")
        self.onsubmit = kwargs.get("onsubmit")
        self.onsubmit_params = kwargs.get("onsubmit_params")
        self.update_text_image()

    def update(self, events, mousepos):
        self.timer += 1
        self.timer %= 60
        mousedown = pygame.mouse.get_pressed()[0]
        mouse_collide = (mousepos[0] >= self.rect.x and mousepos[0] <= self.rect.x + self.rect.w) and ( mousepos[1] >= self.rect.y and mousepos[1] <= self.rect.y + self.rect.h)
        last_text = self.text
        if mouse_collide:
            if mousedown:
                if self.input_manager.mousetag_object[0] == None:
                    if str(type(self.onclick)) == "<class 'function'>":
                        if self.onclick_params != None:
                            self.onclick(*self.onclick_params)
                        else:
                            self.onclick()
            else:
                self.image = self.hover_image
                if self.mouselast and self.input_manager.mousetag_object[0] == self:
                    self.input_manager.mouse_connect_object[0] = self
            self.mouselast = mousedown
        else:
            if self.input_manager.mousetag_object[0] == self:
                self.input_manager.mouse_connect_object[0] = self
            if not mousedown:
                self.image = self.inactive_image
            if mousedown and self.input_manager.mouse_connect_object[0] == self:
                self.input_manager.mouse_connect_object[0] = None
                if str(type(self.onsubmit)) == "<class 'function'>":
                    if self.onsubmit_params != None:
                        self.onsubmit(*self.onsubmit_params)
                    else:
                        self.onsubmit()
        if self.input_manager.mouse_connect_object[0] == self:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.cursor >= 1:
                        self.cursor -= 1
                    if event.key == pygame.K_RIGHT and self.cursor < len(self.text):
                        self.cursor += 1
                    if event.key == pygame.K_BACKSPACE and self.cursor > 0:
                        self.text = self.text[:self.cursor - 1] + self.text[self.cursor:]
                        self.cursor -= 1
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.text = self.text[:self.cursor] + "\n" + self.text[self.cursor:]
                    elif event.unicode != "" and event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB and event.key != pygame.K_DELETE and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and event.key != pygame.K_KP_ENTER:
                        if (self.enabled_symbols == None or event.unicode in self.enabled_symbols) and not (event.unicode in self.disabled_symbols):
                            self.text = self.text[:self.cursor] + event.unicode + self.text[self.cursor:]
                            self.cursor += 1
        if last_text != self.text:
            self.update_text_image()
            print("\n" + self.text)
            if str(type(self.onchange)) == "<class 'function'>":
                if self.onchange_params != None:
                    self.onchange(*self.onchange_params)
                else:
                    self.onchange()

    def update_text_image(self):
        text = self.text.split("\n")
        ins = []
        for i in range(len(text)):
            t = text[i]
            while self.font.render(text[i], 1, self.font_color).get_width() > self.rect.w - self.text_x * 2:
                tn = ""
                for j in range(len(t)):
                    tn += t[j]
                    if self.font.render(tn, 1, self.font_color).get_width() > self.rect.w - self.text_x * 2:
                        text[i] = t[j:]
                        t = text[i]
                        ins.append((i - 1, tn[:-1]))
                        break
        for i in ins:
            text.insert(i[0], i[1])
        self.text_lines = text

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        w = 0
        for t in self.text_lines:
            render_text(t, (self.rect.x + self.text_x, self.rect.y + self.text_y + w), screen, font=self.font, color=self.font_color)
            w += self.w
        if self.input_manager.mouse_connect_object[0] == self and self.timer > 30:
            pass