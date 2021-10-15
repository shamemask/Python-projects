# условия if
age = 12
print(age < 14)
if age < 14:
    print("Ты младше 14")
print(age > 14)
if age > 14:
    print("Ты старше 14")
print(age == 14)
if age == 14:
    print("Тебе 14 лет")

if age <= 14:
    print("Ты младше 14, либо тебе исполнилось 14 только в этом году")
if age >= 14:
    print("Ты старше 14, либо тебе исполнилось 14 только в этом году")
if age != 14:
    print("Тебе не 14")

if 7 <= age <= 17:
    print("Ты ходишь в школу")

# сравниваем строки
if "пять" == "пять":
    print("'пять' равно 'пять'")
# сравниваем символы
if "5" == "5":
    print("5 равно 5")
# сравниваем число и символ
if 5 == "5":
    print("Если ты видишь эту строчку, значит свершилось невозможное")

# проверяем существование подстроки в строке
things = "На столе лежат тетрадь и карандаш"
if "тетрадь" in things:
    print("Я нашел тетрадь")
if "ручка" not in things:
    print("А вот ручку не нашел")

# условие if-else
number = input("Введите число: ")
number = int(number)
if number % 2 == 0:
    print("Вы ввели четное число")
else:
    print("Вы ввели нечетное число")


# условие if-elif
temp = input("Какая сейчас температура воздуха? ")
temp = int(temp)
if temp <= 0:
    print("Очень холодно")
elif 0 < temp <= 12:
    print("Холодно")
elif 12 < temp <= 18:
    print("Прохладно")
elif 18 < temp <= 25:
    print("Тепло")
elif 25 < temp <= 32:
    print("Жарко")
elif temp > 32:
    print("Очень жарко")

# условие c and
money = True
seats = True
if money == True and seats == True:
    print("Ты можешь купить билет в кино")
else:
    print("Ты не можешь купить билет в кино")

# условие c or
age = 12
parents = False
if age >= 12 or parents == True:
    print("Ты можешь посмотреть кино")
else:
    print("Ты не можешь посмотреть кино")

# Д.З. определяем, к какому сезону относится месяц
month = input("Введите номер месяца: ")
if month == "1" or month == "2" or month == "12":
    print("Зимний месяц")
elif month == "3" or month == "4" or month == "5":
    print("Весенний месяц")
elif month == "6" or month == "7" or month == "8":
    print("Летний месяц")
elif month == "9" or month == "10" or month == "11":
    print("Осенний месяц")
else:
    print("Вы ввели неверный номер")