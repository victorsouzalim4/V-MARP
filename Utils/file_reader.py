import os

def get_files(dir, output_file, backspace):

    if not os.path.isfile(dir):
        files = os.listdir(dir)
        #print(files)

        for file in files:
            newDir = os.path.join(dir, file).replace("\\", "/")
            output_file.write(backspace + newDir + '\n')

            get_files(newDir, output_file, backspace=backspace+"|________")
        