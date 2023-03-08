import datetime
from PIL import Image
import numpy as np
import base64
import os
import pickle
from pathlib import Path


def ex1(folder_path):
    for folder in folder_path.glob("*"):
        folder_encrypted_name = folder.name
        folder_decrypted_name = base64.b32decode(folder_encrypted_name)
        replace_name = folder_decrypted_name.decode('UTF-8')
        print(folder.parent)
        os.rename(str(folder), str(folder.parent) + "/" + str(replace_name))


def ex2():
    img = Image.open(r"C:\Users\Liav\PythonExercise\ex2\noised_img.png")
    data = np.asarray(img)
    mysterious_file = np.load(r"C:\Users\Liav\PythonExercise\ex2\mysterious_file.npz")
    decrypted_image = Image.fromarray(data - mysterious_file['arr_0'])
    decrypted_image.save(r"decoded_image.png")


def ex3(file_path):
    new_dict = {}
    with open(file_path, 'rb') as pkl:
        new_dict.update(pickle.load(pkl))
    for folder in new_dict:
        folder_decrypted = base64.b32decode(folder).decode('utf-8')
        path = r'C:\Users\Liav\PythonExercise\ex1\\'
        new_path = path + folder_decrypted
        for f in os.listdir(new_path):
            nums = f[:-4].split('_')
            date = new_dict[folder][int(nums[1])] + int(nums[0])
            file_date = datetime.datetime.fromtimestamp(date).date()
            the_file = os.path.join(new_path, f)
            if os.path.isfile(the_file):
                os.rename(the_file, os.path.join(new_path, str(file_date)))


def ex4(folder_path):
    l = []
    for folder in os.listdir(folder_path):
        li = []
        path = os.path.join(folder_path, folder)
        files = os.listdir(os.path.join(folder_path, folder))
        for f in files:
            file_path = os.path.join(path, f)
            tempArr = np.load(file_path, allow_pickle=True)
            li.append(np.append(tempArr['arr_0'], [np.nan] * (4016 - tempArr['arr_0'].shape[0])))
        l.append(li)

    nparray = np.vstack(l).reshape(len(os.listdir(folder_path)),
                                   len(os.listdir(folder_path + "\\" + os.listdir(folder_path)[0])), -1)
    np.savez(r'C:\Users\Liav\PythonExercise\ex4\ex4.npz', nparray)


ex4(r'C:\Users\Liav\PythonExercise\ex1')
