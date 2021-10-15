name = input("Как тебя зовут? ")
print("Привет, " + name + ". Время поиграть в поле чудес!")
print("Так, начнем...")

word = "алгоритм"
letters = []
attempts = 3

while attempts > 0:
    failed = 0
    letter = input("Назови букву: ")

    letters.append(letter)

    for char in word:
        if char in letters:
            print(char, end=" ")
        else:
            print("*", end=" ")
            failed = failed + 1

    if failed == 0:
        print()
        print("Ты победил!")

        break

    print()

    if letter not in word:
        attempts = attempts - 1
        print("Неправильно")
        print("У тебя осталось " + str(attempts) + " попыток")

        if attempts == 0:
            print("Ты проиграл :-(")
