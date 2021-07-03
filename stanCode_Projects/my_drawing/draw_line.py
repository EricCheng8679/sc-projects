"""
File: draw_line.py
Name: Eric Cheng
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE_OF_CIRCLE = 10

# Global Variables
window = GWindow(width=500, height=400, title='Draw Lines')   # Canvas
x = 0                                                       # record the x coordinate of circle
y = 0                                                       # record the y coordinate of circle
one_circle = False                                          # whether the first circle exists
circle = GOval(0, 0)                                        # record circle on canvas


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_circle_or_line)  # mouse driven function


def create_circle_or_line(mouse):
    """
    This function controls what patter would be produced on the window when a mouse clicks
    """
    global x, y, one_circle, circle
    if not one_circle:
        circle = GOval(SIZE_OF_CIRCLE, SIZE_OF_CIRCLE)
        window.add(circle, mouse.x-SIZE_OF_CIRCLE/2, mouse.y-SIZE_OF_CIRCLE/2)
        x = mouse.x
        y = mouse.y
        one_circle = True
    else:
        line = GLine(x, y, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
        one_circle = False


if __name__ == "__main__":
    main()
