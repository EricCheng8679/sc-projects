"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.3

BLACK_PIXEL = 120


def main():
    """
    The photo looks like a person who is about to be put in prison,
    thus I combine it with a line chart of height.After that, I
    do gray scale processing on the synthesized photos.
    """
    fig = SimpleImage('image_contest/photo.jpg')
    bg = SimpleImage('image_contest/prison.jpg')
    bg.make_as_big_as(fig)
    combined_img = combine(bg, fig)
    gray_scale_img = grayscale(combined_img)
    gray_scale_img.show()


def combine(bg, fig):
    """
    :param bg: image, background
    :param fig: image, figure
    :return : fig, figure emerged in to background
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_fig = fig.get_pixel(x, y)
            avg = (pixel_fig.red+pixel_fig.blue+pixel_fig.green) // 3
            total = pixel_fig.red+pixel_fig.blue+pixel_fig.green
            if pixel_fig.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fig.red = pixel_bg.red
                pixel_fig.blue = pixel_bg.blue
                pixel_fig.green = pixel_bg.green
    return fig


def grayscale(img):
    """
    :param img: image
    :return : img, image processed by gray scale
    """
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    return img

if __name__ == '__main__':
    main()
