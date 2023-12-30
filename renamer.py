import os

def rename_files(folder_path, new_prefix):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        new_filename = new_prefix + filename
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

# Example usage:
folder_path = "back_up/50cm/2500"
new_prefix = "normal_"
rename_files(folder_path, new_prefix)