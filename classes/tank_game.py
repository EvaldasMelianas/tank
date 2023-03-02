from functions.info import info, end_game_info
from functions.visual import draw_map
from constant.objective import Target, check_if_hit


class TankGame:

    def __init__(self, tank):
        self.tank = tank
        self.target = Target()
        self.menu = {
            1: self.tank.move_up,
            2: self.tank.move_down,
            3: self.tank.move_left,
            4: self.tank.move_right,
            5: self.tank.shoot,
            6: print(info(self.tank)),
            7: print(f'Game Over\n{end_game_info(self.tank)}')
        }

    def run(self):
        while self.tank.points > 0:
            draw_map(self.tank, self.target, 9)
            print(f'Facing: {self.tank.direction}, Targe:{self.target.x, self.target.y}')
            print('Menu:\n1.Move/Turn North | 2.Move/Turn South | 3.Move/Turn East\n'
                  '4.Move/Turn west | 5. Shoot | 6. Info\n7. Exit')
            try:
                choice = int(input('Enter choice: '))
            except ValueError:
                print('Choose from the menu')
                continue
            action = self.menu.get(choice)
            if choice == 5:
                if check_if_hit(self.tank, self.target):
                    self.target.generate_new_location()
            action()
            if choice == 7:
                break
            print('\n'*5)
        else:
            print(f'Game over\n{end_game_info(self.tank)}')
