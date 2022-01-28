'''
    Цель: доделать игру Пинг-понг, настроить управление и взаимодействие спрайтов.
    
    + проверить домашнее задание;
    + вспомнить команды прошлого урока; 
    - настроить управление ракеткой с клавиатуры;
    - определить, что произойдет, когда отпустишь клавишу;
    - установить пределы для ракетки; 
    - прописать, как мяч будет отбиваться; 
    - ввести подсчет очков; 
    - добавить проигрыш в игре; 
    - ввести переменную состояния игры;
    - добавить победу в игру;
    - сделать выводы по уроку; 
    - получить домашнее задание.

'''
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Пинг-Понг'

SPEED_X = 5
SPEED_Y = 3

class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x  = -self.change_x
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png",0.1)
        self.bar = Bar("bar.png",0.1)
        self.setup()
    
    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y
        self.bar.center_x = SCREEN_WIDTH/2

    def on_draw(self):
        self.clear((255,255,255))
        self.ball.draw()
        self.bar.draw()

    def update(self, delta_time):
        self.ball.update()
        self.bar.update()



window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()