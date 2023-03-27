import base64
import glob
import os
import pickle


def decode_base32(string):
    byte_val = string.encode("UTF-8")
    # Decoding the Base32 bytes
    decode_val = base64.b32decode(byte_val)
    # Decoding the bytes to string
    ret_val = decode_val.decode("UTF-8")
    return ret_val


def get_all_files_end_with(dictionary, end):
    os.chdir(dictionary)
    for file in glob.glob(end):
        return file

