deals = ["помыть посуду", "вынести мусор", "сделать уроки", "позаниматься программированием"]
print(deals)

print(deals[0])
print(deals[1])
print(deals[2])
print(deals[3])

deals[1] = "поиграть в игры"
print(deals)

deals.append("почитать книгу")
print(deals)

deals.remove("помыть посуду")
print(deals)

deal = deals.pop()
print(deals)
print(f"Я выполнил дело : {deal}")

deal_num = deals.index("сделать уроки")
deal = deals.pop(deal_num)
print(deals)
print(f"Я выполнил дело : {deal}")

books = ["Гарри Поттер", "Властелин Колец", "Дядя Федор, пёс и кот"]

for book in books:
    print(book)

length = len(books)
print("Список книг: ")
for i in range(length):
    print(f"{i+1}. {books[i]}")

if "Гарри Поттер" in books:
    print("Конечно же я читал Гарри Поттера")

books.append("Война и мир")
if "Война и мир" not in books:
    print("Я еще не читал Войну и мир")
else:
    print("Я уже прочел Войну и мир. Я молодец")

book = input("Какую книгу хотим добавить? ")
if book in books:
    print(f"Книга {book} уже есть в списке")
else:
    books.append(book)
    print(f"Книга {book} добавлена с список")
