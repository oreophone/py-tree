from display.Display import Display
import sched, time
from curses import wrapper, window
import curses
from display.Drawer import Drawer
from display.Pixel import Pixel
from display.ANSIColour import ANSIColour
from geometry.Line2D import Line2D
from geometry.Point2D import Point2D
from random import randint

def main(stdscr: window):
    x = Display(stdscr, doDebug=True)
    x.setDebugMessage(curses.COLOR_PAIRS)
    while True:
        x.clearAll()
        v = Pixel((randint(0,40),randint(1,28)),"$",ANSIColour(5,5,5))
        l = Line2D(Point2D(randint(0,40),randint(1,28)), Point2D(randint(0,40),randint(1,28)))
        d = Drawer(
            l,
            ["x","#"],
            [ANSIColour(5,0,0),ANSIColour(randint(0,5),randint(0,5),randint(0,5))]
        )

        x.draw(
            v,d
        )
        x.refresh()
        time.sleep(0.02)
    # TODO handle other stuff

wrapper(main)

