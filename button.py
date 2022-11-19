from pygame import pygame as pg
from pygame import mixer

from settings import *


class Btn:
    def __init__(self, game, name, color, x_pos, y_pos):
        self.game = game
        self.name = name
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.is_active = False
        self.width = BTN_WIDTH
        self.height = BTN_HIGHT

    def draw(self):
        if self.is_active:
            pg.draw.rect(self.game.screen,
                         self.color,
                         (self.x_pos * BTN_WIDTH, self.y_pos * BTN_HIGHT, BTN_WIDTH, BTN_HIGHT))
        else:
            pg.draw.rect(self.game.screen,
                         self.color + '4',
                         (self.x_pos * BTN_WIDTH, self.y_pos * BTN_HIGHT, BTN_WIDTH, BTN_HIGHT))

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
