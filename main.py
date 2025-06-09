from Utils.file_reader import get_files
from datetime import datetime

dir = 'C:/Users/Valle/OneDrive/Documentos/Neural_Networks/Neural_Networks'
output_file = 'output.txt'

date = datetime.strptime("2025-06-09", "%Y-%m-%d").date()

with open(output_file, "w", encoding="utf-8") as f:
    get_files(dir=dir, output_file=f, backspace="", date=date)
