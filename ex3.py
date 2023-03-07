import os
import pickle
from datetime import datetime
import ex1
import shutil


ex1_decoded_files = 'ex1_decoded'


def find_file_names_transform(

) -> dict:
    # 110 (hint from part 2) == 6
    with open('dirs/ex3/6/6.pkl', 'rb') as f:
        data: dict = pickle.load(f)

    result = {
        field_name: {} for field_name in os.listdir('dirs/ex1')
    }

    for field_name, decoding_data in data.items():
        field_name: str = field_name
        decoding_data: dict = decoding_data

        for filename in os.listdir(f'dirs/ex1/{field_name}'):
            file_id = int(filename.split('.')[0].split('_')[1])
            unix_timestamp = decoding_data[file_id] + int(filename.split('.')[0].split('_')[0])
            date = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d')

            result[field_name].update({
                filename: f'{date}.npz'
            })

    return result


def transform_filenames(

) -> None:
    if not os.path.isdir(ex1_decoded_files):
        os.mkdir(ex1_decoded_files)

    filenames_transform = find_file_names_transform()

    for encoded_field_name in os.listdir('dirs/ex1/'):
        decoded_field_name = ex1.revert(encoded_field_name)
        decoded_field_name_folder = f'{ex1_decoded_files}/{decoded_field_name}'

        if not os.path.isdir(decoded_field_name_folder):
            os.mkdir(decoded_field_name_folder)

        for encoded_filename in os.listdir(f'dirs/ex1/{encoded_field_name}'):
            decoded_filename = filenames_transform[encoded_field_name][encoded_filename]
            shutil.copyfile(
                src=f'dirs/ex1/{encoded_field_name}/{encoded_filename}',
                dst=f'{ex1_decoded_files}/{decoded_field_name}/{decoded_filename}'
            )


def post_process(

) -> None:
    def join_fields(
            src_dir: str,
            dst_dir: str
    ) -> None:
        for filename in os.listdir(src_dir):
            shutil.move(
                src=f'{src_dir}/{filename}',
                dst=f'{dst_dir}/{filename}'
            )

        os.rmdir(src_dir)

    join_fields(
        src_dir=f'{ex1_decoded_files}/Case-Fatality_Ratio',
        dst_dir=f'{ex1_decoded_files}/Case_Fatality_Ratio'
    )
    join_fields(
        src_dir=f'{ex1_decoded_files}/Incidence_Rate',
        dst_dir=f'{ex1_decoded_files}/Incident_Rate'
    )


transform_filenames()
post_process()

# print([len(str(v)) for v in combined_data.values().values()])



