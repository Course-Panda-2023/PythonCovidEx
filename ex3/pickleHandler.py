import sys
import pickle
sys.path.insert(1, 'ex1')
import decoder
import os
import re
import datetime

def get_substr(sampleStr:str, char1, char2) -> str: 
    regexPattern = char1 + '(.+)' + char2
    try:
        str_found = re.search(regexPattern, sampleStr).group(1)
    except AttributeError:
        str_found = 'Nothing found between two markers'
    return str_found

def Decodepkl(pklfile : str):
    with open('C:\\Users\\dan-client\\Desktop\\vs_code\\training\\python_learning\\Bar_python_exercise\\ex3\\files'+pklfile, 'rb') as file1:
        data: dict = pickle.load(file1)
        for key,value in data.items():
            #print(decoder.decode(key))
            folder1_path = 'C:\\Users\\dan-client\\Desktop\\vs_code\\training\\python_learning\\Bar_python_exercise\\ex1\\files\\' + decoder.decode(key)
            folder1 = os.listdir(folder1_path)
            for filename in folder1:
                keytodict = get_substr(filename,'_','.npz')
                fileNumber = filename.split('_')[0]
                newName = str(datetime.datetime.fromtimestamp((value[int(keytodict)]) + int(fileNumber)).date()) + '_' + keytodict + ".npz"
                os.rename(folder1_path + '\\' + filename, folder1_path + '\\' + newName)
#Decodepkl("\\6\\6.pkl")    # this was to be activated ONCE which i did