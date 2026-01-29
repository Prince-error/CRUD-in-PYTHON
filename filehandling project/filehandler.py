from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}   :  {items}")


def createfile():
    readfileandfolder()
    try:
        name=input("Enter the name of the file :-")
        p=Path(name)
        if not p.exists():

            with open(p,"w") as fs:
                data=input("what you want to write :-")
                fs.write(data)
            print("FILE CREATED SUCCESFULLY")
        else:
            print("this file already exists") 
    except Exception as err:
        print(f"an error is ocured as {err}")
     

def readfile():
    try:
        readfileandfolder()
        name=input("Input name of the file you want to read  :-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
                print(f"file readed succesfully")
        else:
             print("no such file exists")        
    except Exception as err:
         print(f"an error is occured as {err}")

def updatefile():
    readfileandfolder()
    name=input("Enter the file name you want to update:-")
    p=Path(name)
    try:
        if p.exists and p.is_file:
            print("press 1 for rename the file")
            print("press 2 for overwrite  the file")
            print("press 3 for append the file")
            res=int(input("tell your response :-"))
            if res==1:
                    name2=input("enter the name of the file:-")
                    if name!=name2:
                        p2=Path(name2)
                        p.rename(p2)
                        print("File rename succesfully")
                    else:
                         print("please select the different name")    
            elif res==2:
                    data=input("enter your data this will overwrite your file:-")
                    with open(p,"w") as fs:
                        fs.write(data)
                        print("file overwritten succesfully")
            elif res==3:
                    data=input("enter your data this will add at last:-")
                    with open(p,"a") as fs:
                        fs.write(f"\n{data}")
                        print("file appended succesfully")
            else:
                    print("invaild response") 
        else:
            print("file does not exists")               
    except Exception as err:
        print(f"An error is occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name=input("enter the name of the file you want to delete:-")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("file deleted succesfully")
        else:
            print("no such file found")
    except Exception as err:
         print(f"an error is occured as {err}")


for i in range(1,100):
    print(f"press 1 for creating  a file")
    print(f"press 2 for reading   a file")
    print(f"press 3 for updating  a file")
    print(f"press 4 for deleting  a file")
    print(f"press 5 for end")
    check=int(input("Enter number for operation "))
    if check==1:
        createfile()
    elif check==2:
        readfile()
    elif check==3:
        updatefile()
    elif check==4:
        deletefile()
    elif check==5:
        break
    else:
         print("invalid response please select from given number")