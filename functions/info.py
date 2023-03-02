def info(tank):
           f'Points:{tank.points}, '\
           f'Shots in directions:{[(key, value) for key, value in tank.shots.items()]}'

def end_game_info(tank):
    return f'Points:{tank.points}, Shots fired:{sum(tank.shots.values())}'


    #with open('scores.txt', 'w') as file:
        #file.write(f'{tank.player_name}, {tank.points}')
