import random
class Insects:

# 1. задаем атрибуты насекомого (имя, еда, чувство сытости)
    def __init__(self):
        pass

# 2. после еды увеличиваем/уменьшаем нужные атрибуты      
    def eat(self):
        pass

# 3. после поиска еды уменьшаем/увеличиваем нужные атрибуты
    def find_food(self):
        pass

# 4. унаследуем класс пчелы от класса насекомых
class Bee():
# 5. задаем атрибуты пчелы (количество меда, помимо остальных атрибутов)
    def __init__(self, name):
        pass

# 6. после сбора меда увеличиваем/уменьшаем нужные атрибуты
    def collecting_honey(self):
        pass
        
# 7. данный метод готов, нужно будет его запустить в самый последний момент и объяснить, как он работает
    def live(self):
        pass
#        living = True
#        if self.hunger <= 0:
#            print(f'{self.name} died :(')
#            living = False
#            return living
#        action = random.randint(1,3)
#        if self.hunger < 4:
#            if self.food == 0:
#                self.find_food()
#            else:
#                self.eat()
#        else:
#            if action == 1:
#                self.collecting_honey()
#            elif action == 2:
#                self.eat()
#            else:
#                self.find_food()

                
# 8. пчела живет 30 дней (если она погибает, то итерации заканчиваются)


