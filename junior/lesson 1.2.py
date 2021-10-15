
# повторяем строковые переменные
city = "Санкт-Петербург"
print(city + " - очень красивый город")

#повторяем целочисленные переменные
current_year = 2020
print("Сейчас "+str(current_year)+" год")

birth_year = input("В каком году ты родился? ")
birth_year = int(birth_year)
age = current_year-birth_year
print("В этом году тебе исполняется " + str(age))
print("В 2035 году тебе исполнится " + str(2035-birth_year))

# повторяем логические переменные
boolean = 5 > 3
print("Первый результат:"+str(boolean))
boolean = 6 < 1
print("Второй результат: "+str(boolean))

#тренируемся писать f-строки
print(f"Я хочу посетить {city} в следующем году")
print(f"Я хочу посетить {city} в {current_year-1} году")
