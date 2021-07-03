"""
File: bouncing_ball.py
Name: Eric Cheng
-------------------------
This function simulates the process of bounce.
The process will start once we click mouse. Furthermore,the extra
mouse clicks would not affect the process while ball is bouncing.
After the bounce process is executed three times, clicking the mouse will be invalid.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 50
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
start_process = False       # record whether bouncing process is running
n = 0                       # count the times of bouncing process


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)


def bouncing(mouse):
    global start_process, n
    if n < 3 and not start_process:
        start_process = True                            # make extra mouse clicks be invalid while bouncing
        vy = 0
        while True:
            vy += GRAVITY
            ball.move(VX, vy)
            if ball.y >= window.height-ball.height:     # touch ground
                ball.y = window.height-ball.height      # ensure ball bounce from ground
                vy = -vy * REDUCE                       # initial vertical velocity after bouncing
            elif ball.x >= window.width:                # go through the right side of the window
                ball.x = START_X
                ball.y = START_Y
                start_process = False
                n += 1
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
