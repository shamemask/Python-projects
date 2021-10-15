print("Это программа расчета твоих сбережений.")

saved_roubles = input("Сколько ты уже накопил? ")
saved_roubles = int(saved_roubles)
added_roubles = input("Сколько ты планируешь откладывать каждый день? ")
added_roubles = int(added_roubles)
days = input("На какое количество дней будем делать расчет? ")
days = int(days)

print(f"У тебя уже есть {saved_roubles} рублей.")
print(f"Если ты каждый день будешь откладывать по {added_roubles} рублей, то за {days} дней...")
for i in range(days):
    saved_roubles = saved_roubles + added_roubles
    #print(f"День {i}, сумма -  {saved_roubles}")
print(f"... ты накопишь {saved_roubles} рублей!")

#считаем сколько дней надо накопить до цели
goal = input("А сколько ты хочешь накопить? ")
goal = int(goal)
saved_roubles = input("Сколько ты уже накопил? ")
saved_roubles = int(saved_roubles)
added_roubles = input("Сколько ты планируешь откладывать каждый день? ")
added_roubles = int(added_roubles)
days = 0
while goal > saved_roubles:
    saved_roubles = saved_roubles + added_roubles
    days = days + 1
    #print(f"День {days}, сумма -  {saved_roubles}")
print(f"Ты накопишь {goal} рублей за {days} дней")

