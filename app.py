import os, os.path, shutil, zipfile
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile

path = ""

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
            valid = True
        elif startExtraction == "N":    #stop extraction
            input("Goodbye!")
            valid = True
        else:   #remove invalid inputs
            print("invalid input - type y or n")


def menu():
    print("WELCOME\n1 - Choose path\n2 - extract")
    usrInput = int(input("option : "))

    if usrInput == 1:
        chooseFolder()
    elif usrInput == 2:
        extraction()


menu()

input()