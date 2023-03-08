import os
import base64


def decode_folder_names():
    src_folder_paths = [os.path.join("ex1", fold_name) for fold_name in os.listdir("ex1")]
    dest_folders_paths = [os.path.join("ex1", base64.b32decode(fold_name).decode('utf-8')) for fold_name in os.listdir("ex1")]
    for src_path, dest_path in zip(src_folder_paths, dest_folders_paths):
        os.rename(src_path, dest_path)

