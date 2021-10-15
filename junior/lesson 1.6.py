import random

def say_hello():
    print("Hello")

say_hello()
say_hello()

def say_hello(name):
    print(f"Hello, {name}")

say_hello("Vasya")
say_hello("Fedya")
say_hello("Petya")

def area_square(side):
    area = side * side
    print(f"Площадь квадрата со стороной {side} = {area}")

area_square(5)
area_square(7)

def area_rectangle(side_a, side_b):
    area = side_a * side_b
    print(f"Площадь прямоугольника со сторонами {side_a} и  {side_b} = {area}")

area_rectangle(2, 4)
area_rectangle(4, 6)

def lottery():
    tickets = [13, 54, 23, 1, 5, 3]
    ticket = random.choice(tickets)
    return ticket


winner = lottery()
print(f"Выигрышный билет - {winner}")

def multi_lottery():
    tickets = [13, 54, 23, 1, 5, 3]
    ticket1 = random.choice(tickets)
    tickets.remove(ticket1)
    ticket2 = random.choice(tickets)
    return ticket1, ticket2


first_winner, second_winner = multi_lottery()
print(f"Выигрышные билеты - {first_winner} и {second_winner}")


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for i in range(1,11):
    print(f"Факториал {i} = {factorial(i)}")

sum = lambda a: a * a
print(sum(2))
print(sum(5))
sum = lambda a,b: a * b
print(sum(2,4))


# Д.З. нахождение наименьшего числа из трех
def min_number(a, b, c):
    min = 0
    if a <= b and a <= c:
        min = a
    if b <= a and b <= c:
        min = b
    if c <= a and c <= b:
        min = c
    return min

print(f"Наименьшее из трех чисел- {min_number(2,4,9)}")

# Д.З. площадь круга
def area_circle(r):
    S = 3.14*r*r
    return S

print(f"Площадь круга - {area_circle(2)}")