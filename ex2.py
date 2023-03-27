from PIL import Image
from numpy import asarray
from numpy import load
from matplotlib import cm
import numpy as np


def decode_message_from_picture(picture_path : str, mysterious_file_path : str, save_file_path: str):

    img = Image.open(picture_path)

    data = load(mysterious_file_path)
    lst = data.files
    result_numpy = asarray(img) - data[lst[0]]

    img = Image.fromarray(result_numpy)
    img.save(save_file_path)
    # img.show()