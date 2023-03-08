import base64
import os
import pickle
import datetime

import numpy as np
from PIL import Image


def ex4f(path):
    l = []

    for dir in os.listdir(path):
        li = []
        dirPath=os.path.join(path,dir)
        arr = os.listdir(os.path.join(path,dir))
        for file in arr:
            filePath=os.path.join(dirPath,file)
            tempArr=np.load(filePath,allow_pickle=True)
            li.append(np.append(tempArr['arr_0'],[np.nan] * (4016 - tempArr['arr_0'].shape[0])))
        l.append(li)

    nparray=np.vstack(l).reshape(len(os.listdir(path)),len(os.listdir(path+"\\"+os.listdir(path)[0])),-1)
    np.savez(r'C:\Users\mamag2\Desktop\eyal\python\project1\ex4\ex4.npz',nparray)

