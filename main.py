from sys import argv
from os.path import isfile

VERSION = float(0.1)

ANSI_CODES = [
    "\x1b[0m",
    "\x1b[31m",
    "\x1b[34m",
    "\x1b[33m"
]

def is_file_found(fpath: str):
    print(f"{ANSI_CODES[2]}note{ANSI_CODES[0]}: we are checking if file is found or not")
    if isfile(fpath) == True:
        if fpath[len(fpath)-1] == "d" and fpath[len(fpath)-2] == "m":
            print(f"{ANSI_CODES[3]}note{ANSI_CODES[0]}: showing preview")
        else:
            print(f"{ANSI_CODES[1]}error{ANSI_CODES[0]}: file is not a markdown") 
    else:
        raise FileNotFoundError
    
if __name__ == "__main__":
    try:
        if argv[1] == "-h" or "":
            print('''
            tmv: Terminal Markdown Viewer
            =============================
            usage:
            -h: show this menu
            tmv file.md: opens file.md  
            ''')
        elif argv[1] == "-v":
            print("tmv",VERSION)
        else:
            is_file_found(argv[1])
    except IndexError:
        print(f"error: no file or parameter specified")