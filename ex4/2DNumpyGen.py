import numpy as np
import os

# Set the path to the directory containing the folders of npz files
data_dir = "C:\\Users\\dan-client\\Desktop\\vs_code\\training\\python_learning\\Bar_python_exercise\\ex1\\files"

# Get a list of the folder names
folder_names = sorted(os.listdir(data_dir))

# Initialize an empty dictionary to hold the arrays for each folder
folder_arrays = {}

# Loop through the folder names and load each npz file into an array
for folder_name in folder_names:
    folder_path = os.path.join(data_dir, folder_name)
    npz_files = sorted(os.listdir(folder_path))
    folder_arrays[folder_name] = []
    max_len = 0
    for npz_file in npz_files:
        npz_path = os.path.join(folder_path, npz_file)
        with np.load(npz_path, allow_pickle=True) as data:
            arr = data["arr_0"]
            max_len = max(max_len, len(arr))
            folder_arrays[folder_name].append(arr)
    # Pad arrays with zeros to ensure they all have the same length
    for i in range(len(folder_arrays[folder_name])):
        arr = folder_arrays[folder_name][i]
        if len(arr) < max_len:
            zeros = np.zeros(max_len - len(arr))
            folder_arrays[folder_name][i] = np.concatenate((arr, zeros))

# Stack the arrays for each folder into a single array
all_data = np.column_stack(tuple(folder_arrays.values()))

# Save the array to a npz file
np.savez("all_data.npz", all_data=all_data)
