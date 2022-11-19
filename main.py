import sys
from pygame import pygame as pg

from settings import *
from button import Btn


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.is_running = True
        self.new_game()

    def new_game(self):
        self.btn_Q = Btn(self, name='Q', color=BLUE, x_pos=0, y_pos=0)
        self.btn_W = Btn(self, name='W', color=RED, x_pos=1, y_pos=0)
        self.btn_A = Btn(self, name='A', color=GREEN, x_pos=0, y_pos=1)
        self.btn_S = Btn(self, name='S', color=ORANGE, x_pos=1, y_pos=1)

    def update(self):

        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')

        self.btn_Q.draw()
        self.btn_W.draw()
        self.btn_A.draw()
        self.btn_S.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_q]:
                    self.btn_Q.activate()
                elif keys[pg.K_w]:
                    self.btn_W.activate()
                elif keys[pg.K_a]:
                    self.btn_A.activate()
                elif keys[pg.K_s]:
                    self.btn_S.activate()
            elif event.type == pg.KEYUP:
                self.btn_Q.deactivate()
                self.btn_W.deactivate()
                self.btn_A.deactivate()
                self.btn_S.deactivate()

    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
