'''
    + Повторить прошлые уроки
    + Познакомиться с правилами
    + Загрузить фон
    + Добавить твердые блоки
    + Добавить разрушаемые блоки
    + Создать главного героя
    + Сделать выводы к уроку
    + Получить домашнее задание
'''

import arcade
import random
import animate

# задаем ширину, высоту и заголовок окна

SCREEN_TITLE = "Bomberman"
CELL_WIDTH = 60
CELL_HEIGHT = 60
ROW_COUNT = 11
COLUMN_COUNT = 11
SCREEN_WIDTH = CELL_WIDTH * COLUMN_COUNT
SCREEN_HEIGHT = CELL_HEIGHT * ROW_COUNT

def difference(coordinate, distance):
    return coordinate * distance + distance/2

class Bomberman(animate.Animate):
    def __init__(self):
        super().__init__("Bomberman/Front/Bman_F_f00.png",0.5)
        # Front
        self.walk_down_frames = []
        for i in range(8):
            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png"))
        # Back
        self.walk_up_frames = []
        for i in range(8):
            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))
        # Right
        self.walk_right_frames = []
        for i in range(8):
            self.walk_right_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png"))
        # Left
        self.walk_left_frames = []
        for i in range(8):
            self.walk_left_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", 
            flipped_horizontally = True)
            )
        self.direction = 4

    def costume_change(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames


class SolidBlock(arcade.Sprite):
    def __init__(self):
        super().__init__('Blocks/SolidBlock.png', 1)

class ExplodableBlock(arcade.Sprite):
    def __init__(self):
        super().__init__('Blocks/ExplodableBlock.png', 1)

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #текстуры
        self.bg = arcade.load_texture('Blocks/BackgroundTile.png')
        #спрайтлисты
        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks = arcade.SpriteList()
        #спрайты
        self.bomberman = Bomberman()
        self.bomberman2 = Bomberman()
        #инициализация спрайтов
        self.setup()

    def setup(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                if x % 2 == 1 and y % 2 == 1:
                    solid_block = SolidBlock()
                    solid_block.center_x = difference(x, CELL_WIDTH)
                    solid_block.center_y = difference(y, CELL_HEIGHT)
                    self.solid_blocks.append(solid_block)
                elif random.randint(1, 2) == 1:
                    if (not (x == 0 and y <= 2)
                    and not (y == 0 and x <= 2)
                    and not (x == ROW_COUNT - 1 and y >= COLUMN_COUNT - 3)
                    and not (y == COLUMN_COUNT - 1 and x >= ROW_COUNT - 3)):
                        exp_block = ExplodableBlock()
                        exp_block.center_x = difference(x, CELL_WIDTH)
                        exp_block.center_y = difference(y, CELL_WIDTH)
                        self.explodable_blocks.append(exp_block)
        x = SCREEN_WIDTH / COLUMN_COUNT - CELL_WIDTH / 2
        y = SCREEN_HEIGHT / ROW_COUNT - CELL_HEIGHT / 2
        self.bomberman.set_position(x, y)
        x2 = SCREEN_HEIGHT - CELL_HEIGHT / 2
        y2 = SCREEN_WIDTH - CELL_WIDTH / 2
        self.bomberman2.set_position(x2, y2)
        self.bomberman2.color = (255,0,0)





    def draw_background(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                arcade.draw_texture_rectangle(
                   difference(x, CELL_WIDTH),
                    difference(y, CELL_WIDTH), 
                    CELL_WIDTH, CELL_HEIGHT, self.bg
                )


    def on_draw(self):
        self.clear()
        self.draw_background()
        self.solid_blocks.draw()
        self.explodable_blocks.draw()
        self.bomberman.draw()
        self.bomberman2.draw()

    def update(self, delta_time):
        self.bomberman.update_animation(delta_time)
        self.bomberman2.update_animation(delta_time)
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bomberman.direction = 1
        elif key == arcade.key.RIGHT:
            self.bomberman.direction = 2
        elif key == arcade.key.UP:
            self.bomberman.direction = 3
        elif key == arcade.key.DOWN:
            self.bomberman.direction = 4
        self.bomberman.costume_change()
        self.bomberman2.costume_change()

    def on_key_release(self, key, modifiers):
        pass

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
