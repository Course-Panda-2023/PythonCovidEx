import base64
import datetime

import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import pickle
import codecs, json


def decode32(st):
    return str(base64.b32decode(st), 'utf-8')


def renameFiles():
    path = "C:/Users/dan-client/Downloads/Bar_python_exercise/ex1"
    for filename in os.listdir(path):
        old_name = path + "/" + filename
        new_name = path + "/" + decode32(filename)
        os.rename(old_name, new_name)


def show110():
    path_ex2 = "C:/Users/dan-client/Downloads/Bar_python_exercise/ex2"
    noise = np.asarray(Image.open(path_ex2 + "/noised_img.png"))

    mystery_npz = np.load(path_ex2 + "/mysterious_file.npz", 'r')
    mystery = mystery_npz.f.arr_0

    plt.imshow(noise - mystery, interpolation='nearest')
    plt.show()


def ex3t():
    i = 0
    for i in range(150):
        to_open = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex3/' + str(i) + '/' + str(i) + '.pkl'
        with open(to_open, 'rb') as handle:
            b = pickle.load(handle)

        to_print = ""
        for key in b:
            to_print += decode32(key) + " "
            to_print += str(list(b[key].keys())) + " "
            to_print += str(list((b[key].values()))[0]) + " "
        print(to_print)


def all_dates_in6():
    # return: a Dict[lil_num] -> List(Big num, folder) for each line in ex3/6/6.pkl
    to_open = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex3/6/6.pkl'
    with open(to_open, 'rb') as handle:
        b = pickle.load(handle)

    all_dates_in_6 = {}

    for folder_key in b:
        for lil_num_key in b[folder_key]:
            all_dates_in_6[lil_num_key] = [b[folder_key][lil_num_key], decode32(folder_key)]
    return all_dates_in_6

def all_ex1_unix_time():
    # return: List(big_num, lil_num) for each file in each folder in ex1
    path = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex1'
    all_ex1_unixtime = []
    for root, dirs, files in os.walk(path):
        for _file in files:
            removed_npz = _file[:-4]
            big_num, lil_num = removed_npz.split('_')
            #date = datetime.datetime.fromtimestamp(int(before_))
            all_ex1_unixtime.append([int(big_num), int(lil_num)])

    return all_ex1_unixtime


def filename_daytime():
    # return: dict[filepath] = daytime
    all_dates_in_6 = all_dates_in6()
    all_ex1_unixtime = all_ex1_unix_time()
    filename_daytime = {}
    for tzemed in all_ex1_unixtime:
        tot_unix_time = tzemed[0] + all_dates_in_6[tzemed[1]][0]
        path_to_file = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex1/' + all_dates_in_6[tzemed[1]][1] + '/'
        filename = str(tzemed[0]) + "_" + str(tzemed[1]) + ".npz"

        filename_daytime[filename] = [path_to_file, str(datetime.datetime.fromtimestamp(tot_unix_time))[:-9], all_dates_in_6[tzemed[1]][1]]
    return filename_daytime

def ex3combined():
    filename_daytime_ = filename_daytime()
    path = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex1'
    for root, dirs, files in os.walk(path):
        for _file in files:
            old_name = path + "/" + filename_daytime_[_file][2] + "/" + _file
            new_name = filename_daytime_[_file][0] + filename_daytime_[_file][1]
            os.rename(old_name, new_name)


def ex4():
    all_dates_all_fields = []
    #np_all_dates_all_fields = np.array()
    path = 'C:/Users/dan-client/Downloads/Bar_python_exercise/ex1'
    for root, dirs, files in os.walk(path):
        all_dates_in_field = []
        for _file in files:
            all_dates_in_field.append(_file)
        all_dates_all_fields.append(all_dates_in_field)
    all_dates_all_fields.pop(0)
    all_dates_all_fields.pop(0)
    answer = np.array(all_dates_all_fields)
    np.savez('C:/Users/dan-client/Downloads/Bar_python_exercise/ex4/answer.npz', answer)
    # print(answer)


if __name__ == '__main__':
    ex4()




