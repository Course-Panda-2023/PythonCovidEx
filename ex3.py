import pickle
from datetime import datetime
import helper_functions
import os

PICKLE_PATH = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex3\6\6.pkl"
PART_1_PATH = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex1"


def return_to_original_dates_as_filenames():
    pickleFile = pickle.load(open(PICKLE_PATH, "rb"))

    for key in pickleFile.keys():
        dir_name = helper_functions.decode_base32(key)
        for index in pickleFile[key]:
            date_ex3 = pickleFile[key][index]  # the value from ex3
            directory = os.path.join(PART_1_PATH,dir_name)
            end = f"*_{index}.npz"
            found_file = helper_functions.get_all_files_end_with(directory, end)
            date_ex1 = found_file.split('_')[0]  # the value from ex1
            date_int = date_ex3 + int(date_ex1)  # addition between the integer in ex3 to integer in ex1
            datetime_final = datetime.fromtimestamp(date_int).date()  # the original date

            old_name = os.path.join(directory,found_file)

            new_name = f"{directory}\{datetime_final}.npz"
            print(old_name)
            print(new_name)
            os.rename(old_name, new_name)
