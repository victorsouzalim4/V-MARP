import os
from datetime import datetime
from Utils.data_base_function import get_file_authorization
from Utils.compress_path import compress_path

def zip_walk(current_path, limit_date):

    if not get_file_authorization(db_path = "file_mapping.lmdb", file_path = current_path):
        if not os.path.isfile(current_path):  # check if current_path is a file or an empty folder
            entries = os.listdir(current_path)

            for entry in entries:
                child_path = os.path.join(current_path, entry).replace("\\", "/")

                zip_walk(
                    child_path, 
                    limit_date = limit_date
                )
    else:
        compress_path(current_path, current_path + ".zip")
        print(f"✔ Compactado: {current_path}")


        