import base64
import re
import datetime

import FileManager
import os

import numpy
import numpy as np
from PIL import Image
#ex1
# FileManager.DecodeFilesNameBase32("D:\pandaCourse\Python\covidEX\question\ex1")

#ex2
"""
file = np.load(r'D:\pandaCourse\Python\covidEX\question\ex2\mysterious_file.npz')
image = Image.open(r'D:\pandaCourse\Python\covidEX\question\ex2\noised_img.png')
imageArr = np.asarray(image)
newImage = Image.fromarray(imageArr+file['arr_0'])
newImage.save(r'D:\pandaCourse\Python\covidEX\question\ex2\newImage.png')
"""
basePath = 'D:\\pandaCourse\\Python\\covidEX\\question\\ex3'
"""
for i in range(150):
    currFile = np.load(basePath+'\\'+str(i)+'\\'+str(i)+'.pkl',allow_pickle=True)
    print(currFile)
"""


#ex3
# 6 is the exception file found by the method above
"""
currFile = np.load(basePath + '\\6\\6.pkl', allow_pickle=True)
#print (currFile)
for key in currFile:
    currFolderName=base64.b32decode(key).decode('utf-8')
    ex1FilePath= 'D:\\pandaCourse\\Python\\covidEX\\question\\ex1\\' + str(currFolderName)
    fileNames = os.listdir(ex1FilePath)
    for value in currFile[key]:
        for fileNameInEx1 in fileNames:
            template = "\w+_"+str(value)+".npz"
            if(re.search(template, fileNameInEx1)):
                newDateUnix = (int(currFile[key][value]) +int(fileNameInEx1.split('_')[0]))
                newDate = datetime.datetime.fromtimestamp(newDateUnix).date()
                os.rename(ex1FilePath +'\\'+ fileNameInEx1, ex1FilePath +'\\'+ str(newDate)+'.npz')
"""

#ex4
file_list = []
folder_list = []
big_list = []
number_of_files_in_a_folder=76
newFile = 'D:\\pandaCourse\\Python\\covidEX\\question\\ex4\\mixNPZs'
folderPath = 'D:\\pandaCourse\\Python\\covidEX\\question\\ex1'
folderNames = os.listdir(folderPath)
for currFolderName in folderNames:
    fileNames = os.listdir(folderPath+'\\'+currFolderName)
    folder_list.append(currFolderName)
    for fileName in fileNames:
        pathToCurrFile = folderPath+'\\'+currFolderName+'\\'+fileName
        loadedFile = np.load(pathToCurrFile, allow_pickle=True)
        new_max_length = 4016
        modified_loadedFile = np.resize(loadedFile, (new_max_length,))
        file_list.append(modified_loadedFile)
    big_list.append(file_list)


nparray=np.vstack(big_list).reshape(len(folderNames),number_of_files_in_a_folder,-1)
numpy.savez(newFile,nparray)