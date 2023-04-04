import numpy as np
from PIL import Image as img


def main():
    file: np.lib.npyio.NpzFile = np.load(".\\ex2\\mysterious_file.npz")
    number_on_background: np.ndarray = img.fromarray(file.get("arr_0"))

    image = img.open(".\\ex2\\noised_img.png")
    background: np.ndarray = np.asarray(image)

    no_background_image: np.ndarray = background - number_on_background

    number_image = img.fromarray(no_background_image)
    number_image.save('mysterious_message.png')


if __name__ == '__main__':
    main()
