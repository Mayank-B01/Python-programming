
from os.path import exists


def is_file(file_name):
    return exists(file_name)


print(is_file(input("Enter file name:")))
