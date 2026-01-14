from gui import *
import pygame
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("GUI test")
keep_going = 1
timer = pygame.time.Clock()

buttons = ButtonManager(background_color=(255, 255, 255))
buttons.add(Button((50, 50, 200, 50), onrelease=lambda: print(1)))
buttons.add(TextBox((50, 150, 200, 50)))
buttons.add(Slider((50, 250, 200, 50), (44, 44)))
buttons.add(RadioButton((50, 350, 30, 30)))
#
panel = Panel((500, 100, 300, 600), background_color=(180, 180, 180))
panel.add(Button((5, 5, 250, 35), text="button 1"))
panel.add(Button((5, 45, 250, 35), text="button 2"))
panel.add(Button((5, 85, 250, 35), text="button 3"))
buttons.add(panel)
#
group = RadioButtonGroup()
buttons.add(RadioButton((50, 400, 30, 30), selected=1, group=group, text="1"))
buttons.add(RadioButton((50, 440, 30, 30), group=group, text="2"))
buttons.add(RadioButton((50, 480, 30, 30), group=group, text="3"))
buttons.add(RadioButton((50, 520, 30, 30), group=group, text="4"))
#
buttons.add(TextLabel("Hello world!", (0, 0), font_color=(0, 128, 255)))
label = TextLabel("", (0, 30))
label.add_update_text(lambda: "value: " + str(buttons.get_component(2).get_value()))
buttons.add(label)
#
slider = Slider((275, 250, 200, 50), (44, 44))
slider.add_update_text(lambda x: "value: " + str(x))
buttons.add(slider)


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