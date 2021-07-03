"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

BLURRED_SCALE = 9


def blur(old_img):
    """
    :param old_img: a original image
    :return: a blurred image
    """
    blur_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            if x == 0 and y == 0:                               # Upper left corner
                old_pixel_00 = old_img.get_pixel(x, y)          # Reference point
                old_pixel_s = old_img.get_pixel(x, y + 1)       # South
                old_pixel_e = old_img.get_pixel(x + 1, y)       # East
                old_pixel_se = old_img.get_pixel(x + 1, y + 1)  # Southeast
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_00.red + old_pixel_s.red + old_pixel_e.red + old_pixel_se.red) // 4
                blur_pixel.green = (old_pixel_00.green + old_pixel_s.green + old_pixel_e.green + old_pixel_se.green) \
                    // 4
                blur_pixel.blue = (old_pixel_00.blue + old_pixel_s.blue + old_pixel_e.blue + old_pixel_se.blue) // 4
            elif x == 0 and y == old_img.height - 1:            # Bottom left
                old_pixel_0h = old_img.get_pixel(x, y)
                old_pixel_n = old_img.get_pixel(x, y - 1)       # North
                old_pixel_e = old_img.get_pixel(x + 1, y)
                old_pixel_ne = old_img.get_pixel(x + 1, y - 1)  # Northeast
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_0h.red + old_pixel_n.red + old_pixel_e.red + old_pixel_ne.red) // 4
                blur_pixel.green = (old_pixel_0h.green + old_pixel_n.green + old_pixel_e.green + old_pixel_ne.green) \
                    // 4
                blur_pixel.blue = (old_pixel_0h.blue + old_pixel_n.blue + old_pixel_e.blue + old_pixel_ne.blue) // 4
            elif x == old_img.width - 1 and y == 0:             # Upper right corner
                old_pixel_w0 = old_img.get_pixel(x, y)
                old_pixel_s = old_img.get_pixel(x, y + 1)
                old_pixel_w = old_img.get_pixel(x - 1, y)       # West
                old_pixel_sw = old_img.get_pixel(x - 1, y + 1)  # Southwest
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_w0.red + old_pixel_s.red + old_pixel_w.red + old_pixel_sw.red) // 4
                blur_pixel.green = (old_pixel_w0.green + old_pixel_s.green + old_pixel_w.green + old_pixel_sw.green) \
                    // 4
                blur_pixel.blue = (old_pixel_w0.blue + old_pixel_s.blue + old_pixel_w.blue + old_pixel_sw.blue) // 4
            elif x == old_img.width - 1 and y == old_img.height - 1:  # Bottom right corner
                old_pixel_wh = old_img.get_pixel(x, y)
                old_pixel_n = old_img.get_pixel(x, y - 1)
                old_pixel_w = old_img.get_pixel(x - 1, y)
                old_pixel_nw = old_img.get_pixel(x - 1, y - 1)        # Northwest
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_wh.red + old_pixel_n.red + old_pixel_w.red + old_pixel_nw.red) // 4
                blur_pixel.green = (old_pixel_wh.green + old_pixel_n.green + old_pixel_w.green + old_pixel_nw.green) \
                    // 4
                blur_pixel.blue = (old_pixel_wh.blue + old_pixel_n.blue + old_pixel_w.blue + old_pixel_nw.blue) // 4
            elif x == 0 and y != 0 and y != old_img.height - 1:       # Left side except for head and tail
                old_pixel_0y = old_img.get_pixel(x, y)
                old_pixel_n = old_img.get_pixel(x, y - 1)
                old_pixel_s = old_img.get_pixel(x, y + 1)
                old_pixel_ne = old_img.get_pixel(x + 1, y - 1)
                old_pixel_e = old_img.get_pixel(x + 1, y)
                old_pixel_se = old_img.get_pixel(x + 1, y + 1)
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_0y.red + old_pixel_n.red + old_pixel_s.red + old_pixel_ne.red +
                                  old_pixel_e.red + old_pixel_se.red) // 6
                blur_pixel.green = (old_pixel_0y.green + old_pixel_n.green + old_pixel_s.green + old_pixel_ne.green +
                                    old_pixel_e.green + old_pixel_se.green) // 6
                blur_pixel.blue = (old_pixel_0y.blue + old_pixel_n.blue + old_pixel_s.blue + old_pixel_ne.blue +
                                   old_pixel_e.blue + old_pixel_se.blue) // 6
            elif y == 0 and x != 0 and x != old_img.width - 1:        # Top except for head and tail
                old_pixel_x0 = old_img.get_pixel(x, y)
                old_pixel_w = old_img.get_pixel(x - 1, y)
                old_pixel_sw = old_img.get_pixel(x - 1, y + 1)
                old_pixel_s = old_img.get_pixel(x, y + 1)
                old_pixel_e = old_img.get_pixel(x + 1, y)
                old_pixel_se = old_img.get_pixel(x + 1, y + 1)
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_x0.red + old_pixel_w.red + old_pixel_s.red + old_pixel_sw.red +
                                  old_pixel_e.red + old_pixel_se.red) // 6
                blur_pixel.green = (old_pixel_x0.green + old_pixel_w.green + old_pixel_s.green + old_pixel_sw.green +
                                    old_pixel_e.green + old_pixel_se.green) // 6
                blur_pixel.blue = (old_pixel_x0.blue + old_pixel_w.blue + old_pixel_s.blue + old_pixel_sw.blue +
                                   old_pixel_e.blue + old_pixel_se.blue) // 6
            elif x == old_img.width - 1 and y != 0 and y != old_img.height - 1:  # right side except for head and tail
                old_pixel_wy = old_img.get_pixel(x, y)
                old_pixel_n = old_img.get_pixel(x, y - 1)
                old_pixel_nw = old_img.get_pixel(x - 1, y - 1)
                old_pixel_w = old_img.get_pixel(x - 1, y)
                old_pixel_sw = old_img.get_pixel(x - 1, y + 1)
                old_pixel_s = old_img.get_pixel(x, y + 1)
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_wy.red + old_pixel_n.red + old_pixel_s.red + old_pixel_nw.red +
                                  old_pixel_w.red + old_pixel_sw.red) // 6
                blur_pixel.green = (old_pixel_wy.green + old_pixel_n.green + old_pixel_s.green + old_pixel_nw.green +
                                    old_pixel_w.green + old_pixel_sw.green) // 6
                blur_pixel.blue = (old_pixel_wy.blue + old_pixel_n.blue + old_pixel_s.blue + old_pixel_nw.blue +
                                   old_pixel_w.blue + old_pixel_sw.blue) // 6
            elif y == old_img.height - 1 and x != 0 and x != old_img.width - 1:  # Bottom except for head and tail
                old_pixel_xh = old_img.get_pixel(x, y)
                old_pixel_w = old_img.get_pixel(x - 1, y)
                old_pixel_nw = old_img.get_pixel(x - 1, y - 1)
                old_pixel_n = old_img.get_pixel(x, y - 1)
                old_pixel_ne = old_img.get_pixel(x + 1, y - 1)
                old_pixel_e = old_img.get_pixel(x + 1, y)
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_xh.red + old_pixel_w.red + old_pixel_nw.red + old_pixel_n.red +
                                  old_pixel_e.red + old_pixel_ne.red) // 6
                blur_pixel.green = (old_pixel_xh.green + old_pixel_w.green + old_pixel_nw.green + old_pixel_n.green +
                                    old_pixel_e.green + old_pixel_ne.green) // 6
                blur_pixel.blue = (old_pixel_xh.blue + old_pixel_w.blue + old_pixel_nw.blue + old_pixel_n.blue +
                                   old_pixel_e.blue + old_pixel_ne.blue) // 6
            else:  # middle parts having 8 neighbors
                old_pixel_xy = old_img.get_pixel(x, y)
                old_pixel_w = old_img.get_pixel(x - 1, y)
                old_pixel_nw = old_img.get_pixel(x - 1, y - 1)
                old_pixel_n = old_img.get_pixel(x, y - 1)
                old_pixel_ne = old_img.get_pixel(x + 1, y - 1)
                old_pixel_s = old_img.get_pixel(x, y + 1)
                old_pixel_sw = old_img.get_pixel(x - 1, y + 1)
                old_pixel_e = old_img.get_pixel(x + 1, y)
                old_pixel_se = old_img.get_pixel(x + 1, y + 1)
                blur_pixel = blur_img.get_pixel(x, y)
                blur_pixel.red = (old_pixel_xy.red + old_pixel_w.red + old_pixel_nw.red + old_pixel_n.red +
                                  old_pixel_e.red + old_pixel_ne.red + old_pixel_s.red + old_pixel_sw.red +
                                  old_pixel_se.red) // 9
                blur_pixel.green = (old_pixel_xy.green + old_pixel_w.green + old_pixel_nw.green + old_pixel_n.green +
                                    old_pixel_e.green + old_pixel_ne.green + old_pixel_s.green + old_pixel_sw.green +
                                    old_pixel_se.green) // 9
                blur_pixel.blue = (old_pixel_xy.blue + old_pixel_w.blue + old_pixel_nw.blue + old_pixel_n.blue +
                                   old_pixel_e.blue + old_pixel_ne.blue + old_pixel_s.blue + old_pixel_sw.blue +
                                   old_pixel_se.blue) // 9
    return blur_img


def main():
    """
    This program blurs a image. The practical approach is to find average values of RGB with adjacent pixels
    Then,it would show the blurred one by repeating the above approach some times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLURRED_SCALE):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
