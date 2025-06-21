from display.Display import Display
import sched, time
from curses import wrapper, window
import curses
from display.Pixel import Pixel
from display.ANSIColour import ANSIColour

def main(stdscr: window):
    x = Display(stdscr, doDebug=True)
    x.setDebugMessage(curses.COLOR_PAIRS)
    v = Pixel((8,14),"$",ANSIColour(5,5,5))
    a = Pixel((9,14),"#",ANSIColour(0,5,5))
    while True:
        x.drawDebug()
        x.drawPixel(v)
        x.drawPixel(a)
        x.refresh()
        time.sleep(0.1)
    # TODO handle other stuff

wrapper(main)

