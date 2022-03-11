import lxml
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

session = requests.Session()
auth = session.post('https://accounts.google.com/ServiceLogin?sacu=1&oauth=1&rip=1', data={'login':'vezde.svoe@gmail.com','password':'Ty073kl!'})
print(auth.status_code)
res = session.get('https://mail.google.com/mail/b/ALGkd0yYEipTERNGp5UCchNQw5tGy-e5635SZsHJW1a4Mg_xKVaA/u/0/feed/atom')
print(res.status_code)
print(res.url)



calls_df = pd.read_html("https://mail.google.com/mail/b/ALGkd0yYEipTERNGp5UCchNQw5tGy-e5635SZsHJW1a4Mg_xKVaA/u/0/feed/atom")

print(calls_df)
