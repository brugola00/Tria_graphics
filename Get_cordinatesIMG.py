import pygame
import sys
import time

finestra = pygame.display.set_mode((500, 500))
bg = pygame.image.load('Tria_struct.jpg')
finestra.blit(bg, (100, 100))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.05)
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
    pygame.display.update()
