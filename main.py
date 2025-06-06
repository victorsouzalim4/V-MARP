from Utils.file_reader import get_files

dir = 'C:/Users/Valle/OneDrive/Documentos/Neural_Networks/Neural_Networks'
output_file = 'output.txt'

with open(output_file, "w", encoding="utf-8") as f:
    get_files(dir=dir, output_file=f, backspace="")
