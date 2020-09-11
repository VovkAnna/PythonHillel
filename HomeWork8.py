
import os
def directory_and_name (filename, folder_path):
    name = filename.rsplit("/", 1)[-1]
    path =folder_path.rsplit("/", 1)[0]
    print(name,path)

my_path = "./MyFiles/text.txt"

directory_and_name(my_path,my_path)
################################################################
def all_files(path_folder):
    name = os.listdir(path_folder)
    list_files=[]
    for str in name:
        if os.path.isfile(str):
            list_files.append(os.path.join(path,str))
    return(list_files)

def all_folders(path_folder):
    name = os.listdir(path_folder)
    list_folder =[]
    for str in name:
        if os.path.isdir(str):
            list_folder.append(os.path.join(path, str))
    return (list_folder)

path ="C:/Users/User/PycharmProjects/ANNApythonlessons"
print(all_files(path))
print(all_folders(path))

def dict_files_and_folders(path_folder):
    my_dict={"files":(all_files(path)),"folders":(all_folders(path))}
    return my_dict
print(dict_files_and_folders(path))
###############################################################
import os
def makes_fold_tmp (my_dir):
    my_list=os.listdir(my_dir)
    flag=True
    for names in my_list:
        if os.path.isdir(names):
            os.mkdir(f"{names}_tmp")
            flag =False
    if flag ==True:
        os.mkdir("tmp")
my_path = r"C:/Users/User/PycharmProjects/ANNApythonlessons"
makes_fold_tmp(my_path)
