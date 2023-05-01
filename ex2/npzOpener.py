from numpy import load
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


with load('C:\\Users\\dan-client\\Desktop\\vs code\\הכשרה\\python learning\\Bar_python_exercise\\ex2\\mysterious_file.npz') as data:
    lst = data.files
    for item in lst:
        #print(item)
        print(data[item])


def dechiperPicture():
    path_ex2 = "C:\\Users\\dan-client\\Desktop\\vs code\\הכשרה\\python learning\\Bar_python_exercise\\ex2"
    noise = np.asarray(Image.open(os.path.join(path_ex2, "noised_img.png")))

    mysterious_file = np.load(os.path.join(path_ex2, "mysterious_file.npz"), 'r')
    mystery_arr = mysterious_file.f.arr_0

    plt.imshow(noise - mystery_arr, interpolation='nearest')
    plt.show()

dechiperPicture() #answer: 110