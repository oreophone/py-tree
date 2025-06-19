from display.Display import Display
import sched, time
from curses import wrapper, window

def main(stdscr: window):
    x = Display(stdscr, doDebug=True)
    while True:
        x.drawDebug(False)
        time.sleep(0.1)
    # TODO handle other stuff

wrapper(main)

## remove on final version
def tests():
    s = sched.scheduler(time.time, time.sleep)
    def g(): print("Hello, sched!")
    s.enter(1,0,g)
    s.run()
    print("Hi!")
