import base64
import datetime
import os
import pickle

import numpy as np
from PIL import Image


# excresice 1
def decrypt_directories(directory):
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]  # get all directories
    for d in directories:
        full_path = os.path.join(directory, d)  # get full path to directory
        decrypted_name = base64.b32decode(bytearray(d, 'ascii')).decode('utf-8')  # decrypt the directory name
        os.rename(full_path, os.path.join(directory, decrypted_name))  # rename it with the new name!


# decrypt_directories("ex1")

# excresize 2

def decrypt_image():
    mystery_file_load = np.load('ex2/mysterious_file.npz')  # load the numpy archive
    mystery_array = mystery_file_load['arr_0']  # load the array inside the archive
    noised_image_array = np.asarray(Image.open('ex2/noised_img.png'))
    decrypted_array = noised_image_array - mystery_array
    img = Image.fromarray(np.uint8(decrypted_array))  # decrypt the image...
    img.save('decrypted_image.png')  # and save it!


# decrypt_image()

# excrecsie 3

def decrypt_pickles(directory_path):
    stack = [directory_path]
    result = []
    while stack:
        folder_path = stack.pop()  # go over every folder in ex3
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)  # get file path
            if os.path.isdir(filepath):
                stack.append(filepath)  # add another folder to the stack to check for
            elif filename.endswith('.pkl'):
                with open(filepath, 'rb') as f:  # load the files if ends with .pkl
                    data = pickle.load(f)
                    decrypted_dict = decrypt_dict_key(data)  # process the dictionary
                    result.append(decrypted_dict)
    return result


def decrypt_dict_key(data):
    decrypted_dict = {}
    for key, value in data.items():  # go over key and value
        decrypted_key = base64.b32decode(bytearray(key, 'ascii')).decode('utf-8')
        decrypted_dict[decrypted_key] = value  # decrypt only the key, keep the value
    return decrypted_dict


# print(decrypt_pickles("ex3"))
# it seems to show a list of dictionaries for every file, but in index 43 there is something suspicious...
# after investigation, could index 43 be the index for all the index pointers of ex1?
# by summing the values of both the dictionary and the ex1 index values: we can get a unix time value for a certain date

def find_index_ndict(index):
    suspicious_index = decrypt_pickles("ex3")[43]
    for OUTER_KEY in suspicious_index:  # get folder name in outer key
        for INNER_KEY in suspicious_index[OUTER_KEY]:  # get all indexes (key) and values inside the folder
            if INNER_KEY == index:
                return suspicious_index[OUTER_KEY][INNER_KEY]  # return the values when found


def split_file(filename):
    basename = os.path.basename(filename)  # get filename without path prefix
    filename_without_ext = os.path.splitext(basename)[0]  # remove file extension
    new_string = filename_without_ext.split('_')  # split filename on underscore
    return new_string[0], new_string[1]


def get_unix_time(file_value, dict_value):
    return str(
        datetime.datetime.fromtimestamp(int(split_file(file_value)[0]) + dict_value))  # convert the unix time to date


def remove_path_from_file(file_path):
    file_name = os.path.basename(file_path)  # extracts filename from path
    return file_name


def search_file(directory, index):
    for item in os.listdir(directory):  # iterate over every folder/file inside the directory
        item_path = os.path.join(directory, item)  # set item path
        if os.path.isdir(item_path):
            result = search_file(item_path, index)  # search for index recursively until found
            if result:
                return result
        elif os.path.isfile(item_path):
            string, file_index = split_file(item)  # split file
            if file_index == str(index):  # if they match, return index
                return item_path
    return None


def calculate_date(index):  # the final function
    return get_unix_time(remove_path_from_file(search_file("ex1", index)), find_index_ndict(index))


def decrypt_dates(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  # get the file path
            file_name = remove_path_from_file(file_path)  # get the file name
            raw_split_file = split_file(file_name)  # split the file to get the index
            date = calculate_date(int(raw_split_file[1]))
            new_file_name = date.replace(':', '_').replace('/',
                                                           '-')  # replace invalid characters with allowed characters
            new_file_path = os.path.join(root, new_file_name)  # concatenate the directory path with the new file name
            os.rename(file_path, new_file_path + ".npz")
    print("finished")


# decrypt_dates("ex1")

# exc 4
def create_table_np(directory_path):
    subdirs = [f.path for f in os.scandir(directory_path) if f.is_dir()] # get all subdirectories in the given directory
    folder_dict = {}
    for subdir in subdirs: # loop through each subdirectory
        folder_name = os.path.basename(subdir) # get the folder name from the subdirectory path
        files = [f.name for f in os.scandir(subdir) if f.is_file()] # get all files in the subdirectory
        if folder_name not in folder_dict:
            folder_dict[folder_name] = [files]
        else:
            folder_dict[folder_name].append(files)
    # create numpy arrays from the folder and file names
    folder_names = []
    file_names = []
    for folder, files_list in folder_dict.items():
        folder_names.extend([folder] * len(files_list))
        for files in files_list:
            file_names.append(files)
    folder_array = np.array(folder_names)
    file_array = np.array(file_names)
    # stack the folder and file arrays horizontally to create the table
    table = np.column_stack((folder_array, file_array))
    np.savez('table.npz', table=table)



table = create_table_np("ex1")
b = np.load('table.npz')
print(b['table'])