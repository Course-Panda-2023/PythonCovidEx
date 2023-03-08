import numpy as np
import os

EX1_FULL_PATH = "C:\\Users\\AssafHillel\\Desktop\\python_assignment4\\ex1"


def main():
    directories_names = directories_names_ordered()
    numpy_arrays = [concatenate_npz_files(directory_name) for directory_name in directories_names]

    result = np.concatenate(numpy_arrays)
    np.savez("result.npz", result=result)
    loaded_npz = np.load("result.npz")['result']
    print(np.array_equal(np.asarray(loaded_npz), result))


def concatenate_npz_files(directory):
    npz_files = [file for file in os.listdir(os.path.join(EX1_FULL_PATH, directory)) if file.endswith('.npz')]
    arrays = [load_npz_file(os.path.join(EX1_FULL_PATH, directory, file)) for file in npz_files]
    return np.concatenate(arrays)


def load_npz_file(filepath):
    with np.load(filepath) as data:
        return np.asarray(data)


def directories_names_ordered():
    directories_names = []
    for index, directory_name in enumerate(os.listdir(EX1_FULL_PATH)):
        directories_names.append(directory_name)
    directories_names.sort()
    return directories_names


if __name__ == '__main__':
    main()