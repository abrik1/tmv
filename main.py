from sys import argv

VERSION = float(0.1)

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
            pass
    except IndexError:
        print("error: no file or parameter specified")