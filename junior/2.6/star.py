'''
Цель: создать игру Star Wars и изучить новые методы обработки взаимодействия с мышью.
+ Повторить команды из прошлых уроков; 
+ Добавить фон; 
+ Добавить Сокол Тысячелетия; 
+ Настроить движение Сокола Тысячелетия; 
+ Создать класс Лазера; 
+ Научить Сокол Тысячелетия стрелять; 
+ Добавить врагов; 
+ Настроить попадание во врагов; 
+ Определить победу; 
+ Добавить метеорит; 
+ Сделать выводы к уроку; 
+ Получить домашнее задание. 
'''

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Star Wars"
LASER_SPEED = 5
ENEMY_SPEED = 1
ENEMY_DISTANCE = 50

class MillenniumFalcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH/2
        self.center_y = 100
    def update(self):
        self.center_x+=self.change_x

class Lazer (arcade.Sprite):
    def __init__(self):
        super().__init__('laser.png', 0.8)
        self.center_x = window.falcon.center_x
        self.bottom = window.falcon.top
        self.change_y = LASER_SPEED
        self.laser_sound = arcade.load_sound('laser.wav')
    
    def update(self):
        self.center_y+=self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()

class TieFighter(arcade.Sprite):
    def __init__(self):
        super().__init__('TieFighter.png', 0.2)
        self.change_y = ENEMY_SPEED
    
    def update(self):
        self.center_y -= self.change_y
        if self.center_y < 0:
            self.kill()
            window.fails+=1

class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__('meteorit.png', 0.5)
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*3)
        self.change_y = ENEMY_SPEED + LASER_SPEED
    
    def update(self):
        self.center_y-=self.change_y
        if self.top < 0:
            self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT * 3)




class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('background.jpg')
        self.falcon = MillenniumFalcon()
        self.set_mouse_visible(False)
        self.lasers = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.setup()
        self.game = True
        self.win = arcade.load_texture('win.png')
        self.meteor = Meteor()
        self.fails = 0
        self.lost = arcade.load_texture('lost.jpg')
        self.sound = arcade.load_sound('A New Hope.mp3')
        arcade.play_sound(self.sound, 0.05)



    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:
            if button == arcade.MOUSE_BUTTON_LEFT:
                laser = Lazer()
                self.lasers.append(laser)
                arcade.play_sound(sound=laser.laser_sound, volume=1)
    
    def on_mouse_motion(self, x, y, dx, dy):
        if self.game:
            self.falcon.center_x = x
        
    
    def setup(self):
        for i in range(20):
            tie_fighter = TieFighter()
            tie_fighter.center_x = random.randint(0, SCREEN_WIDTH)
            tie_fighter.center_y = SCREEN_HEIGHT + i * ENEMY_DISTANCE
            self.enemies.append(tie_fighter)
        

    
    def on_draw(self):
        self.background_color = (255,255,255)
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.falcon.draw()
        self.lasers.draw()
        self.enemies.draw()
        if len(self.enemies) == 0:
            self.game = False
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win)
        self.meteor.draw()
        if self.fails > 3:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.lost)



    def update(self, delta_time):
        if self.game:
            self.falcon.update()
            self.lasers.update()
            self.enemies.update()
            for laser in self.lasers:
                hit_list = arcade.check_for_collision_with_list(laser, self.enemies)
                if hit_list:
                    laser.kill()
                    for enemy in hit_list:
                        enemy.kill()
            self.meteor.update()
            if arcade.check_for_collision(self.meteor, self.falcon):
                self.game = False
            dead_end = arcade.check_for_collision_with_list(self.falcon, self.enemies)
            if dead_end or self.fails > 3:
                self.game = False
                self.fails = 5





window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()