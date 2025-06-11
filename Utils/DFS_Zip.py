import os
from datetime import datetime
import shutil
from Utils.data_base_function import get_file_authorization
from Utils.compress_path import compress_path

def zip_walk(current_path, limit_date, ):

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
        zip_path = current_path + ".zip"
        
        try:
            compress_path(current_path, zip_path = zip_path)
        except Exception as e:
            print(f"❌ Falha ao compactar {current_path}: {e}")
            return

        if os.path.exists(zip_path):
            print(f"✔ Compactado: {current_path} → {zip_path}")
            try:
                if os.path.isfile(current_path):
                    os.remove(current_path)
                elif os.path.isdir(current_path):
                    shutil.rmtree(current_path)
                print(f"🗑️  Original removido: {current_path}")
            except Exception as e:
                print(f"⚠️ Erro ao remover {current_path}: {e}")
        else:
            print(f"⚠️ Compactação falhou: {zip_path} não foi criado.")


        