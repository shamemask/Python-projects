'''
Цель: создать игру Динозаврик с цикличным движением и анимированными спрайтами.
+ вспомнить команды из прошлых уроков;
+ познакомиться с правилами игры, создать шаблон программы;
+ добавить фон;
+ добавить анимированного динозавра;
+ научить динозавра прыжку;
+ добавить кактус;
+ настроить движение кактуса;
+ настроить столкновение спрайтов;
- отрисовать фон о конце игры;
- сделать выводы по уроку;
- получить домашнее задание.
'''
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Динозаврик"
GRAVITATION = 0.5
DINO_HEIGHT = 12
CACTUS_SPEED = 5

class Animate(arcade.Sprite):
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

class Cactus(Animate):
    score = 0
    def update(self):
        self.center_x -= self.change_x
        if self.right < 0:
            self.left = SCREEN_WIDTH + random.randint(0, SCREEN_WIDTH)
            self.score += 1

class Dino(Animate):
    jump = False
    def update(self):
        self.center_y += self.change_y
        self.change_y -= GRAVITATION
        if self.center_y < 200:
            self.center_y = 200
            self.jump = False
            
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('images/bg.png')
        self.dino = Dino("images/dino1.png",0.5)
        self.cactus = Cactus("images/cactus1.png",0.5)
        self.game = True
        self.game_over = arcade.load_texture('images/game_over.png')
        self.win_bg = arcade.load_texture('images/win.png')
        self.win = False

         

    def setup(self):
        self.dino.center_x = 200
        self.dino.center_y = 200
        self.cactus.center_x = SCREEN_WIDTH
        self.cactus.center_y = 200
        self.dino.append_texture(arcade.load_texture("images/dino2.png"))
        self.dino.append_texture(arcade.load_texture("images/dino3.png"))
        self.cactus.append_texture(arcade.load_texture("images/cactus2.png"))
        self.cactus.change_x = CACTUS_SPEED

    def on_key_press (self, key, modifiers):
        if self.game:
            if key == arcade.key.SPACE and not self.dino.jump:
                self.dino.change_y = DINO_HEIGHT
                self.dino.jump = True

    def on_draw(self):
        self.clear()
        if self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        elif self.win:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win_bg)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.game_over)

        self.dino.draw()
        self.cactus.draw()
        arcade.draw_text(f'Счет:{self.cactus.score}', SCREEN_WIDTH - 120, SCREEN_HEIGHT - 40, (255,255,255), font_size=20)

    def update(self, delta_time):
        if self.game:
            self.dino.update_animation(delta_time)
            self.cactus.update_animation(delta_time)
            self.dino.update()
            self.cactus.update()
            if arcade.check_for_collision(self.dino, self.cactus):
                self.game = False
            if self.cactus.score >= 10:
                self.win = True
                self.game = False

        


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
