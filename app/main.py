import time

import curses
from curses import wrapper

from app import graphicsEngine as gE
from app.player import playerEngine as pE
from app import worldGenerator as wG

run = True
FPS = 1/60

worldsize_r = 100
worldsize_c = 100
WORLD_HEIGHT = 100
WORLD_WIDTH = 300

world = wG.generateWorld(WORLD_HEIGHT, WORLD_WIDTH)

def init_curses(stdscr: curses.window):
    curses.start_color()
    curses.curs_set(0)
    stdscr.nodelay(True)
    gE.init_graphicsEngine(stdscr)


def check_key(stdscr: curses.window):
    try:
        key = stdscr.getkey()
        pE.player1.check_key(key, stdscr, world)
        # Break if q was hit
        if key == 'q':
            gE.clear(stdscr)
            #doesnt exit
            exit()
    except:
        pass


def main(stdscr: curses.window):
    print(1)

    init_curses(stdscr)

    while True:
        check_key(stdscr)
        gE.draw_world(stdscr, world, pE.player1.pos)
        gE.draw_info(stdscr, pE.player1.pos)
        time.sleep(FPS)


wrapper(main)