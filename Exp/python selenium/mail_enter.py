import imaplib
mail = imaplib.IMAP4_SSL(host='imap.gmail.com',port=993)
mail.login(user='vezde.svoe@gmail.com', password='Ty073kl!')
mail.list()
print(mail.list())
print("########################################")
# Выводит список папок в почтовом ящике.
mail.select("inbox") # Подключаемся к папке "входящие"

result, data = mail.search(None, "ALL")
with open("result.txt","w") as f1:
    f1.write(result)
    f1.write(str(data))
print(result, data)
print("########################################")
ids = data[0] # Получаем сроку номеров писем
with open("ids.txt","w") as f1:
    f1.write(str(ids))
print(ids)
print("########################################")
id_list = ids.split() # Разделяем ID писем
with open("id_list.txt","w") as f1:
    f1.write(str(id_list))
print(id_list)
print("########################################")
latest_email_id = id_list[-1] # Берем последний ID
with open("latest_email_id.txt","w") as f1:
    f1.write(str(latest_email_id))
print(latest_email_id)
print("########################################")
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем тело письма (RFC822) для данного ID
with open("result2.txt","w") as f1:
    f1.write(result)
    f1.write(str(data))
print(result, data)
print("########################################")
raw_email = data[0][1] # Тело письма в необработанном виде
with open("raw_email.txt","w") as f1:
    f1.write(str(raw_email))
# включает в себя заголовки и альтернативные полезные нагрузки
print(raw_email)
print("########################################")

import email
email_message = email.message_from_string(str(raw_email))
 
print (email_message['To'])
 
print( email.utils.parseaddr(email_message['From'])) # получаем имя отправителя "Yuji Tomita" 
 
print( email_message.items() )# Выводит все заголовки.
 
def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
