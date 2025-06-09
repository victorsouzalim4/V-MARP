import os
from datetime import datetime

def get_files(dir, output_file, backspace, date):

    authorized = False

    if not os.path.isfile(dir):
        files = os.listdir(dir)
        #print(files)

        for file in files:
            newDir = os.path.join(dir, file).replace("\\", "/")
            output_file.write(backspace + newDir + '\n')

            authorized = get_files(newDir, output_file, backspace=backspace+"|________", date= date)
    else:
        mod_time = os.path.getmtime(dir)
        mod_date = datetime.fromtimestamp(mod_time).date()

        if mod_date < date:
            authorized = True

    print(authorized)
    return authorized
        