
class Tank:

    def __init__(self):
        self.x, self.y, self.direction = 5, 5, 'N'
        self.shots = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
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
        if self.direction == 'N':
            self.y += 1
            self.check_y()
        self.direction = 'N'

    def move_down(self):
        self.points -= 5
        if self.direction == 'S':
            self.y -= 1
            self.check_y()
        else:
            self.direction = 'S'

    def move_left(self):
        self.points -= 5
        if self.direction == 'W':
            self.x += 1
            self.check_x()
        else:
            self.direction = 'W'

    def move_right(self):
        self.points -= 5
        if self.direction == 'E':
            self.x -= 1
            self.check_y()
        self.direction = 'E'

    def shoot(self):
        self.shots[self.direction] += 1
