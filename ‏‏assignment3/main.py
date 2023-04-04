import pickle as pck
import os
from datetime import datetime as dt
import constants as cons
import base64


def load_pickle_file():
    source = cons.PICKLE_FULL_PATH
    result_dict = {}

    with open(source, 'rb') as file:
        loaded_pickle_file = pck.load(file)
    for key in loaded_pickle_file.keys():
        result_dict[base64.b32decode(key).decode('utf-8')] = loaded_pickle_file[key]

    return result_dict


def the_filename_without_suffix(filename, suffix_size):
    return filename[:-suffix_size]


def rename_ex1_file(directory, file_filename_as_timestamp, pickle_timestamp, filename):
    full_path_of_directory = cons.PATH_OF_EX1_DIRECTORY + "\\" + directory
    os.chdir(full_path_of_directory)
    file_name_as_timestamp = pickle_timestamp + file_filename_as_timestamp
    timestamp_to_date = str(dt.fromtimestamp(file_name_as_timestamp).date())

    correct_filename = timestamp_to_date + cons.DOT_NPZ_SUFFIX

    os.rename(filename, correct_filename)


def rename_ex1_directory(directory, dictionary):
    full_path_of_directory = cons.PATH_OF_EX1_DIRECTORY + "\\" + directory

    all_files_in_directory = os.listdir(full_path_of_directory)

    for file_filename in all_files_in_directory:
        filename_prefix = the_filename_without_suffix(file_filename, cons.SIZE_OF_PREFIX_DOT_NPZ)
        if cons.SEPARATOR_BY_UNDERSCORE not in filename_prefix:
            continue
        timestamp_of_file, identifier_of_file = filename_prefix.split(cons.SEPARATOR_BY_UNDERSCORE)
        pickle_timestamp_as_int = int(dictionary[int(identifier_of_file)])
        rename_ex1_file(directory, int(timestamp_of_file), pickle_timestamp_as_int, file_filename)


def rename_directories_files():
    loaded_pickle_file = load_pickle_file()

    directories_names_list = os.listdir(cons.PATH_OF_EX1_DIRECTORY)

    for directory in directories_names_list:
        if directory not in loaded_pickle_file.keys():
            continue

        rename_ex1_directory(directory, loaded_pickle_file[directory])


def main():
    rename_directories_files()


if __name__ == '__main__':
    main()
