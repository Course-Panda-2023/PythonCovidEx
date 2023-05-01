import base64
import os
from os import listdir


def decode(codedData: str)-> str:
    print(codedData)
    return( str(base64.b32decode(codedData), 'utf-8'))



def get_file_name(file_path: str) -> str:
    # file name with extension
    file_name = os.path.basename(file_path)

    # file name without extension
    return(os.path.splitext(file_name)[0])


def decode_folder(folder_path):
    for file in listdir(folder_path):
        os.rename(os.path.join(folder_path,get_file_name(file)),os.path.join(folder_path,decode(get_file_name(file))))

#decode_folder('ex1\\files')    # this was to be activated ONCE which i did