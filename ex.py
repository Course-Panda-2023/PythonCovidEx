import numpy as np
from PIL import Image
import base64
import os
from PIL import Image as im
import datetime
import pickle5 as pickle
from datetime import datetime
def ex1():
    rootdir = r'C:\Users\omri tuito\Desktop\pythonProject8\ex1'
    for file in os.listdir(rootdir):
        old_file_name = os.path.join(rootdir, file)
        decode_name = base64.b32decode(file).decode('utf-8')
        new_file_name = os.path.join(rootdir, decode_name)
        os.rename(old_file_name,new_file_name)

def ex2():
    img = Image.open(r'C:\Users\omri tuito\Desktop\pythonProject8\ex2\noised_img.png')
    data_from_hacker = np.asarray(img)
    data_from_mysterious = np.load(r'C:\Users\omri tuito\Desktop\pythonProject8\ex2\mysterious_file.npz')
    data_from_mysterious = data_from_mysterious['arr_0']
    data_from_mysterious = im.fromarray(data_from_hacker - data_from_mysterious)
    data_from_mysterious.save('decode_image.png')


def get_dict():
    #Returns a dictionary for the conversions
    with open(r'C:\Users\omri tuito\Desktop\pythonProject8\ex3\6\6.pkl', "rb") as fh:
      data = pickle.load(fh)
      new_dict = {base64.b32decode(file).decode('utf-8'):data[file] for file in data.keys()}
    return new_dict

def edit_name_npz(folder_name,dict_convert):
    root_dir = 'ex1\\'+folder_name
    for file in os.listdir(root_dir):
        val,index = file.split('_')
        index = int(index.split('.')[0])
        val = int(val)
        dt = datetime.datetime.fromtimestamp(val + dict_convert[index])
        new_name = str(dt.date())+ ".npz"
        old_file_name = os.path.join(root_dir, file)
        new_file_name = os.path.join(root_dir, new_name)
        os.rename(old_file_name, new_file_name)
def ex3():
    dict_folder = get_dict()
    for key in dict_folder.keys():
        edit_name_npz(key,dict_folder[key])


def load_file(folder_name):
    root_dir = 'ex1\\'+folder_name
    file_names = sorted(os.listdir(root_dir), key=lambda x: datetime.strptime(x[:10], '%Y-%m-%d').date())
    a = []
    b = []
    for file_name in file_names:
        arr = np.load(root_dir+"\\"+file_name,allow_pickle=True)
        a.append(arr['arr_0'].shape)
        final_arr = np.append(arr['arr_0'], [np.nan] * (4016 - arr['arr_0'].shape[0])) #Complements each vector to size 4016
        b.append(final_arr)
    #print(set(a),folder_name,len(file_names))
    return np.array(b)
def ex4():
    rootdir = r'C:\Users\omri tuito\Desktop\pythonProject8\ex1'
    folder_names_sort = sorted(os.listdir(rootdir))
    f_mat = []
    for folder in folder_names_sort:
        a = load_file(folder)
        f_mat.append(a)
    f_mat:np.array = np.array(f_mat)
    f_mat = f_mat.reshape(76,14,4016)
    np.savez('ex4_arr.npz',f_mat)
