from pathlib import Path
import shutil

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        if item.is_dir():
            print(f"{i+1}   :  [FOLDER] {item}")
        else:
            print(f"{i+1}   :  [FILE]   {item}")


def createfolder():
    readfileandfolder()
    try:
        name = input("Enter the name of the folder: ")
        p = Path(name)
        if not p.exists():
            p.mkdir(parents=True)  # parents=True creates parent folders if needed
            print("FOLDER CREATED SUCCESSFULLY")
        else:
            print("This folder already exists")
    except Exception as err:
        print(f"An error occurred: {err}")


def readfolder():
    try:
        readfileandfolder()
        name = input("Enter folder name to view its contents: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            print(f"\nContents of '{name}':")
            items = list(p.iterdir())
            if items:
                for i, item in enumerate(items, start=1):
                    if item.is_dir():
                        print(f"{i}. [FOLDER] {item.name}")
                    else:
                        print(f"{i}. [FILE]   {item.name}")
            else:
                print("Folder is empty")
        else:
            print("No such folder exists")
    except Exception as err:
        print(f"An error occurred: {err}")


def updatefolder():
    readfileandfolder()
    name = input("Enter the folder name you want to update: ")
    p = Path(name)
    try:
        if p.exists() and p.is_dir():
            print("Press 1 to rename the folder")
            print("Press 2 to move the folder")
            res = int(input("Enter your choice: "))
            
            if res == 1:
                name2 = input("Enter the new name: ")
                if name != name2:
                    p2 = Path(name2)
                    p.rename(p2)
                    print("Folder renamed successfully")
                else:
                    print("Same name! Please choose a different name")
            
            elif res == 2:
                destination = input("Enter destination path: ")
                dest_path = Path(destination)
                if dest_path.exists() and dest_path.is_dir():
                    new_location = dest_path / p.name
                    shutil.move(str(p), str(new_location))
                    print("Folder moved successfully")
                else:
                    print("Destination folder doesn't exist")
            else:
                print("Invalid response")
        else:
            print("Folder does not exist")
    except Exception as err:
        print(f"An error occurred: {err}")


def deletefolder():
    try:
        readfileandfolder()
        name = input("Enter the folder name you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
            if confirm.lower() == 'yes':
                shutil.rmtree(p)  # Deletes folder and all its contents
                print("Folder deleted successfully")
            else:
                print("Deletion cancelled")
        else:
            print("No such folder found")
    except Exception as err:
        print(f"An error occurred: {err}")


# Main menu
for i in range(1, 100):
    print("\n" + "="*40)
    print("FOLDER MANAGEMENT SYSTEM")
    print("="*40)
    print("Press 1 to CREATE a folder")
    print("Press 2 to READ/VIEW folder contents")
    print("Press 3 to UPDATE a folder")
    print("Press 4 to DELETE a folder")
    print("Press 5 to EXIT")
    print("="*40)
    
    check = int(input("Enter number for operation: "))
    
    if check == 1:
        createfolder()
    elif check == 2:
        readfolder()
    elif check == 3:
        updatefolder()
    elif check == 4:
        deletefolder()
    elif check == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid response! Please select from given numbers")