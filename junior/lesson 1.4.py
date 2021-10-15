counter = 7
while counter > 0:
    print(counter, end="")
    counter = counter - 1
print()
counter = 10
while counter > 0:
    print(counter, end="")
    counter = counter - 2
print()

while True:
    print("Это бесконечный цикл")
    stop = input("Остановить цикл? (да/нет) ")
    if stop == "да":
        print("Цикл остановлен")
        break

counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)

word = "кукушка"
for char in word:
    print(char, end="")
print()

for i in range(5):
    print("Hello")
print()
for i in range(5):
    print(i, end="")
print()
for i in range(1,5):
    print(i, end="")
print()
#Д.З. считаем сумму чисел из ряда от 1 до 20, пример решения
sum = 0
for i in range(1,21):
    sum += i
print(f"Сумма чисел от 1 до 20 = {sum}")

#Д.З. считаем сумму нечетных чисел от 0 до 10, пример решения
sum = 0
counter = 0
while counter < 10:
    if counter % 2 == 1:
        sum += counter
    counter += 1
print(f"Сумма нечетных чисел от 0 до 10 = {sum}")

#Д.З. пока не получим bye
while True:
    answer = input("hello! ")
    if answer == "bye":
        print("bye")
        break
