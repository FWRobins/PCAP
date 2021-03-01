import os

def find(thepath, thedir):
    paths = []
    os.chdir(thepath)

    for a,b,c in os.walk(os.getcwd()):
        index = a.rfind('\\')
        if a[index+1:] == 'python':
            paths.append(a)

    return print(paths)

find('.\\tree', 'python')
