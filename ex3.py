import pickle
import os
import base64
from datetime import datetime


def decrypt_dates():  # change
    dir_path = "ex3/6/6.pkl"
    with open(dir_path, 'rb') as pick_file:
        data_dict = pickle.load(pick_file)
    data_dict = {base64.b32decode(fold_name).decode('utf-8'): data_dict[fold_name] for fold_name in data_dict.keys()}

    for folder_name in os.listdir("ex1"):
        folder_path = os.path.join("ex1", folder_name)
        for file_name in os.listdir(folder_path):
            t_stamp, code = file_name.split('_')
            code = int(code.split('.')[0])
            decrypted_date = datetime.fromtimestamp(int(t_stamp) + int(data_dict[folder_name][code])).date()
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, f"{str(decrypted_date)}.npz"))

