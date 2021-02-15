import os, subprocess, time, random

def hello_world():
    string = '''
Hello, World!
This is my first program using Python!
And hope to make more soon!
    '''
    return string

def print_no_newline(*args):
    for arg in args:
        print(arg, end=" ")

def clearPycache(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if "__pycache__" in dir:
                os.remove(dir)
                return True
            else:
                return False

def install_modules(*args):
    for module in args:
        command = f"python -m pip install {module}"
        subprocess.run(command)

def py_utils_help():
    base = 'This command gives you a list of all available functions and classes.'
    mainString = '''update this'''
    print(base)
    time.sleep(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    return mainString