import patoolib
import helper_functions
import ex1, ex2, ex3, ex4

PATH_EX1 = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex1"
PATH_NOISE_IMG = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex2\noised_img.png"
PATH_MYSTERIOUS_FILE = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex2\mysterious_file.npz"
PATH_RESULT_EX2 = r"C:\Users\Owner\Desktop\Project\Bar_python_exercise\ex2\result.png"

if __name__ == '__main__':
    # patoolib.extract_archive("Bar_python_exercise.rar")
    print("main")

    print("************** EX 1 **************")
    print("Decode namefiles")
    # ex1.decode_filenames(PATH_EX1)

    print("************** EX 2 **************")
    print("Decode picture")
    # ex2.decode_message_from_picture(PATH_NOISE_IMG, PATH_MYSTERIOUS_FILE, PATH_RESULT_EX2)

    print("************** EX 3 **************")
    print("Return to original dates as filenames")
    # ex3.return_to_original_dates_as_filenames()

    print("************** EX 4 **************")
    ex4.save_an_one_npz_with_all_files()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
