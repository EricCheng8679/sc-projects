"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: To produce a photo without passersby by using
      multiple photos of the same scene existing passersby
      to find the most suitable pixels.
"""
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    return [red//len(pixels), green//len(pixels), blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # Method 1: By dictionary
    dist_dic = {}
    i = 0                               # Index of pixel position in pixels
    for pixel in pixels:                # Dictionary: key is an index , value is a RGB mean distance of pixel
        dist_dic[i] = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        i += 1
    best_pair = min(dist_dic.items(), key=lambda s: s[1])  # To find the best pixel-distance pair after converting pairs into tuple form
    best_pixel_index = best_pair[0]                        # The best index of pixel position in pixels
    print(best_pixel_index)
    return pixels[best_pixel_index]

    ### Method 2:By list ###
    # dist_list = []
    # pixel_index = 0                     # Recording position of best pixel in pixels list
    # for pixel in pixels:                # To list all corresponding distances from the average RGB of pixels
    #     dist = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
    #     dist_list.append(dist)
    # min_distance = min(dist_list)
    # for i in range(len(dist_list)):     # To find the index of best pixel
    #     if min_distance == dist_list[i]:
    #         pixel_index = i
    #         break
    #     else:
    #         pixel_index += 1
    # return pixels[pixel_index]

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):                      # To list every pixel in an image
        for y in range(height):
            pixels = []
            for i in range(len(images)):        # To list the pixels of each image at the same position coordinate
                pixel = images[i].get_pixel(x, y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red   # To fill best pixel into canvas of result
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))  # To make a filename list
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:               # jpgs = [filename1,filename2,filename3,...]
        print("Loading", filename)
        image = SimpleImage(filename)   # open image
        images.append(image)            # To make an image list
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]             # sys.argv[0] = stanCodoshop.py
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])   # args[0] =sys.argv[1] = hoover/clock-tower/math-corner/monster (photos in a folder)
    solve(images)


if __name__ == '__main__':
    main()
