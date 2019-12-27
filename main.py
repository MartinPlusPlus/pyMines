import pygame as pg
import sys
from pygame.locals import *
from screens import screen

WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))
RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))

DARK_WHITE = ((150, 150, 150))

pg.init()
window = pg.display.set_mode((600, 800))

#         self.currentRoom = self.roomList[request]
pg.display.set_caption("pyMines")
window.fill((200, 200, 200))
pg.display.update()

def titleScreen():
    pg.font.init()

running = True

while running:
    for event in pg.event.get():
        # Close the program if the x is pressed
        if event.type == pg.QUIT:
            pg.font.quit()
            running = False

        bomb = pg.draw.rect(window, DARK_WHITE, (0, 0, 30, 30), 0)
        pg.display.flip()

pg.font.quit()
pg.quit()
sys.exit()
