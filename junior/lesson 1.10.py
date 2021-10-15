with open("languages.txt") as file:
    print(file.read())

with open("languages.txt") as file:
    for line in file:
        print(f"Мой любимый язык программирования: {line}")

with open("blank.txt", "w") as file:
    file.write("Совсем новый текст")

with open("blank.txt", "a") as file:
    file.write("\nПросто добавим текст")

with open("blank.txt") as file:
    print(file.read())

with open("languages.txt", "a") as file:
    file.write("\nPascal")

with open("languages.txt") as file:
    print(file.read())