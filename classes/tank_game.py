from functions.info import info, save_score, top
from functions.visual import draw_map
from constant.objective import Target, check_if_hit
from constant.tank import Tank


class TankGame:

    def __init__(self):
        self.tank = Tank()
        self.target = Target()
        self.menu = {
            1: self.tank.move_up,
            2: self.tank.move_down,
            3: self.tank.move_right,
            4: self.tank.move_left,
            5: self.tank.shoot,
            6: lambda: print(info(self.tank)),
            7: lambda: print(top()),
            8: lambda: save_score(self.tank)
        }

    def run(self):
        while self.tank.points > 0:
            draw_map(self.tank, self.target, 9)
            print(f'Facing: {self.tank.direction}')
            print('Menu:\n1.Up | 2.Down | 3.Right | 4.Left |'
                  '\n 5. Shoot | 6. Info | 7. Top 5 | 8. Exit')
            try:
                choice = int(input('Enter choice: '))
            except ValueError:
                print('Choose from the menu')
                continue
            action = self.menu.get(choice)
            action()
            if action is None:
                print('Choose from the menu')
                continue
            elif choice == 5:
                if check_if_hit(self.tank, self.target):
                    self.target.generate_new_location()
            elif choice == 8:
                break
        else:
            print(f'Game over\nShots fired: {self.tank.shots}, Score: {self.tank.points}')
            save_score(self.tank)
