import base64
import os
import pickle
import datetime

import numpy as np
from PIL import Image



def decode_ex2(pathFile, pathImage):
    mysteriosFile = np.load(pathFile)

    encodedImage = Image.open(pathImage)
    pix = np.asarray(encodedImage)

    dix = Image.fromarray(pix - mysteriosFile['arr_0'])
    dix.save(r'C:\Users\mamag2\Desktop\eyal\python\project1\ex2\decodedImage.png')

