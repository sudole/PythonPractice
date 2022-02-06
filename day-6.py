# Let's read the file and find the word you want

import os

def checkPath(path):
    path_type = "none"
    # File Path Check
    if (os.path.isfile(path)):
        path_type = "file"
    # Directory Path Check
    if (os.path.isdir(path)):
        path_type = "dir"
    return path_type

path = input("input path :: ")
print("path = ", path)
print(checkPath(path))