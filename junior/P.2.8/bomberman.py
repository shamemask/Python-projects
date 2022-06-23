'''
Цель урока: Настроить управление, добавить возможность установки бомбы и настроить ее взаимодействие с другими объектами.
- Повторение
- Проверка домашнего задания
- Настроить управление Бомбермэном
- Настроить взаимодействие Бомбермэна со стенами
- Создать бомбы
- Добавить огонь от бомбы
- Создать финал игры
- Добавить бонусы (дополнительное задание)
- Сделать выводы к уроку
- Получить домашнее задание

'''

import arcade
import random
import animate
import time


# задаем ширину, высоту и заголовок окна

SCREEN_TITLE = "Bomberman"
CELL_WIDTH = 60
CELL_HEIGHT = 60
ROW_COUNT = 11
COLUMN_COUNT = 11
SCREEN_WIDTH = CELL_WIDTH * COLUMN_COUNT
SCREEN_HEIGHT = CELL_HEIGHT * ROW_COUNT

PLAYER1_SPEED = 10
PLAYER2_SPEED = 10

PLAYER1_BOMB_COUNT = 1
PLAYER2_BOMB_COUNT = 1

PLAYER1_POWER = 3
PLAYER2_POWER = 3


def difference(coordinate, distance):
    return coordinate * distance + distance/2


def justify_x(position_x):
    for x in range(COLUMN_COUNT):
        cell_center_x = difference(x, CELL_WIDTH)
        if position_x - cell_center_x <= CELL_WIDTH / 2:
            return cell_center_x


def justify_y(position_y):
    for y in range(ROW_COUNT):
        cell_center_y = difference(y, CELL_HEIGHT)
        if position_y - cell_center_y <= CELL_HEIGHT / 2:
            return cell_center_y

def bonus_add(image_name, spritelist, block):
    bonus = Bonus(image_name, 1)
    bonus.center_x = block.center_x
    bonus.center_y = block.center_y
    spritelist.append(bonus)


class Bomb(animate.Animate):
    def __init__(self):
        super().__init__('Bomb/Bomb_f00.png',0.7)
        for i in range(3):
            self.append_texture(arcade.load_texture(f'Bomb/Bomb_f0{i}.png'))
        self.bomb_timer = time.time()
        self.power = 3

    def update(self):
        if time.time() - self.bomb_timer >3:
            exp = Explosion()
            exp.center_x = self.center_x
            exp.center_y = self.center_y
            window.explosions.append(exp)
            left = True
            right = True
            top = True
            bottom = True
            self.kill()
            for i in range(1,  self.power+1):
                if left:
                    exp1 = Explosion()
                    exp1.center_x = exp.center_x - CELL_WIDTH * i
                    exp1.center_y = exp.center_y
                    window.explosions.append(exp1)
                    if exp1.check():
                        left = False
                if right:
                    exp2 = Explosion()
                    exp2.center_x = exp.center_x + CELL_WIDTH * i
                    exp2.center_y = exp.center_y
                    window.explosions.append(exp2)
                    if exp2.check():
                        right = False
                if bottom:
                    exp3 = Explosion()
                    exp3.center_x = exp.center_x
                    exp3.center_y = exp.center_y - CELL_HEIGHT * i
                    window.explosions.append(exp3)
                    if exp3.check():
                        bottom = False
                if top:
                    exp4 = Explosion()
                    exp4.center_x = exp.center_x
                    exp4.center_y = exp.center_y + CELL_HEIGHT * i
                    window.explosions.append(exp4)
                    if exp4.check():
                        top = False







class Bomberman(animate.Animate):
    def __init__(self, speed, bomb_count, power):
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
        self.motion = 0
        self.speed = speed
        self.bomb_count = bomb_count
        self.power = power
        self.win = False

    def costume_change(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.bottom < 0:
            self.bottom = 0
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        self.collisions(window.solid_blocks)
        self.collisions(window.explodable_blocks)



    def to_up(self):
        if not self.motion:
            self.motion = 1
            self.direction = 3
            self.change_y = self.speed
    
    def to_down(self):
        if not self.motion:
            self.motion = 1
            self.direction = 4
            self.change_y = -self.speed

    def to_left(self):
        if not self.motion:
            self.motion = 1
            self.direction = 1
            self.change_x = -self.speed

    def to_right(self):
        if not self.motion:
            self.motion = 1
            self.direction = 2
            self.change_x = self.speed

    def to_stop(self):
        self.change_x = 0
        self.change_y = 0
        self.direction = 0
        self.motion = 0

    def collisions(self, spritelist):
        block_hit = arcade.check_for_collision_with_list(
        self, 
        spritelist
        )
        if len(block_hit) > 0:
            for block in block_hit:
                if self.direction == 3 and self.top >= block.bottom:
                    self.top = block.bottom
                elif self.direction == 4 and self.bottom <= block.top:
                    self.bottom = block.top
                elif self.direction == 2 and self.right >= block.left:
                    self.right = block.left
                elif self.direction == 1 and self.left <= block.right:
                    self.left = block.right
        bombs_up = arcade.check_for_collision_with_list(
            self,
            window.bomb_power_up
        )
        flame_up = arcade.check_for_collision_with_list(
            self,
            window.flame_power_up
        )
        speed_up = arcade.check_for_collision_with_list(
            self,
            window.speed_power_up
        )
        if len(bombs_up) > 0:
            self.bomb_count += 1
            for bonus in bombs_up:
                bonus.kill()
        if len(flame_up) > 0:
            self.power += 1
            for bonus in flame_up:
                bonus.kill()
        if len(speed_up) > 0:
            self.speed += 1
            for bonus in speed_up:
                bonus.kill()




class SolidBlock(arcade.Sprite):
    def __init__(self):
        super().__init__('Blocks/SolidBlock.png', 1)

class ExplodableBlock(arcade.Sprite):
    def __init__(self):
        super().__init__('Blocks/ExplodableBlock.png', 1)

class Bonus(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)


class Explosion(animate.Animate):
    def __init__(self):
        super().__init__('Flame/Flame_f00.png', 0.7)
        for i in range(5):
            self.append_texture(arcade.load_texture(f'Flame/Flame_f0{i}.png'))
        self.explosion_timer = time.time()

    def update(self):
        if time.time() - self.explosion_timer > 2:
            self.kill()

    def check(self):
        hits = arcade.check_for_collision_with_list(
            self,
            window.solid_blocks
        )
        return len(hits) > 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #текстуры
        self.bg = arcade.load_texture('Blocks/BackgroundTile.png')
        self.win1 = arcade.load_texture('win/win1.png')
        self.win2 = arcade.load_texture('win/win2.png')
        #спрайтлисты
        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks = arcade.SpriteList()
        self.bombs_player1 = arcade.SpriteList()
        self.bombs_player2 = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        self.bomb_power_up = arcade.SpriteList()
        self.flame_power_up = arcade.SpriteList()
        self.speed_power_up = arcade.SpriteList()
        #спрайты
        self.bomberman = Bomberman(PLAYER1_SPEED, PLAYER1_BOMB_COUNT, PLAYER1_POWER)
        self.bomberman2 = Bomberman(PLAYER2_SPEED, PLAYER2_BOMB_COUNT, PLAYER2_POWER)
        #поля
        self.game = True
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
                        bonus_place = random.randint(1, 6)
                        if bonus_place == 1:
                            bonus_add(
                                'Powerups/BombPowerup.png', 
                                self.bomb_power_up, 
                                exp_block
                            )
                        elif bonus_place == 2:
                            bonus_add(
                                'Powerups/SpeedPowerup.png', 
                                self.speed_power_up, 
                                exp_block
                            )
                        elif bonus_place == 3:
                            bonus_add(
                                'Powerups/FlamePowerup.png', 
                                self.flame_power_up, 
                                exp_block
                            )

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
        self.bomb_power_up.draw()
        self.flame_power_up.draw()
        self.speed_power_up.draw()
        self.explodable_blocks.draw()
        self.bombs_player1.draw()
        self.bombs_player2.draw()
        self.bomberman.draw()
        self.bomberman2.draw()
        self.explosions.draw()

        if self.bomberman.win:
            arcade.draw_texture_rectangle(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                self.win1
            )
            self.game = False
        if self.bomberman2.win:
            arcade.draw_texture_rectangle(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                self.win2
            )
            self.game = False


    def update(self, delta_time):
        if self.game:
            self.bomberman.update_animation(delta_time)
            self.bomberman2.update_animation(delta_time)
            self.bomberman.update()
            self.bomberman2.update()
            self.bombs_player1.update()
            self.bombs_player1.update_animation(delta_time)
            self.bombs_player2.update()
            self.bombs_player2.update_animation(delta_time)
            self.explosions.update()
            self.explosions.update_animation()
            for flame in self.explosions:
                explosions = arcade.check_for_collision_with_list(
                    flame, 
                    self.explodable_blocks)
                if len(explosions) > 0:
                    for block in explosions:
                        block.kill()
                hit_list = arcade.check_for_collision_with_list(
                        flame, 
                        self.solid_blocks)
                if len(hit_list) > 0:
                    flame.kill()
                if arcade.check_for_collision(flame, self.bomberman):
                    self.bomberman.color = (0,0,0)
                    self.bomberman2.win = True
                if arcade.check_for_collision(flame, self.bomberman2):
                    self.bomberman2.color = (0,0,0)
                    self.bomberman.win = True



        

    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.LEFT:
                self.bomberman.to_left()
            elif key == arcade.key.RIGHT:
                self.bomberman.to_right()
            elif key == arcade.key.UP:
                self.bomberman.to_up()
            elif key == arcade.key.DOWN:
                self.bomberman.to_down()
            self.bomberman.costume_change()            
            if key == arcade.key.SPACE:
                if len(self.bombs_player1) < self.bomberman.bomb_count:
                    bomb = Bomb()
                    bomb.center_x = justify_x(self.bomberman.center_x)
                    bomb.center_y = justify_y(self.bomberman.center_y)
                    bomb.power = self.bomberman.power
                    self.bombs_player1.append(bomb)

            if key == arcade.key.A:
                self.bomberman2.to_left()
            elif key == arcade.key.D:
                self.bomberman2.to_right()
            elif key == arcade.key.W:
                self.bomberman2.to_up()
            elif key == arcade.key.S:
                self.bomberman2.to_down()
            self.bomberman2.costume_change()
            if key == arcade.key.E:
                if len(self.bombs_player2) < self.bomberman2.bomb_count:
                    bomb = Bomb()
                    bomb.center_x = justify_x(self.bomberman2.center_x)
                    bomb.center_y = justify_y(self.bomberman2.center_y)
                    bomb.power = self.bomberman2.power
                    self.bombs_player2.append(bomb)




    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.DOWN:
            self.bomberman.to_stop()
        if key == arcade.key.A or key == arcade.key.D or key == arcade.key.W or key == arcade.key.S:
            self.bomberman2.to_stop()



window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
