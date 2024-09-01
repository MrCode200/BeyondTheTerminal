import time

import curses
from curses import wrapper

import graphicsEngine as gE
import playerEngine as pE

run = True
FPS = 1/30
worldsize_r = 100
worldsize_c = 100

world = []

def init_curses(stdscr):
    curses.start_color()
    curses.curs_set(0)
    stdscr.nodelay(True)


def check_key(stdscr):
    try:
        key = stdscr.getkey()
        pE.check_key(key, stdscr)
        # Break if esc was hit
        if key == 'esc':
            curses.endwin()
    except:
        pass


def main(stdscr):
    init_curses(stdscr)


    while True:
        check_key(stdscr)
        time.sleep(FPS)


wrapper(main)