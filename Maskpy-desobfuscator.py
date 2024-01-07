import sys, os

def restore(code, filename):
    code[-1] = code[-1].replace("exec", "print")
    code = "\n".join(code)
    f = open("temp.py", "w", encoding="utf-8")
    f.write(code)
    f.close()
    os.system("python3 temp.py > "+filename)
    os.system("rm temp.py")
    print("\033[1;32mSuccess:\033[0m the file has been successfully desobfuscated")


def gui():
    banner = """\033[92m
  __  __           _    _____       
 |  \/  |         | |  |  __ \      
 | \  / | __ _ ___| | _| |__) |   _ 
 | |\/| |/ _` / __| |/ /  ___/ | | |
 | |  | | (_| \__ \   <| |   | |_| |  was a 
 |_|  |_|\__,_|___/_|\_\_|    \__, |   joke ...
                               __/ |
                              |___/ """
    print(banner)
    filename = input("""\033[1;35mDrag the file to desobfuscate here : \033[0m""")
    if filename[0] == filename[-1]:
        if filename[0] == "'" or filename[0] == '"':
            filename = filename[1:-1]

    return filename

def open_file(filename):
    if filename[-3:] != ".py":
        print("\033[91mError: \033[0myou need to choose a python file!")
        sys.exit()
    try:
        f = open(filename, "r", encoding='utf-8')
        content = f.read()
        cuted_file = content.splitlines()
        return cuted_file 
    except:
        print("\033[91mError: \033[0mfile doesn't exist!")
        sys.exit()

if __name__ == "__main__":
    a = len(sys.argv)
    if a == 1:
        filename = gui()
        desobfuscated_filename = filename[:-3]+"_desobfuscated.py"        
    elif a == 2:
        filename = sys.argv[1]
        desobfuscated_filename = filename[:-3]+"_desobfuscated.py"
    elif a == 3:
        filename = sys.argv[1]
        desobfuscated_filename = sys.argv[2]
    else:
        print("Error: too many arguments")
        exit()
    restore(open_file(filename), desobfuscated_filename)
