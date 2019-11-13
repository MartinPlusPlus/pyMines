import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600, 800))

pygame.display.set_caption("pyMines")
window.fill((200, 200, 200))
pygame.display.update()


def titleScreen():
    # TODO

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
