from gui import *
import pygame
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("GUI test")
keep_going = 1
timer = pygame.time.Clock()

buttons = ButtonManager()
buttons.add(Button((50, 50, 200, 50), onrelease=lambda: print(1)))
buttons.add(TextBox((50, 150, 200, 50)))
buttons.add(Slider((50, 250, 200, 50), (44, 44)))
buttons.add(RadioButton((50, 350, 30, 30)))
panel = Panel((500, 100, 300, 600))
panel.add(Button((5, 5, 250, 35)))
panel.add(Button((5, 45, 250, 35)))
panel.add(Button((5, 85, 250, 35)))
buttons.add(panel)

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
    buttons.update(screen, events)
    pygame.display.update()
    timer.tick(60)
pygame.quit()