from sys import argv

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
        else:
            pass
    except IndexError:
        print("error: no file or parameter specified")