def info(tank):
    return f'Facing:{tank.direction}, ' \
           f'Points:{tank.points}, '\
           f'Shots in directions:{[(key, value) for key, value in tank.shots.items()]}'

def end_game_info(tank):
    return f'Points:{tank.points}, Shots fired:{sum(tank.shots.values())}'
