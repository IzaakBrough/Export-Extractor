import os, os.path, shutil, zipfile
from exif import Image
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile

path = "undefined"

def chooseFolder():
    searching = True
    folder = input("Input folder:   ")

    while searching:
        if os.path.exists(folder) == True: #check valid path 
            print("Added!")
            searching = False
        else:
            print("invalid path")
            folder = input("Input folder:   ")
    return folder

def extraction():
    global path
    if path == "undefined":
        print("No path defined")
        path = chooseFolder()
    files = [f for f in listdir(path) if isfile(join(path, f))] #gets all files in a folder

    #listing the files in the folder
    for file in files:
        print(file)

    valid = False
    while valid == False:
        startExtraction = input("you have "+str(len(files))+" files to be extracted    continue(y/n) :").upper()    #user validation

        if startExtraction == "Y":
            for file in files:
                extract = path +"\\"+ file  #file path to extract
                print(file+"    extracting...")
                with zipfile.ZipFile(extract, 'r') as zip_ref:  #extraction process
                    zip_ref.extractall(path)
                print("Done!")
            print("\nExtraction complete!")
            
            src_path = join(path, "Takeout\Google Photos")
            shutil.move(src_path, path) #puts extraction in a nice format
            valid = True

        elif startExtraction == "N":    #stop extraction
            input("Goodbye!")
            valid = True
            
        else:   #remove invalid inputs
            print("invalid input - type y or n")
    menu()

def moveJson():
    global path
    if path == "undefined":
        print("No path defined")
        path = chooseFolder()
    path=path+"\\Google Photos"
    files = os.listdir(path)
    paths = [path]
    for file in files: #find subfolders
        filename,extension = os.path.splitext(file)
        extension = extension [1:]
        if extension == '':
            paths.append(file)
    for f in paths:
        if f != path:
            tempPath = path+'/'+f
        else:
            tempPath = path
        files = os.listdir(tempPath)
        for file in files:
            filename,extension = os.path.splitext(file)
            extension = extension [1:]
            if extension == 'json':
                if os.path.exists(tempPath+'/'+extension):
                    shutil.move(tempPath+'/'+file, tempPath+'/'+extension+'/'+file)

                else:   # makes a json directory if not already there
                    os.makedirs(tempPath+'/'+extension)
                    shutil.move(tempPath+'/'+file, tempPath+'/'+extension+'/'+file)               
    print("moved json files")
    menu()

def info():
    print("Put all the Google Photos export .zip's in a folder and copy the path into the terminal")
    usrRating = int(input("Rate 0-5  "))
    stars = [[" |"],["R|"],["A|"],["T|"],["E|"],[" |"]]
    star = [["    ,    "],[" __/ \__ "],[" \     / "],[" /_   _\\ "],["   \ /   "],["    '    "]]
    rows = range(6)
    for i in range(0,usrRating):
        for row in rows:
            stars[row][0] = stars[row][0]+star[row][0]
    for row in rows:
        print(stars[row][0])
    menu()

def menu():
    global path
    print(r" _____                       _               ")
    print(r"| ____|_  ___ __   ___  _ __| |_             ")
    print(r"|  _| \ \/ / '_ \ / _ \| '__| __|            ")
    print(r"| |___ >  <| |_) | (_) | |  | |_             ")
    print(r"|_____/_/\_\ .__/ \___/|_|   \__|            ")
    print(r" _____     |_|                 _             ")
    print(r"| ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __ ")
    print(r"|  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|")
    print(r"| |___ >  <| |_| | | (_| | (__| || (_) | |   ")
    print(r"|_____/_/\_\\__|_|  \__,_|\___|\__\___/|_|   ")
    print("For Google Photos export zip's\n")
    print(" 1 - Choose path\n 2 - extract\n 3 - move json files\n 4 - info\n-1 - exit")
    print("Path: ",path)
    usrInput = int(input("option : "))

    if usrInput == 1:
        path = chooseFolder()
        menu()
    elif usrInput == 2:
        extraction()
    elif usrInput == 3:
        moveJson()
    elif usrInput == 4:
        info()
    elif usrInput == -1:
        return()

menu()

input("\nend")