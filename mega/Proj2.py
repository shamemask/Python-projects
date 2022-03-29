# 2.            Дан файл text.txt в котором содержится произвольный текст.
# Необходимо написать:
# - решение, которое будет шифровать данный файл, создавая новый файл text_ encrypted.txt
# - решение которое будет расшифровывать файл и создавать новый расшифрованный файл text_ decrypted.txt
# Методы шифрования на ваше усмотрение. Текст до шифрования и после расшифровки должен быть одинаковым. В описании решения укажите какой метод шифрования используется.

from Crypto.Cipher import DES

key = b'megaphon'


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)
answer = 0
while answer != 1 and answer != 2:
    answer = int(
        input("Выберите действие:\n1. Зашифровать файл text.txt\n2. Расшифровать файл text_encrypted.txt\n"))

    if answer == 1:
        with open("text.txt", "rb") as file:
            text = file.read()
            #text = b'Python rocks!'

        padded_text = pad(text)

        encrypted_text = des.encrypt(padded_text)
        print(encrypted_text)
        with open("text_encrypted.txt", "wb") as file_en:
            file_en.write(encrypted_text)

    elif answer == 2:
        with open("text_encrypted.txt", "rb") as file_des:
            encrypted_text = file_des.read()
        data = des.decrypt(encrypted_text)
        print(data)
        with open("text_decrypted.txt", "wb") as file_dec:
            file_dec.write(data)
