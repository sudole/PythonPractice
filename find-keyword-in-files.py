# Let's read the file and find the word you want

from inspect import getfile
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

def getFileList(path):
    file_list = os.listdir(path)
    return file_list

def findKeywordInContent(keyword, content):
    #print("Find Keyword: ", keyword)
    if keyword in content:
        return True
    else:
        return False

def start():
    path = input("input path :: ")
    # print("path = ", path)
    path_type = checkPath(path)
    # print(path_type)
    keyword = input("keyword :: ")

    if (path_type == "file"):
        content = readFile(path)
        # print(content)
        if (findKeywordInContent(keyword, content)):
            print("Find keyword! in ( ", path, ") ")

    if (path_type == "dir"):
        dir_list = getFileList(path)
        for item_path in dir_list:
            if (checkPath(item_path) == "file"):
                #print(item_path)
                content = readFile(item_path)
                #print(content)
                if (findKeywordInContent(keyword, content)):
                    print("Find keyword! (",keyword ,") in ( ", item_path, ") ")
            #else:
            #    print("directory pass (", item_path, ")")

start()