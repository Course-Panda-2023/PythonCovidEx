import pickle, base64
import os
import datetime

def rename_files(folder_name, key, d):
    for file_name in os.listdir(path + folder_name + '/'):
        num = file_name.split('_')
        for i in d[key]:
            if(str(num[1])[:-4] == str(i)):
                my_source = path + folder_name + '/' + str(num[0]) + '_' + str(num[1])
                unixToDatetime = datetime.datetime.fromtimestamp(int(num[0]) + int(d[key][i]))
                my_dest = path + folder_name + '/' + str(unixToDatetime.date()) + ".npz"
                os.rename(my_source, my_dest)


dict_list = []
dictionary = {} 
# open the sixth file and append all the dicts to a dict_list.
with (open("ex3/6/6.pkl", "rb")) as openfile:
    while True:
        try:
            dict_list.append(pickle.load(openfile))
        except EOFError:
            break

# converts keys in dict_list.
for d in dict_list:
    for key in d:
        new_key = (str(base64.b32decode(key))[2:-1])
        dictionary[new_key] = d[key]
    dict_list.remove(d)
    dict_list.append(dictionary)
# print(dict_list)


path = "ex1/"
for d in dict_list:
    for key in d:
        for folder_name in os.listdir(path):
                if(key == folder_name):
                    rename_files(folder_name, key, d)

            


