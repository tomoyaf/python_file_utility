import os
import re

def remove_current_dir_prefix_from_path(path):
    return path[:2].replace("./", "") + path[2:]

def read_all_files_absolute_path(root):
    paths = []
    for obj in os.listdir(root):
        path = root + "/" + obj
        if os.path.isfile(path):
            file_path = re.sub("/+", "/", path)
            paths.append(os.path.abspath(file_path))
        elif os.path.isdir(path):
            childs = read_all_files_absolute_path(path + "/")
            paths.extend(childs)
    return paths

def read_all_files_relative_path(root, current_dir_relative_path = "./"):
    paths = []
    current_dir_path = root + "/" + remove_current_dir_prefix_from_path(current_dir_relative_path)
    for obj in os.listdir(current_dir_path):
        if os.path.isfile(current_dir_path + obj):
            file_path = re.sub("/+", "/", current_dir_relative_path + obj)
            paths.append(file_path)
        elif os.path.isdir(current_dir_path + obj):
            child_dir_relative_path = current_dir_relative_path + "/" + obj + "/"
            childs = read_all_files_relative_path(root, child_dir_relative_path)
            paths.extend(childs)
    return paths

def read_child_files_name(root):
    files = []
    for obj in os.listdir(root):
        if os.path.isfile(root + "/" + obj):
            files.append(obj)
    return files

def read_child_dirs_name(root):
    dirs = []
    for obj in os.listdir(root):
        if os.path.isdir(root + "/" + obj):
            dirs.append(obj)
    return dirs

def read_child_files_and_dirs_name(root):
    return read_child_dirs_name(root) + read_child_files_name(root)

def is_file_extension(file_name, ext):
    return file_name.lower().endswith(ext)

if __name__ == "__main__":
    files = read_child_files_and_dirs_name("./file_utility")
    
    print(files)

