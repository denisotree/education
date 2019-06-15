import os
import sys
import shutil
import re
# print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    elif not new_name:
        print("Необходимо указать имя копии файла третьим параметром")
        return
    try:
        shutil.copyfile(file_name, new_name)
        print('Файл {} успешно скопирован'.format(file_name))
    except FileExistsError:
        print('Файл {} не существует'.format(file_name))


def rm_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path = os.getcwd()
    files = os.listdir(path)
    n = 0
    for file in files:
        asw = ''
        if file == file_name:
            full_file_name = os.path.join(path, file)
            while asw != 'n':
                asw = input('Вы точно хотите удалить файл {} (y/n): '.format(file))
                if asw == 'y':
                    try:
                        os.remove(full_file_name)
                        print('Файл {} успешно удален'.format(file))
                        n += 1
                        return
                    except FileNotFoundError:
                        print('Такого файла не существует')
                else:
                    print('Нужно выбрать y или n')
        else:
            pass
    if n == 0:
        print('Такого файла не существует')


def ls():
    files = os.listdir(os.getcwd())
    [print(file) for file in files]


def cd():
    if not dir_name:
        print("Необходимо указать относительный или абсолютный путь вторым параметром")
        return
    regex_windows = r'(^[A-Z]{1}:[\\]+)'
    regex_linux = r'(^[/+])'
    full_path = os.getcwd()
    if re.match(regex_linux, dir_name) or re.match(regex_windows, dir_name):
        try:
            os.chdir(dir_name)
            print('Новая директория {}'.format(os.getcwd()))
        except OSError:
            print('Вы ввели неверный путь')
    else:
        new_full_path = os.path.join(full_path, dir_name)
        try:
            os.chdir(new_full_path)
            print('Новая директория {}'.format(os.getcwd()))
        except OSError:
            print('Вы ввели неверный путь')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm_file": rm_file,
    "ls": ls,
    "cd": cd
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    new_name = sys.argv[3]
except IndexError:
    new_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
