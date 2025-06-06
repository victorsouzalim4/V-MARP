import os

def get_files(dir):

    if not os.path.isfile(dir):
        files = os.listdir(dir)
        #print(files)

        for file in files:
            newDir = os.path.join(dir, file).replace("\\", "/")
            print(newDir)

            get_files(newDir)
        