
class Tank:

    def __init__(self):
        self.x, self.y, self.direction = 5, 5, 'UP'
        self.shots = {'UP': 0, 'RIGHT': 0, 'DOWN': 0, 'LEFT': 0}
        self.points = 100

    def check_x(self):
        if self.x > 9:
            self.x = 1
        elif self.x < 1:
            self.x = 9

    def check_y(self):
        if self.y > 9:
            self.y = 1
        elif self.y < 1:
            self.y = 9

    def move_up(self):
        self.points -= 5
        if self.direction == 'UP':
            self.y += 1
            self.check_y()
        self.direction = 'UP'

    def move_down(self):
        self.points -= 5
        if self.direction == 'DOWN':
            self.y -= 1
            self.check_y()
        else:
            self.direction = 'DOWN'

    def move_left(self):
        self.points -= 5
        if self.direction == 'RIGHT':
            self.x += 1
            self.check_x()
        else:
            self.direction = 'RIGHT'

    def move_right(self):
        self.points -= 5
        if self.direction == 'RIGHT':
            self.x -= 1
            self.check_y()
        self.direction = 'LEFT'

    def shoot(self):
        self.shots[self.direction] += 1
