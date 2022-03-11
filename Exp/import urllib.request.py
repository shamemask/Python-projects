import urllib.request
import urllib
import re
import time
import random
# 抓取代理IP
ip_totle = []  # 所有页面的内容列表
for page in range(2, 6):
    url = 'http://ip84.com/dlgn/'+str(page)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print('get page', page)
    pattern = re.compile('<td>(\d.*?)</td>')  # 截取<td>与</td>之间第一个数为数字的内容
    ip_page = re.findall(pattern, str(content))
    ip_totle.extend(ip_page)
    time.sleep(random.choice(range(1, 3)))
# 打印抓取内容
print('代理IP地址     ', '\t', '端口', '\t', '速度', '\t', '验证时间')
for i in range(0, len(ip_totle), 4):
    print(ip_totle[i], '    ', '\t', ip_totle[i+1],
          '\t', ip_totle[i+2], '\t', ip_totle[i+3])
复制代码
