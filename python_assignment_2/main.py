import numpy as np
from numpy import asarray as image_as_numpy_array
from PIL import image


def main():
    npz_loaded_file = np.load(".\\ex2\\mysterious_file.npz")
    numpy_of_image_with_background = image.fromarray(npz_loaded_file.get("arr_0"))

    img = image.open(".\\ex2\\noised_img.png")
    numpy_background_image_data = image_as_numpy_array(img)

    new_image_as_numpy_array_without_background = numpy_background_image_data - numpy_of_image_with_background

    only_number_without_background = image.fromarray(new_image_as_numpy_array_without_background)
    only_number_without_background.save('mysterious_message.png')


if __name__ == '__main__':
    main()
