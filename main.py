import os
import imagesize


def get_image_size(path):
    """
    Get the size of an image
    :param path: path to the image
    :return: width and height of the image
    """
    width, height = imagesize.get(path)
    return width, height


def rename_image():
    """
    Rename image files in a directory by size using the following format:
    <size>_<index>.<ext>
    """
    path = './img/'
    dict_sizes = {}
    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            width, height = get_image_size(path + filename)
            if (width, height) not in dict_sizes:
                dict_sizes[(width, height)] = 1
            else:
                dict_sizes[(width, height)] += 1
            new_name = str(width) + '_' + str(height) + '_' + \
                str(dict_sizes[(width, height)]) + '.' + filename.split('.')[1]
            os.rename(path + filename, path + new_name)


rename_image()
