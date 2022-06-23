import arcade  # подключаем необходимые библиотеки
import random
import time

SCREEN_WIDTH = 800  # создаем переменную для хранения ширины экрана
SCREEN_HEIGHT = 600  # создаем переменную для хранения высоты экрана

class Animate(arcade.Sprite):
    '''
        Это наш класс анимации, ты его хорошо знаешь.
    '''
    i = 0
    time = 0
    def update_animation(self, delta_time):
        self.time += delta_time
        if self.time >= 0.1:
            self.time = 0
            if self.i == len(self.textures)-1:
                self.i = 0
            else:
                self.i += 1
            self.set_texture(self.i)

class Chicken(Animate):  # создаем класс, который будет отвечать работу курочек
    def __init__(self):  # создаем метод инициализации для создания параметров для курицы
        super().__init__(f"chicken/chicken_0.png", 0.9)  # загружаем начальную текстуру для куриц, задаем ей размер в 90%
        self.frames = 4 # количество текстур куриц 4
        for i in range(self.frames): # пробегаемся по текстурам
            # ошибка 9: в текстуры курица загружается всегда нулевая картинка
            self.append_texture(arcade.load_texture(f"chicken/chicken_{i}.png")) # и добавляем текстуры в спрайт для последующей анимации

# ошибка 1: у класса волка не указан родитель - arcade.Sprite
class Wolf(arcade.Sprite):  # создаем класс, который будет отвечать работу волка
    def __init__(self):  # создаем метод инициализации для создания параметров для волка
        super().__init__("wolf_left_bottom.png", 0.9)  # загружаем начальную текстуру для волка, задаем ей размер в 90%
        self.left_dir = True  # логическая переменная: волк смотрит влево
        self.right_dir = False  # логическая переменная: волк смотрит вправо
        self.top_dir = False # логическая переменная: волк вверху
        self.bottom_dir = True# логическая переменная: волк внизу
        # ниже загружаем текстуры для всех четырех возможных положений волка
        # ошибка 2: перепутаны левые и правые текстуры волка
        self.left_top = arcade.load_texture("wolf_left_top.png")
        self.left_bottom = arcade.load_texture("wolf_left_bottom.png")
        self.right_top = arcade.load_texture("wolf_right_top.png")
        self.right_bottom = arcade.load_texture("wolf_right_bottom.png")

    def update(self):  # создаем метод, отвечающий за игровое поведение волка
        # ниже проверяем, в какой угол смотри волк: в правый верхний, правый нижний, левый верхний или левый нижний
        # после проверки меням текстуру волку на ту, что соответсвует его направлению
        if self.left_dir and self.bottom_dir:
            self.texture = self.left_bottom
        elif self.left_dir and self.top_dir:
            self.texture = self.left_top
        elif self.right_dir and self.bottom_dir:
            self.texture = self.right_bottom
        elif self.right_dir and self.top_dir:
            self.texture = self.right_top


class Egg(arcade.Sprite):  # создаем класс, который отвечает за создание яиц
    def __init__(self):  # создаем метод инициализации для создания параметров для всех яиц
        # ошибка 3: размер яиц очень маленький, надо 1.1
        super().__init__("egg.png", 1.1)  # загружаем начальную текстуру для яйца, задаем ей размер в 110%
        self.pos = 0  # переменная, которая будет отвечать за выбор положения яйца перед его появлением
        # (на какой из четырёх полок оно будет появляться)
        self.change_angle = 4  # задаем скорость изменения угла
        self.change_x = 0.5  # задаем скорость изменения горизонтального положения
        self.change_y = 0.2  # задаем скорость изменения вертикального положения
        self.missed = False  # переменная-датчик для отслеживания, было ли пропущено яйцо

    def setup(self):  # создаем метод для задания начальных значений
        # ошибка 5: яйца появляются только справа, так как рандом выбирает значение 3,4, нужно от 1 до 4
        self.pos = random.randint(1,4)  # рандомно выбираем одно из четырех положений
        # (1 - лев. ниж., 2 - лев. верх., 3 - пр. верх., 4 - пр. ниж.)
        if self.pos == 1: 
            self.center_x = 25   # начальные координаты для первого положения
            self.center_y = 290  # начальные координаты для первого положения
        elif self.pos == 2:
            self.center_x = 25   # начальные координаты для второго положения
            self.center_y = 470  # начальные координаты для второго положения
        elif self.pos == 3:
            self.center_x = 775  # начальные координаты для третьего положения
            self.center_y = 470  # начальные координаты для третьего положения
        elif self.pos == 4:
            self.center_x = 775  # начальные координаты для четвертого положения
            self.center_y = 290  # начальные координаты для четвертого положения

    def update(self):  # создаем метод для задания игрового поведения яиц
        if self.pos == 1 or self.pos == 2:  # если яйцо появилось слева, то вращаем его и постепенно смещаем вправо
            self.angle -= self.change_angle  # вращаем вправо
            self.center_x += self.change_x  # смещаем вправо
            if self.center_x > 210:  # усилием вертикальную тягу после точки x = 210, чтобы создать эффект падения
                self.change_y += 0.5
        elif self.pos == 3 or self.pos == 4:  # если яйцо появилось справа, то вращаем его и постепенно смещаем влево
            self.angle += self.change_angle  # вращаем влево
            self.center_x -= self.change_x  # смещаем влево
            if self.center_x < 590:  # усилием вертикальную тягу после точки x = 590, чтобы создать эффект падения
                self.change_y += 0.5
        # ошибка 4: яйца летят вверх, так как их center_y увеличивается, нужно его уменьшать
        self.center_y -= self.change_y  # даем общее равномерное падение вниз, чтобы яйца катились вних под небольшим
        # углом

        self.change_x += 0.02  # даем общую равномерную тягу по горизонтали, чтобы яйца скатывались с ускорением
        self.change_y += 0.015  # даем общую равномерную тягу по вертикали, чтобы яйца падали с ускорением

        if arcade.check_for_collision(self, window.wolf):  # проверяем наличие столкновения между волком и яйцами
            if self.pos == 1:  # если яйцо падает с лев. ниж. полки
                if window.wolf.left_dir and window.wolf.bottom_dir:  # и если волк держит корзину слева снизу
                    window.score += 1  # то засчитываем яйцо пойманным
                    self.kill()  # убираем модельку этого яйца с экрана
                elif not self.missed:  # в противном случае, если яйцо еще не считалась пропущенным
                    window.missed += 1  # прибавлем единицу к счетчику пропущенных яиц
                    # ошибка 6: одно упавшее яйцо забирает все сердечки, так как оно считается пропущенным на кадом кадре
                    # нужно выставлять переменную флаг пропущенного яйца в True, чтобы считать его пропущенным только 1 раз
                    self.missed = True  # запоминаем, что это яйцо уже было учтено как упавшее
            elif self.pos == 2:  # если яйцо падает с лев. верх. полки
                if window.wolf.left_dir and window.wolf.top_dir:  # и если волк держит корзину слева сверху
                    window.score += 1  # то засчитываем яйцо пойманным
                    self.kill()  # убираем модельку этого яйца с экрана
                elif not self.missed:  # в противном случае, если яйцо еще не считалась пропущенным
                    window.missed += 1  # прибавлем единицу к счетчику пропущенных яиц
                    # ошибка 6: одно упавшее яйцо забирает все сердечки, так как оно считается пропущенным на кадом кадре
                    # нужно выставлять переменную флаг пропущенного яйца в True, чтобы считать его пропущенным только 1 раз
                    self.missed = True  # запоминаем, что это яйцо уже было учтено как упавшее
            elif self.pos == 3:  # если яйцо падает с пр. верх. полки
                if window.wolf.right_dir and window.wolf.top_dir:  # и если волк держит корзину справа сверху
                    window.score += 1  # то засчитываем яйцо пойманным
                    self.kill()  # убираем модельку этого яйца с экрана
                elif not self.missed:  # в противном случае, если яйцо еще не считалась пропущенным
                    window.missed += 1  # прибавлем единицу к счетчику пропущенных яиц
                    # ошибка 6: одно упавшее яйцо забирает все сердечки, так как оно считается пропущенным на кадом кадре
                    # нужно выставлять переменную флаг пропущенного яйца в True, чтобы считать его пропущенным только 1 раз
                    self.missed = True  # запоминаем, что это яйцо уже было учтено как упавшее
            elif self.pos == 4:  # если яйцо падает с пр. ниж. полки
                if window.wolf.right_dir and window.wolf.bottom_dir:  # и если волк держит корзину справа снизу
                    window.score += 1  # то засчитываем яйцо пойманным
                    self.kill()  # убираем модельку этого яйца с экрана
                elif not self.missed:  # в противном случае, если яйцо еще не считалась пропущенным
                    window.missed += 1  # прибавлем единицу к счетчику пропущенных яиц
                    # ошибка 6: одно упавшее яйцо забирает все сердечки, так как оно считается пропущенным на кадом кадре
                    # нужно выставлять переменную флаг пропущенного яйца в True, чтобы считать его пропущенным только 1 раз
                    self.missed = True  # запоминаем, что это яйцо уже было учтено как упавшее

class Health(arcade.Sprite):    # Создание класса жизней
    def __init__(self):     # создание метода инициализации класса (конструктора)
        super().__init__("3_heart.png", 0.7) # загружаем начальную текстуру для жизни, задаем ей размер в 70%
        self.append_texture(arcade.load_texture("2_heart.png"))  # дополнительно загружаем текстуру с картинкой 2 сердечка
        self.append_texture(arcade.load_texture("1_heart.png"))  # дополнительно загружаем текстуру с картинкой 1 сердечек
        self.center_x = SCREEN_WIDTH/2 + 300  # аналогично, начальные координаты для полоски здоровья, здесь х
        self.top = SCREEN_HEIGHT - 5  # позиционируем верхний край спрайта с отступом в 5 пикселей от верхней границы окна
    
    def update(self):
        if window.missed == 1:  # если 1 пропущенное яйцо
            self.set_texture(1)  # то меняем текстуру полоски здоровья на 2 сердечка
        elif window.missed == 2:  # если 2 пропущенных
            self.set_texture(2)  # то меняем на 1 сердечко
        elif window.missed >= 3:  # если 3 пропущенных и больше (мало ли)
            self.kill()  # убираем полоску здоровья
            window.run = False  # "выключаем игру"


class MyWindow(arcade.Window):  # создаем класс для игрового окна
    def __init__(self):  # создаем метод инициализации для создания внутриигровых параметров
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Волк и яйца")  # создаем непосредственно окно размером 800х600 и с заголовком "Волк и яйца"
        self.bg = arcade.load_texture("bg.png")  # загружаем текстуру для заднего фона
        self.go = arcade.load_texture("go.jpg")  # загружаем текстуру для заднего фона
        self.lines = arcade.load_texture("lines.png")  # загружаем текстуру полок
        self.wolf = Wolf()  # создаем волка
        self.eggs = arcade.SpriteList()  # соаздаем список спрайтов для хранения всех объектов-яиц
        self.timer = time.time()  # запоминаем время запуска игры
        self.score = 0  # создаем переменную-счетчик для набранных очков
        self.missed = 0  # создаем перменную счетчик для пропущенных яиц
        self.health_bar = Health()  # создаем спрайт с текстурой в виде трех сердечек (количество жизней)
        self.run = True  # логическая переменная, если равна истине, то считается, что игра запущена
        self.chickens = arcade.SpriteList() # список для хранения спрайтов курочек
        self.setup()  # вызываем метод setup, чтобы у персонажей были выставлены начальные значения для координат и скоростей
        self.sound = arcade.load_sound("sound.mp3") # загружаем фоновую музыку
        # ошибка 10: не проигрывается фоновая музыка
        self.sound.play() # включаем фоновую музыку



    def setup(self):  # создаем метод для задания начальных значений
        self.wolf.center_x = SCREEN_WIDTH/2  # начальные координаты волка, в этой строчке х
        self.wolf.center_y = SCREEN_HEIGHT/2 - 150  # а в этой строчку его у
        # ошибка 8: видна одна курица, на самом деле все 4 курицы и одних и тех же координатах
        self.coords = [(25,290), (25,470),(775,470), (775, 290)] # координаты курочек
        for pos in self.coords: #перебираем список координат
            chicken = Chicken()   # создаем экземпляр класса
            x, y = pos  # разбираем координаты на переменные x и y
            chicken.center_x = x # располагаем курицу по горизонтали
            chicken.center_y = y # располагаем курицу по вертикали
            self.chickens.append(chicken) # добавляем курицу в спрайт-лист

    def on_draw(self):  # создаем метод отрисовки
        self.clear()
        if self.run:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)  # отрисовываем текстуру заднего фона на весь экран
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT/2, self.lines)  # отрисовываем текстуру полок лишь на полэкрана
            self.wolf.draw()  # рисуем волка
            self.eggs.draw()  # рисуем яйца
            # ошибка 7: не отрисовывается надпись о счете
            arcade.draw_text(f"Score: {self.score}", 50, SCREEN_HEIGHT - 55, (255,255,255), 45)  # отображаем надпись со счетом
            self.health_bar.draw()  # рисуем сердечки для обозначения оставшегося здоровья
            self.chickens.draw() # прорисовываем курочек 
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.go)
        

    def update(self, delta_time: float):  # создаем метод для задания игрового поведения и игровой логики
        if self.run:  # проверяем, запущена ли игра
            self.wolf.update()  # вызываем update волка
            self.eggs.update()  # вызываем update у яиц
            if time.time() - self.timer > 3:  # отмеряем 1 секунду с момента, записанного в self.timer
                egg = Egg()  # создаем яйцо
                egg.setup()  # располагаем яйцо на полке
                self.eggs.append(egg)  # добавляем яйцо в список яиц
                self.timer = time.time()  # обновляем таймер
                self.health_bar.update()
        self.chickens.update_animation(delta_time) # запускаем анимацию для курочек

    def on_key_press(self, symbol: int, modifiers: int):  # создаем метод для отслеживания нажатий на клавиатуре
        if symbol == arcade.key.RIGHT:  # если нажата стрелка вправо
            self.wolf.right_dir = True  # волк начинаем смотреть вправо
            self.wolf.left_dir = False  # а влево перестает
        elif symbol == arcade.key.LEFT:  # если нажата стрелка влево
            self.wolf.left_dir = True  # то волк смотрит влево
            self.wolf.right_dir = False  # а вправо перестает
        elif symbol == arcade.key.UP:  # если нажата стрелка вверх
            self.wolf.top_dir = True  # то волк смотрит вверх
            self.wolf.bottom_dir = False  # а вниз перестает
        elif symbol == arcade.key.DOWN:  # если нажата стрелка вниз
            self.wolf.bottom_dir = True  # то волк смотрит вниз
            self.wolf.top_dir = False  # а вверх перестает


window = MyWindow()  # создаем игрвое окно
arcade.run()  # поддерживаем игровое окно открытым
