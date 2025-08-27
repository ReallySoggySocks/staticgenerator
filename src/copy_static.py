import os
import shutil

def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
    else:
        os.mkdir(destination)

    source_list = os.listdir(source)

    for item in source_list:
        new_source = os.path.join(source, item)
        new_destination = os.path.join(destination, item)

        if os.path.isfile(new_source):
            shutil.copy(new_source, new_destination)
        else:
            copy_static(new_source, new_destination)

    return