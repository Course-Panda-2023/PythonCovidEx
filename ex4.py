import numpy as np
import shutil, os


def combine_folders(src_path, dst_path):
    for file_name in os.listdir(src_path):
        shutil.copy(src_path + file_name, dst_path + file_name)

# combine_folders("ex1/Case-Fatality_Ratio/", "ex1/Case_Fatality_Ratio/")
# combine_folders("ex1/Incidence_Rate/", "ex1/Incident_Rate/")


np_file = "C:/Users/User/Desktop/C#/Python/ex4/combined_files"
path = "ex1/"
folder_list = []
files = 0
folders = os.listdir(path)
for folder_name in os.listdir(path):
    file_list = []
    for file_name in os.listdir(path + folder_name):
        files = len(os.listdir(path + folder_name))
        current_path = path + folder_name + '/' + file_name
        temp = np.load(current_path, allow_pickle=True)['arr_0']
        max_size = 4016
        data = np.resize(temp, (max_size,))
        file_list.append(data)
    folder_list.append(file_list)
res = np.vstack(folder_list).reshape(len(folders), files, -1)
np.savez(np_file, res)
