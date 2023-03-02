from dataclasses import dataclass
import random
from functions.logger import Logger


@dataclass
class Target: 
    x = random.randrange(1, 9)
    y = random.randrange(1, 9)
    logger = Logger().get_logger()

    def generate_new_location(self):
        self.x = random.randrange(1, 9)
        self.y = random.randrange(1, 9)


def check_if_hit(tank, target):
    if tank.x == target.x and abs(tank.y - target.y) <= 2:
        if tank.y > target.y:
            if tank.direction == 'S':
                tank.points += 50
                return True
        if tank.y < target.y:
            if tank.direction == 'N':
                tank.points += 50
                return True
    elif tank.y == target.y and abs(tank.x - target.x) <= 2:
        if tank.x > target.x:
            if tank.direction == 'W':
                tank.points += 50
                return True
        if tank.x < target.x:
            if tank.direction == 'E':
                tank.points += 50
                return True
    else:
        tank.points -= 50
        return False
