import requests
datas = {
 'identifier':'def',
 'password':'def'
}
login = "vezde.svoe@gmail.com"
passwd = "Ty073kl!"
datas['identifier']  = login
datas['password'] = passwd
url = 'https://www.google.com/accounts?hl=RU'
s = requests.Session()
loging = s.post(url, data = datas)
f = open('result.txt','w+')
f.write(loging.text)
f.close()
