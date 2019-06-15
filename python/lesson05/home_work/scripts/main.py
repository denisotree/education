# coding utf-8

import os_methods


######################################################################################################
#  Интерфейс
######################################################################################################

while True:
    print(
         'Программа умеет:\n'
         '[1] Переходить в директорию\n'
         '[2] Показывать содержимое текущей директории\n'
         '[3] Создавать директорию\n'
         '[4] Удалять директорию')
    answer = input('Введите номер функции или нажмите [q] для выхода из программы: ')
    if answer == 'q':
        break
    elif not answer.isdigit():
        print('Вы ввели неверную команду')
    elif int(answer) == 1:
        cd_dirname = input('Введите название директории: ')
        if os_methods.scd(cd_dirname):
            print('Мы успешно перешли в директорию')
            input()
        else:
            print('Не удалось перейти в директорию')
            input()
    elif int(answer) == 2:
        list_files = os_methods.ls_all()
        [print(file) for file in list_files]
        input()
    elif int(answer) == 3:
        mk_dirname = input('Введите название директории: ')
        if os_methods.mkdir(mk_dirname):
            print('Мы успешно создали в директорию ', mk_dirname)
            input()
        else:
            print('Не удалось создать в директорию ', mk_dirname, ', так как она уже существует')
            input()
    elif int(answer) == 4:
        rm_dirname = input('Введите название директории: ')
        if os_methods.rmdir(rm_dirname):
            print('Мы успешно удалили в директорию ', rm_dirname)
            input()
        else:
            print('Не удалось удалить в директорию ', rm_dirname, ', так как такой не существует')
            input()
    else:
        pass
