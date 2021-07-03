"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return GRAPH_MARGIN_SIZE + year_index * (width - GRAPH_MARGIN_SIZE*2) // len(YEARS)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_index = 0                 # The position of color in COLORS(list)
    previous_rank = 0               # To record the rank of 10 years ago
    for name in lookup_names:
        color_index %= len(COLORS)            # To repeat the color every four lines
        color = COLORS[color_index]
        color_index += 1
        year_index = 0              # The position of year in YEARS(list)
        for year in YEARS:
            if str(year) in name_data[name]:    # Names in top 1000
                rank = int(name_data[name][str(year)])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX, GRAPH_MARGIN_SIZE + rank *
                                   (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000, text=f'{name} {rank}', anchor=tkinter.SW,
                                   fill=color)
                if year_index == 0:             # The rank of the first data
                    previous_rank = rank
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index - 1),
                                       GRAPH_MARGIN_SIZE + previous_rank *
                                       (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000,
                                       get_x_coordinate(CANVAS_WIDTH, year_index),
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000,
                                       fill=color, width=LINE_WIDTH)
                    previous_rank = rank
            else:                               # Names not in top 1000
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX, CANVAS_HEIGHT -
                                   GRAPH_MARGIN_SIZE, text=f'{name} *', anchor=tkinter.SW, fill=color)
                rank = 1000               # Ranks within 1000 and ranks outside 1000 have the same position on the table
                if year_index == 0:
                    previous_rank = rank
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index - 1),
                                       GRAPH_MARGIN_SIZE + previous_rank *
                                       (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000,
                                       get_x_coordinate(CANVAS_WIDTH, year_index),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       fill=color, width=LINE_WIDTH)
                    previous_rank = rank
            year_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
