import os

import helper_functions


def decode_filenames(path: str):
    dir_list = os.listdir(path)
    os.chdir(path)

    for directory in dir_list:
        decode_dir_name = helper_functions.decode_base32(directory)
        os.rename(directory, decode_dir_name)
        print(decode_dir_name)
