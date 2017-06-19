from os import listdir, path
import random

imagetypes = [".jpg", ".jpeg", ".png", ".gif"]

def is_image(filename):
    """returns true if the file is an image type contained in the lookup table"""
    filename = filename.lower()
    filename, file_extension = path.splitext(filename)
    return file_extension in imagetypes

def random_pick(dir):
    """returns the file name of a random image from the directory"""
    images = [f for f in listdir(dir) if is_image(f)]
    return random.choice(images)
