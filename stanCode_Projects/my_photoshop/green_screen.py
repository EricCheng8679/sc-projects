"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: image of background
    :param figure_img: image of figure
    :return: image :figure merged into background
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            fig = figure_img.get_pixel(x, y)
            bigger = max(fig.red, fig.blue)
            if fig.green > 2*bigger:
                bg = background_img.get_pixel(x, y)
                fig.red = bg.red
                fig.green = bg.green
                fig.blue = bg.blue
    return figure_img



def main():
    """
    This program combines figure with scene. We detect the green screen in ReyGreenScreen and
    replace the part of green screen with scene of space ship.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
