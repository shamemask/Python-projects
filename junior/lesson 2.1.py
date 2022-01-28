import arcade

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > 600 or self.left < 0:
            self.change_x = -self.change_x

class Game(arcade.Window):
    def __init__(self, width, height, title) :
        super().__init__(width, height, title) 
        self.ball = Ball('junior/ball.png', 0.1)
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        self.ball.change_y = 3
        
    def on_draw(self):
        self.clear((255,255,255)) 
        self.ball.draw()
        
    def update(self, delta_time):
        self.ball.update()


window = Game(600, 600, 'Пинг-Понг') 
arcade.run()