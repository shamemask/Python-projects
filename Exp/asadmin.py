import socket
import os
import sys
import win32com.shell.shell as shell


ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(
        lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    # sys.exit(0)
with open("somefilename.txt", "w") as out:
    out.write("i am root")


ip = "10.100.24.28"
port = 80

# создаём сокет для подключения
sock = socket.socket()
sock.connect((ip, port))

# запрашиваем имя файла и отправляем серверу
f_name = 'somefilename.txt'  # input('File to send: ')
sock.send((bytes(f_name, encoding='UTF-8')))

# открываем файл в режиме байтового чтения
f = open(f_name, "rb")

# читаем строку
l = f.read(1024)

while (l):
    # отправляем строку на сервер
    sock.send(l)
    l = f.read(1024)

f.close()
sock.close()
