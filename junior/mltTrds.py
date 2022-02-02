# coding=UTF-8
import ifaddr
import urllib.request
import urllib
import re
import time
import socket
import threading

# Завершить формат IP прокси
proxys = []
inFile = open('junior\proxy.txt', 'r')
# Создаем новый документ, в котором хранится действующий IP
proxy_ip = open('junior\proxy_ip.txt', 'w')

for line in inFile.readlines():
    line = line.strip('\n')
    # proxy_host = '://'.join(line.split('='))
    proxy_host = line.split('=')[1]
    # print(proxy_host)
    proxy_temp = {line.split("=")[0]: proxy_host}
    print(proxy_temp)
    proxys.append(proxy_temp)


lock = threading.Lock()  # Установить блокировку
# Проверяем действительность IP прокси


adapters = ifaddr.get_adapters()

for adapter in adapters:
    for ip in adapter.ips:
        if isinstance(ip.ip, str):
            print(ip.ip)


def test(i):
    socket.setdefaulttimeout(5)  # Установить глобальный тайм-аут
    # url = "http://quote.stockstar.com/stock" # URL для сканирования
    url = "http://www.baidu.com/"  # URL для сканирования

    try:
        proxy_support = urllib.request.ProxyHandler(proxys[i])
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [
            ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib.request.install_opener(opener)
        res = urllib.request.urlopen(url).read()

        # Получение блокировки для синхронизации потоков
        lock.acquire()  # Получить блокировку
        print(proxys[i], 'is OK')
        proxy_ip.write('% s \ n' % str(proxys[i]))  # Записываем IP прокси

        # Снимаем блокировку и запускаем следующий поток
        lock.release()  # release lock
    except Exception as e:
        lock.acquire()
        print(proxys[i], e)
        lock.release()


 # Однопоточная проверка
# '''for i in range(len(proxys)):
#     test(i)'''
 # Многопоточная проверка
threads = []
start = time.time()
for i in range(len(proxys)):
    thread = threading.Thread(target=test, args=[i])
    threads.append(thread)
    thread.start()
 # Заблокировать основной процесс и дождаться завершения всех дочерних потоков
for thread in threads:
    thread.join()

proxy_ip.close()  # Закрываем файл

end = time.time()
print("Время начала:% f s" % start)
print("Время окончания:% f s" % end)
print("Требуется много времени на проверку IP:% f s" % (end-start))
