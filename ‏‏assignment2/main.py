import numpy as np
from numpy import asarray as ImageAsNumpyArray
from PIL import Image


def npz_file_to_console():
    npz_loaded_file = np.load(".\\ex2\\mysterious_file.npz")
    for key_from_npz_file in npz_loaded_file.keys():
        print(key_from_npz_file)

    data = Image.fromarray(npz_loaded_file.get("arr_0"))

    # saving the final output
    # as a PNG file
    data.save('gfg_dummy_pic.png')


def main():
    npz_loaded_file = np.load(".\\ex2\\mysterious_file.npz")
    numpy_of_image_with_background = Image.fromarray(npz_loaded_file.get("arr_0"))

    img = Image.open(".\\ex2\\noised_img.png")
    numpy_background_image_data = ImageAsNumpyArray(img)

    new_image_as_numpy_array_without_background = numpy_background_image_data - numpy_of_image_with_background

    only_number_without_background = Image.fromarray(new_image_as_numpy_array_without_background)
    only_number_without_background.save('mysterious_message.png')


if __name__ == '__main__':
    main()
