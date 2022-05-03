import random
class Insects:

    def __init__(self, name):
        self.name = name
        self.food = 3
        self.hunger = 2
        
    def eat(self):
        if self.food>0:
            self.hunger += 1
            self.food -= 1
            print(f'{self.name} has eaten, hunger = {self.hunger}, food = {self.food}')
        else:
            print(f'{self.name} has not eaten, no food, hunger = {self.hunger},  food = {self.food}')

    def find_food(self):
        self.food += 4
        self.hunger -= 1
        print(f'{self.name} has found food, hunger = {self.hunger}, food = {self.food}')

class Bee(Insects):

    def __init__(self, name):
        super().__init__(name)
        self.honey = 5

    def collecting_honey(self):
        self.honey += 2
        self.hunger -=2
        print(f'{self.name} has collected honey, hunger = {self.hunger}, food = {self.food}, honey = {self.honey}')
        
    def live(self):
        living = True
        if self.hunger <= 0:
            print(f'{self.name} died :(')
            living = False
            return living
        action = random.randint(1,3)
        if self.hunger < 4:
            if self.food == 0:
                self.find_food()
            else:
                self.eat()
        else:
            if action == 1:
                self.collecting_honey()
            elif action == 2:
                self.eat()
            else:
                self.find_food()

                
bee = Bee(name = 'Ms. Bee')

for day in range(1,30):
    print(f'day {day}')
    if bee.live() == False:
        break
