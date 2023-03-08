import base64
import os
import pickle
import datetime

import numpy as np
from PIL import Image

def decode_ex1(path):
    os.chdir(path)
    cwd = os.getcwd()
    print(cwd)
    for dirname in os.listdir(cwd):
        d = os.path.join(cwd, dirname)
        # checking if it is a file
        if os.path.isdir(d):
            os.rename(d, os.path.join(cwd, base64.b32decode(dirname).decode('utf-8')))
