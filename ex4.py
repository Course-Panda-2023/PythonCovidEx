import shutil
import os
import numpy as np


def save_data(data):
    if not os.path.exists("ex4"):
        os.makedirs("ex4")
        np.savez("ex4/data.npz", data)


def pad_array(data, max_len):
    for folder_data in data:
        for i in range(len(folder_data)):
            folder_data[i] = np.concatenate((folder_data[i], np.full(max_len - folder_data[i].size, np.nan)))
    data = np.vstack(data).reshape(len(data), -1, max_len)  # shape: num_of_folders, num_files_in_folder, max_length
    return data


def extract_data_from_files():
    folder_paths = [os.path.join("ex1", fold_name) for fold_name in os.listdir("ex1")]
    data = []
    max_len = 0  # get max length of file arrays, for padding
    for folder_path in folder_paths:
        folder_data = []
        for file in [os.path.join(folder_path, f_name) for f_name in os.listdir(folder_path)]:
            with np.load(file) as f:
                try:
                    file_arr = f['arr_0']
                    folder_data.append(file_arr)
                    max_len = max(max_len, file_arr.size)
                except ValueError:
                    folder_data.append(np.full(0, np.nan))

        data.append(folder_data)
    return data, max_len


def combine_data():  # extract data from files, stack to 1 np array, and save them
    data, max_len = extract_data_from_files()
    data_array = pad_array(data, max_len)
    save_data(data_array)


def fix_split_folders():  # transfer files from split folders
    for fold_src, fold_dest in [("ex1/Case-Fatality_Ratio", "ex1/Case_Fatality_Ratio"),
                                ("ex1/Incident_Rate", "ex1/Incidence_Rate")]:
        for f_name in os.listdir(fold_src):
            shutil.move(os.path.join(fold_src, f_name), fold_dest)
        shutil.rmtree(fold_src)
