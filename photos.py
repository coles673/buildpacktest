import os
import random


def images():
    files = os.listdir("photos")
    return random.choice(files)
