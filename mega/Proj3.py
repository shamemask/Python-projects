# 3.            Напишите функцию, которая в зависимости от
# переданного в нее целочисленного аргумента, будет выводить
# слово «товар» в нужно форме(«12 товаров», но «22 товара»).

while True:
    count = input("Введите количество товара: ")
    if count.isdigit():
        count = int(count)
        product_count = str(count) + " товар"

        if count % 10 == 1 and count % 100 != 11:
            print(product_count)
        elif 1 < count % 10 < 5 and count % 100 != 12 and count % 100 != 13 and count % 100 != 14:
            print(product_count + "а")
        elif count >= 5:
            print(product_count + "ов")
