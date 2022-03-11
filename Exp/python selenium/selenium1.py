from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")
driver.get('https://mail.google.com/mail/b/ALGkd0z2h8ZSjyVpfAl7fhwJ745aquqCrHT5XO7KkvX12S7nMFOO/u/0/#inbox')
time.sleep(3)
email = driver.find_element_by_id('identifierId')
email.send_keys('vezde.svoe')

nextBtn = driver.find_element_by_id('identifierNext')
nextBtn.click()

time.sleep(2)
passwd = driver.find_element_by_name('password')
passwd.send_keys('Ty073kl!')


nextBtn = driver.find_element_by_id('passwordNext')
nextBtn.click()

print("Login completed!")
