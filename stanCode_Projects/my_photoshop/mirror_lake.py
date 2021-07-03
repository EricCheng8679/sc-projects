"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file directory of the original image
    :return: flip-vertical image
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height * 2)  # generating a blank image of double height
    for x in range(img.width):
        for y in range(img.height):
            every_color_of_pixel = img.get_pixel(x, y)
            upper_blank = blank_img.get_pixel(x, y)                        # upper part of blank image
            lower_blank = blank_img.get_pixel(x, blank_img.height - 1 - y) # lower part of blank_image

            upper_blank.red = every_color_of_pixel.red
            upper_blank.green = every_color_of_pixel.green
            upper_blank.blue = every_color_of_pixel.blue

            lower_blank.red = every_color_of_pixel.red
            lower_blank.green = every_color_of_pixel.green
            lower_blank.blue = every_color_of_pixel.blue
    return blank_img


def main():
    """
    This program generates a flip-vertical image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
