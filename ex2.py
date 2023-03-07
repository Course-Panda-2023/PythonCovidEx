

import numpy as np
from PIL import Image


def img_to_np(
        path: str
) -> np.ndarray:
    return np.asarray(Image.open(path))


def np_to_img(
        arr: np.ndarray
) -> Image:
    return Image.fromarray(arr)


def save_img(
        img: Image.Image,
        filepath: str
) -> None:
    img.save(filepath)


mysterious_arr: np.ndarray = np.load('dirs/ex2/mysterious_file.npz')['arr_0']

# load the image
noised_image_arr = img_to_np(
    path='dirs/ex2/noised_img.png'
)

decoded_arr: np.ndarray = noised_image_arr - mysterious_arr

print(decoded_arr.shape)


save_img(
    img=np_to_img(
        arr=decoded_arr
    ),
    filepath='decoded.png'
)


