import pygame as pg

from constants import *
from player import Player


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pg.display.flip()

        # limit the frame rate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
