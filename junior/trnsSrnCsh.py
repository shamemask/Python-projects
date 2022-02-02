from asyncore import socket_map
import socket
import sys
import urllib.request
import os
import http.client

url = "https://github.com/shamemask/C-/blob/main/i.xml"

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(f"path is {path}")

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
print(conn.getresponse().read())
print(socket.gethostbyname(socket.gethostname()))

filename = url.split('/')[-1]
print(f"filename is {filename}")


urllib.request.urlretrieve(url, filename)
