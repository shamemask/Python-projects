
class Car:
    def __init__(self, speed, color):  # метод инициализации
        self.speed = speed  # присваиваем полученное значение свойству скорость
        self.color = color  # присваиваем полученное значение свойству цвет

    def beep(self):
        print("BEEEEEEP")

    def say_speed(self):
        print(f"Speed: {self.speed}")

    def say_color(self):
        print(f"Сolor: {self.color}")


porshe = Car(120, "black")
porshe.beep()
porshe.say_color()

bmw = Car(110, "red")
bmw.beep()
bmw.say_speed()


class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def say_name(self):

        print(f"My name is {self.name}")

    def say_age(self):

        print(f"I am {self.age} years old")

person1 = Person("Tom", 15)
person1.say_name()
person1.say_age()

person2 = Person("Mary", 13)
person2.say_name()
person2.say_age()


class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def beep(self):
        print("BEEEEEEP")

    def say_speed(self):
        print(f"Speed: {self.speed}")

    def say_color(self):
        print(f"Color: {self.color}")

class Car(Transport):

    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner
        self.wheels = 4

    def say_owner(self):
        print("Owner is " + self.owner)


porshe = Car(120, "black", "Vasya")
porshe.say_owner()
porshe.beep()

class Bus(Transport):

    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats
        self.wheels = 8

    def say_owner(self):
        print("No owner")

bus1 = Bus(60, "yellow", 36)
bus1.say_color()
bus1.say_owner()