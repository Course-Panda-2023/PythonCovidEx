import os
import ex3
import time
import numpy as np

decoded_field_names = sorted(os.listdir(ex3.ex1_decoded_files))
MAX_ARRAY_LEN = 4016
TIME_STAMPS = 76


def filename_to_unix_time(
        filename: str
) -> int:
    return int(time.mktime(time.strptime(filename.split('.')[0], '%Y-%m-%d')))


def flat_data(

) -> np.ndarray:
    result: np.ndarray = np.nan * np.zeros(shape=(TIME_STAMPS, len(decoded_field_names), MAX_ARRAY_LEN))

    for field_column_idx, field_name in enumerate(decoded_field_names):
        filenames = os.listdir(f'{ex3.ex1_decoded_files}/{field_name}')
        filenames = sorted(
            filenames,
            key=filename_to_unix_time
        )

        for timestamp, filename in enumerate(filenames):
            try:
                arr: np.ndarray = np.load(f'{ex3.ex1_decoded_files}/{field_name}/{filename}')['arr_0']
            except ValueError:
                continue

            length = arr.shape[0]

            if length != MAX_ARRAY_LEN:
                arr = np.concatenate((arr, np.nan * np.zeros(shape=(MAX_ARRAY_LEN - length, ))), axis=0)

            result[timestamp][field_column_idx] = arr

    return result


if not os.path.isdir('dirs/ex4'):
    os.mkdir('dirs/ex4')


with open('dirs/ex4/flatted_data.npz', 'wb') as f:
    np.save(
        f,
        flat_data()
    )
