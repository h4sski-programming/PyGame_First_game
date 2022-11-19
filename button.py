import pygame as pg

from settings import *


class Btn:
    def __init__(self, game, name, color):
        self.game = game
        self.name = name
        self.color = color

        self.width = BTN_WIDTH
        self.height = BTN_HIGHT

    def draw(self):
        pg.draw.rect(self.game.screen,
                     self.color,
                     (0, 1, BTN_WIDTH, BTN_HIGHT))
