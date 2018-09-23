import os

def test_dir():
    print("os seprater: " + os.sep)

    #current dir
    cwd = os.getcwd()
    print("cwd: "+ cwd)

    #change dir
    os.chdir("../")
    cwd = os.getcwd()
    print("cwd: "+ cwd)

    #parent dir
    print("parent dir: " + os.path.dirname(cwd))
    # list dir , list ->str
    print("list dirs:" + ' '.join(os.listdir(cwd)))

    print(cwd + "is a dir: " + str(os.path.isdir(cwd)))
    print(" .gitignore is a dir: " + str(os.path.isdir('.gitignore')))

    os.chdir('hello')
    cwd = os.getcwd()
    print("-------------")
    for file in os.listdir(cwd):
        if file.endswith(".py"):
            print(file + " is a python file")
    print("-------------")

test_dir()


