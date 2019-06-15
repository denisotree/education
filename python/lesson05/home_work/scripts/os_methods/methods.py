import os
import shutil


def scd(path):
    try:
        os.chdir(path)
    except OSError:
        return False
    else:
        return True


def ls_all():
    files = os.listdir(os.getcwd())
    return files


def mkdir(dirname):
    path = os.getcwd()
    dir_path = os.path.join(path, dirname)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        return False
    else:
        return True


def rmdir(dirname):
    path = os.getcwd()
    dirs = os.listdir(path)
    t = 0
    for dir in dirs:
        if dir == dirname:
            shutil.rmtree(dir)
            t += 1
        else:
            pass
    if t > 0:
        return True
    else:
        return False
