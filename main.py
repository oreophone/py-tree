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
from math import sin

def main(stdscr: window):
    x = Display(stdscr, doDebug=True)
    x.setDebugMessage("Randomised Testing")
    t = 0
    stars = [(randint(0,70),randint(1,30)) for i in range(33)]
    while True:
        x.clearAll()
        l = Line2D(Point2D(17-10*sin(t+0.9),15-8*sin(t+0.9)), Point2D(45+4*sin(t+0.3),15 + 13*sin(t)))
        d = Drawer(
            l,
            list("x"),
            [ANSIColour(5,0,0)]
        )
        L = Line2D(Point2D(44+7*sin(2*t),28), Point2D(33-17*sin(2*t),13))
        D = Drawer(
            L,
            list("*"),
            [ANSIColour(0,5,3)]
        )
        X = Line2D(Point2D(55,2), Point2D(59 + 4*sin(1.3*t + 3),13+10*sin(1.3*t + 3)))
        Q = Drawer(
            X,
            list("%@#^()"),
            [ANSIColour(3,4,0)]
        )

        ps = [Pixel(p,str(round(t) % 10),ANSIColour(2,2,2)) for p in stars]

        x.draw(
            ps,d,D,Q
        )
        x.refresh()

        time.sleep(1/60)
        t += 0.1
    # TODO handle other stuff

wrapper(main)

