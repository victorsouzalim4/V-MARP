import os
from datetime import datetime
from Utils.data_base_function import store_file_data

def map_authorized_files(current_path, output_file, indent, limit_date, env, batch_limit = 1000, batch = [], level = 0):
    is_authorized = False
    all_children_authorized = True

    if not os.path.isfile(current_path) and bool(os.listdir(current_path)):  # check if current_path is a file or an empty folder
        entries = os.listdir(current_path)

        for entry in entries:
            child_path = os.path.join(current_path, entry).replace("\\", "/")

            child_authorization = map_authorized_files(
                child_path, output_file, 
                indent = indent + "|________", 
                limit_date = limit_date,
                env = env,
                batch = batch,
                level = level + 1
            )

            if not child_authorization:
                all_children_authorized = False

        if all_children_authorized:
            is_authorized = True

    else:
        modification_time = os.path.getmtime(current_path)
        modification_date = datetime.fromtimestamp(modification_time).date()

        if modification_date < limit_date:
            is_authorized = True

    output_file.write(indent + current_path + " " + str(is_authorized) + '\n')
    print(is_authorized)

    batch.append((current_path, is_authorized))

    if len(batch) >= batch_limit:
        flush_batch(batch, env)

    if level == 0:
        flush_batch(batch, env)

    return is_authorized

def flush_batch(batch, env):
    with env.begin(write=True) as txn:
        for path_line, is_authorized in batch:
            store_file_data(
                txn = txn, 
                file_path = path_line.strip(), 
                file_authorization = is_authorized
            )
    batch.clear()

        