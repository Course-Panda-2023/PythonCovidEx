import base64
import os
import pickle
import datetime

import numpy as np
from PIL import Image

def fixex3(path):
    for dir in os.listdir(path):
        dirPath =path+"\\"+dir
        for file in os.listdir(dirPath):
            filePath=dirPath+"\\"+file
            os.rename(filePath,filePath+".npz")

def decode_ex3(path):
    b = False
    performance_dict_unpacked = {}
    os.chdir(path)
    cwd = os.getcwd()
    print(cwd)
    for dirname in os.listdir(cwd):
        d = os.path.join(cwd, dirname)
        # checking if it is a file
        if os.path.isdir(d):
            for filename in os.listdir(d):
                with open(os.path.join(d, filename), 'rb') as pick:
                    performance_dict_unpacked.update(pickle.load(pick))
                if (len(performance_dict_unpacked['IZEVAUY=']) > 2):
                    b = True
                    break
            if (b):
                break

    for dir in performance_dict_unpacked:
        dirdecoded = base64.b32decode(dir).decode('utf-8')
        path = r'C:\Users\mamag2\Desktop\eyal\python\project1\ex1\\'
        dirpath = path + dirdecoded
        for f in os.listdir(dirpath):
            nums = f[:-4].split('_')
            date=performance_dict_unpacked[dir][int(nums[1])]+int(nums[0])
            fdate = datetime.datetime.fromtimestamp(date).date()

            d = os.path.join(dirpath,f)
            # checking if it is a file
            if os.path.isfile(d):
                os.rename(d, os.path.join(dirpath,str(fdate)))

    print("\n", dirname, len(performance_dict_unpacked), len(performance_dict_unpacked['IZEVAUY=']), " - ",performance_dict_unpacked, "\n")
