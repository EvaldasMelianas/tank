class Tank:

    def __init__(self):
        self.x = 5
        self.y = 5
        self.direction = 'N'
        self.shots = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        self.points = 100

    def up(self):
        self.points -= 5
        self.direction = 'N'
        self.y += 1
        if self.y > 9:
            self.y = 0

    def down(self):
        self.points -= 5
        self.direction = 'S'
        self.y -= 1
        if self.y < 0:
            self.y = 9

    def left(self):
        self.points -= 5
        self.direction = 'W'
        self.x -= 1
        if self.x < 0:
            self.x = 9

    def right(self):
        self.points -= 5
        self.direction = 'E'
        self.x += 1
        if self.x > 9:
            self.x = 0

    def shoot(self):
        self.shots[self.direction] += 1
