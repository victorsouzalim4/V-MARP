from Utils.tree_scanner import map_authorized_files
from Utils.DFS_Zip import zip_walk
from Utils.data_base_function import store_file_data, get_file_authorization
from datetime import datetime

dir = 'C:/Users/Valle/OneDrive/Documentos/Neural_Networks/Neural_Networks'
output_file = 'output.txt'

date = datetime.strptime("2025-06-09", "%Y-%m-%d").date()


with open(output_file, "w", encoding="utf-8") as f:
    map_authorized_files(
        current_path = dir, 
        output_file=f, indent = "",
        limit_date = date
    )

zip_walk(current_path = dir, limit_date = date)
