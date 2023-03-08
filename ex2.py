import numpy as np
import cv2 as cv
from PIL import Image


def decode_image():
    file = np.load("ex2/mysterious_file.npz")
    myst_arr = file['arr_0']
    im = cv.imread("ex2/noised_img.png")
    new_img = Image.fromarray(myst_arr[:, :, 1:] - im)
    new_img.save("decrypted.jpeg")



