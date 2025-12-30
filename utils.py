import pygame
pygame.init()

def render_text(text, pos, screen, color=(0, 0, 0), centerx="left", centery="up", font=pygame.font.SysFont(None, 40)):#отрисовка текста на экране
    text_img = font.render(text, True, color)
    text_rect = text_img.get_rect()
    if centerx == "left":
        text_rect.x = pos[0]
    elif centerx == "center":
        text_rect.centerx = pos[0]
    elif centerx == "right":
        text_rect.x = pos[0] - text_img.get_width()
    if centery == "up":
        text_rect.y = pos[1]
    elif centery == "center":
        text_rect.centery = pos[1]
    elif centery == "down":
        text_rect.y = pos[1] - text_img.get_height()
    screen.blit(text_img, text_rect)

def render_text_image(text, pos, w, h, color=(0, 0, 0), centerx="left", centery="up", font=pygame.font.SysFont(None, 40), alpha=True):#отрисовка текста в картинку
    screen = pygame.Surface((w, h))
    screen.fill((0, 1, 255))
    screen.set_colorkey((0, 1, 255))
    text_img = font.render(text, alpha, color)
    text_rect = text_img.get_rect()
    if centerx == "left":
        text_rect.x = pos[0]
    elif centerx == "center":
        text_rect.centerx = pos[0]
    elif centerx == "right":
        text_rect.x = pos[0] - text_img.get_width()
    if centery == "up":
        text_rect.y = pos[1]
    elif centery == "center":
        text_rect.centery = pos[1]
    elif centery == "down":
        text_rect.y = pos[1] - text_img.get_height()
    screen.blit(text_img, text_rect)
    return(screen)