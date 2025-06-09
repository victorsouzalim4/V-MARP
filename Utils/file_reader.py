import os
from datetime import datetime

def get_files(dir, output_file, backspace, date):

    authorized = False
    verification_flag = True

    # check if dir is a file or an empty folder
    if not os.path.isfile(dir) and bool(os.listdir(dir)):  
        files = os.listdir(dir)

        for file in files:
            newDir = os.path.join(dir, file).replace("\\", "/")

            return_value = get_files(newDir, output_file, backspace=backspace+"|________", date= date)

            if not return_value:
                verification_flag = False

        if verification_flag:
            authorized = True
    else:
        mod_time = os.path.getmtime(dir)
        mod_date = datetime.fromtimestamp(mod_time).date()

        if mod_date < date:
            authorized = True

    output_file.write(backspace + dir + " " + str(authorized) + '\n')
    print(authorized)

    return authorized
        