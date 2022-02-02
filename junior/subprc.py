

import os
import subprocess

from threading import Thread

from numpy import empty


username = 'eapteka\\d.artamonov2'
password = 'Df4kq-poECW1'
file = 'C:\\Users\\dartamonov\\Documents\\Git\\Python\\Python\\junior\\subjects.txt'
ips = ["10.100.24.28", "172.16.7.151", "172.16.7.149", "172.16.7.111"]


def threaded_function(ip):
    try:
        os.system("chcp 1251 >nul")
        cmd = "chcp 1251 >nul && C:/Windows/System32/net.exe view \\\\"+ip
        result = subprocess.check_output(
            cmd, shell=True, text=True).encode('cp1251').decode('cp866')
        result = result.split('\n')
        if len(result) < 7:
            return
        print(result[7].split(' ')[0])

        row = 7
        begin = "chcp 1251 && NET USE \\\\"+ip
        while len(result) > row:
            if result[row].split(' ')[0] == 'Команда':
                return
            xcopy = "xcopy "+file+" \\\\"+ip+'\\' + \
                result[row].split(' ')[0]+" /i /e /h /y"
            end = "NET USE \\\\"+ip+" /DELETE"

            cmd = begin + " && " + xcopy  # + " && " + end
            print(cmd)

            try:

                net_copy = subprocess.check_output(
                    cmd, shell=True, text=True).encode('cp1251').decode('cp866')
                print(net_copy)
                return
            except subprocess.CalledProcessError:
                row += 1
                continue

    except subprocess.CalledProcessError:
        exit(1)


for ip in ips:
    thread = Thread(target=threaded_function, args=[ip])
    thread.start()
    thread.join()
