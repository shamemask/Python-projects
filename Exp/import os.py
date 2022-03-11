import os
import datetime

testpath = input('Введите адрес: ')

if os.path.exists(testpath):
    if os.path.isfile(testpath):
        print('ФАЙЛ')
        print('Размер:', os.path.getsize(testpath)//1024, 'Кб')
        print('Дата создания:',
              datetime.datetime.fromtimestamp(int(os.path.getctime(testpath))))
        print('Дата последнего открытия:',
              datetime.datetime.fromtimestamp(int(os.path.getatime(testpath))))
        print('Дата последнего изменения:',
              datetime.datetime.fromtimestamp(int(os.path.getmtime(testpath))))
    elif os.path.isdir(testpath):
        print('КАТАЛОГ')
        print('Список объектов в нем: ', os.listdir(testpath))
else:
    print('Объект не найден')
