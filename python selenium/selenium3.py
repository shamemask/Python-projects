##email.send_keys('vezde.svoe')
##passwd.send_keys('Ty073kl!')

##driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
import time
import smtplib
from html.parser import HTMLParser
####
class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data
f = HTMLFilter()
####
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('vezde.svoe@gmail.com','Ty073kl!')
####
options = {}
chrome_options = ChromeOptions()
#chrome_options.add_argument('--user-data-dir=hash')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless")
browser = Chrome(seleniumwire_options=options, options=chrome_options)

browser.get('https://gmail.com')
browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys('vezde.svoe')
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Ty073kl!')
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()


time.sleep(1)
#browser.find_element_by_xpath("//div[@class='gb_Eb gb_Ib']/div[1]/a[@class='gb_Lb']").click()
#browser.get('https://mail.google.com/mail/b/ALGkd0yQGJhh7HEeCoG9MPuwH6cnlZXvwePNa0Ybv0Z9559itGcM/u/0/#inbox')
#browser.find_element_by_id(":2i").click()
#y = browser.find_element_by_xpath('//*[@id=":2g"]/tbody/tr')

while True:
    try:
        print(browser.find_element_by_class_name('bqe').find_element_by_xpath('..').text)#'//*[@class="bqe"]'))
        if browser.find_elements_by_class_name('bqe')[0]:
        
            #if browser.find_element_by_xpath('//*[@class="bqe"]'):
            browser.find_element_by_class_name('bqe').find_element_by_xpath('..').click()# захват всех непрочитанных, можно открывать всегда первый
            mail = browser.find_element_by_xpath('//*[@class="gs"]').text + "\n"
            #mail += browser.find_element_by_xpath('//*[@class="ho"]').text + "\n"
            m3 = browser.find_elements_by_xpath('//*[@class="aZo N5jrZb"]')
            for n in m3:
                mail += str(n.firstChild().get('data-tooltip')) + "\t" + str(n.firstChild().get('href').text) + "\n"
                
            print(mail)
            
            smtpObj.sendmail("vezde.svoe@gmail.com","vezde.svoe@gmail.com",mail.encode('utf8'))
            browser.find_element_by_xpath('//*[@class="TO aBP nZ aiq" ]').click() #возврат к входящим
            #window.open(document.querySelectorAll("[class='aZo N5jrZb']")[1].firstElementChild.href,'_blank')# открыть ссылку в отдельном окне, выбрано 2е вложение
            #document.querySelectorAll("[class='aZo N5jrZb']").forEach((value) =>{window.open(value.firstElementChild.href,'_blank')})#скачает все вложения одновременно
            #browser.send_keys('{} {}')
    finally:
        time.sleep(5)








