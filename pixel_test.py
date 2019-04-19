import pygame, sys, random
from pygame.locals import *
from smalldata import *
pygame.init()
win = pygame.display.set_mode((133, 54))
clock = pygame.time.Clock()
win.fill((255, 255, 255)) #设置背景色
pygame.display.flip()

def flush_box(box_color, rect):  #涂色
    pygame.draw.rect(win, box_color, rect)

while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in range(0,54):
        for j in range(0,133):
            if M[i][j] == -1:
                color = (0,0,139)
                flush_box(color, pygame.Rect(j, i, 1, 1))
            if M[i][j] == 2:
                color = (255,130,71)
                flush_box(color, pygame.Rect(j, i, 1, 1))
    
    pygame.display.update()
