from ftplib import FTP

# ftp = FTP()

HOST = '10.100.24.28'
HOST1 = '172.16.7.132'
PORT = '80'
username = 'eapteka\d.artamonov2'
password = 'Df4kq-poECW1'
# ftp.connect(HOST, username, password)
ftp = FTP(HOST)
ftp.login()
data = ftp.retrlines('LIST')

print(data)
