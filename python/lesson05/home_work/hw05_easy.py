import os
import re
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def mkdirs():
    path = os.getcwd()
    t = 0
    for i in range(1, 10):
        dir_path = os.path.join(path, 'dir_' + str(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            t += 1
        else:
            t += 0
    if t == 0:
        return True
    else:
        return False


def rmdirs():
    path = os.getcwd()
    dirs = os.listdir(path)
    t = 0
    for dir in dirs:
        if dir.startswith('dir_'):
            shutil.rmtree(dir)
            t += 1
        else:
            pass
    if t > 0:
        return True, t
    else:
        return False


print(rmdirs())
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def lsall():
    files = os.listdir(os.getcwd())
    [print(file) for file in files]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copycurrentfile():
    filename = os.path.basename(__file__)
    shutil.copyfile(filename, filename + '_copy')
