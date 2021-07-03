"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    According to the zoom factor, we take the coordinates of the shrunk image in the original image
    :param filename: str, the file directory of the original image
    :return shrunk_img: shrunk image
    """
    img = SimpleImage(filename)
    shrunk_img = img.blank(img.width // 2, img.height // 2)
    for x in range(shrunk_img.width):
        for y in range(shrunk_img.height):
            img_pixel = img.get_pixel(x * 2, y * 2)
            shrunk_pixel = shrunk_img.get_pixel(x, y)
            shrunk_pixel.red = img_pixel.red
            shrunk_pixel.green = img_pixel.green
            shrunk_pixel.blue = img_pixel.blue
    return shrunk_img


def main():
    """
    This function shrinks the original image to one fourth.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
