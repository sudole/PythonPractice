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

def readFile(path):
    content = ''
    f = open(path, "r", encoding="utf-8")
    while True:
        line = f.readline()
        if not line: break
        content += line
    f.close()
    return content

def start():
    path = input("input path :: ")
    # print("path = ", path)
    path_type = checkPath(path)
    # print(path_type)

    if (path_type == "file"):
        content = readFile(path)
        # print(content)

start()