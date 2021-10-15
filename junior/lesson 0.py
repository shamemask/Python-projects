#print(5)
#print(5 + 5)
#print("hello world")
#print("hello world" + "from Vasya")
#name = "Вася"
#print("Меня зовут " + name)
#user_name = input("Введите Ваше имя")
#print("Привет" + user_name)

import random

secret_number = random.randint(1,10)

print("Компьютер загадал число от 1 до 10. Попробуйте его угадать.")
attempts = 3

while attempts > 0:
    print("Количество попыток: "+ str(attempts))
    user_number = input("Введите число: ")
   # print("Вы ввели: "+user_number)
    user_number = int(user_number)

    if secret_number > user_number:
        print("Секретное число больше")
    if secret_number < user_number:
        print("Секретное число меньше")
    if secret_number == user_number:
        print("Вы угадали")
        break

    attempts = attempts - 1
    if attempts == 0:
        print("Вы проиграли")
        print("Секретное число: " + str(secret_number))

