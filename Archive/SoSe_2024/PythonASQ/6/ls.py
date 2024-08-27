import sys
import os

def inputError():
    print("Usage: python ls.py [-sort] [-folder] [-dir path]")
    sys.exit(1)

path = os.getcwd()
sort = False
folder = False
args = sys.argv[1:]

if "-help" in args:
    print("Usage: python ls.py [-sort] [-folder] [-dir path]")
    print("-sort: Sorts the files and folders by date instead of alphabetically")
    print("-folder: Only shows folders")
    print("-dir path: Shows the files and folders in the specified directory (current directory if omitted)")
    sys.exit(0)
    
i = 0
while i < len(args):
    current = args[i]
    if current == "-sort":
        sort = True
    elif current == "-folder":
        folder = True
    elif current == "-dir":
        if i+1 >= len(args):
            inputError()
        path = args[i+1]
        i += 1
    else:
        inputError()
    i += 1

os.chdir(path)
files = os.listdir()
if sort:
    files.sort(key=lambda x: os.path.getmtime(x))
if folder:
    files = [f for f in files if os.path.isdir(f)]
for f in files:
    print(f)