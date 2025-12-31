from button import *
from text_box import *
from slider import *
from input_manager import *
import pygame
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("GUI test")
keep_going = 1
timer = pygame.time.Clock()

IM = InputManager()
buttons = []
buttons.append(Button(pygame.Rect(50, 50, 200, 50), IM, onrelease=lambda: print(1)))
buttons.append(TextBox(pygame.Rect(50, 150, 200, 50), IM))
#buttons.append(Slider(pygame.Rect(50, 150, 200, 50), pygame.Rect(), IM))

while keep_going:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            keep_going = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keep_going = 0
    #
    screen.fill((255, 255, 255))
    for b in buttons:
        b.update(events)
    for b in buttons:
        b.draw(screen)
    IM.update(events)
    pygame.display.update()
    timer.tick(60)
pygame.quit()