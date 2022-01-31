import sys
import urllib.request
import os


url = "https://akamainet.com/update/Service.SchCache.rtf"

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(f"path is {path}")

filename = url.split('/')[-1]
print(f"filename is {filename}")


urllib.request.urlretrieve(url, filename)
