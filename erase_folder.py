import os
import shutil

def erase_folder(from_folder):    
    for filename in os.listdir(from_folder):
        file_path = os.path.join(from_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
