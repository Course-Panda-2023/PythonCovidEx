import pickle
import helper_functions
PICKLE_PATH = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex3\6\6.pkl"


def save_an_one_npz_with_all_files():
    pickleFile = pickle.load(open(PICKLE_PATH, "rb"))
    keys_list = list(pickleFile.keys())
    decode_list = []

    for key in keys_list:
        decode_list.append(helper_functions.decode_base32(key))

    decode_list.remove('Case-Fatality_Ratio')
    decode_list.remove('Incident_Rate')




# dir_list = get_dir_names_ex3()
# total_arr = []
# for dir in sorted(dir_list):
#     dir_path = os.path.join(path, dir)
#     size_files = len(os.listdir(dir_path))
#     dir_arr = []
#     # print(dir_path)
#     for sub_dir in sorted(os.listdir(dir_path)):
#         sub_dir_path = os.path.join(dir_path, sub_dir)
#         load_numpy = numpy.load(sub_dir_path, allow_pickle=True)['arr_0']
#         dir_arr.append(load_numpy)
#     total_arr.append(dir_arr)
