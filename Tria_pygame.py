import pygame
import data
import sys
import time
from pygame.locals import *

__author__ = "Riccardo Martinelli"
__status__ = "development"
__date__ = "01/04/2018"

clock = pygame.time.Clock()
finestra = pygame.display.set_mode((500, 500))
pygame.display.set_caption("schema gioco tria")
bg = pygame.image.load('Tria_struct.jpg')
green = (32, 173, 54)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grigio = (120, 120, 120)
cordinatex = [115, 250, 380, 150, 250, 340, 200, 250,
              300, 110, 150, 200, 295, 345, 385, 200,
              250, 300, 150, 250, 340, 110, 250, 380]
cordinatey = [115, 115, 115, 160, 160, 160, 200, 200,
              200, 250, 250, 250, 250, 250, 250, 300,
              300, 300, 300, 340, 340, 340, 385, 385, 385]
while True:
    Val = data.ReturnValue("Val")
    print(Val)
    for i in range(0, 24):
        if Val[i] == 1:
            print("utente")
            pygame.draw.circle(
                finestra, grigio, (cordinatex[i], cordinatey[i]), 13, 0)
            pygame.display.update()
        if Val[i] == 10:
            pygame.draw.circle(
                finestra, blue, (cordinatex[i], cordinatey[i]), 13, 0)
            pygame.display.update()
    clock.tick(60)
    finestra.fill(green)
    finestra.blit(bg, (100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
