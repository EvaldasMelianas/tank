def info(tank):
    return '\n'*3, f"Points:{tank.points}, Shots in directions:{[(key, value) for key, value in tank.shots.items()]}"


def save_score(tank):
    with open('scores.txt', 'a+') as file:
        file.write(f'{input(str("Please provide name: "))}, {tank.points}\n')
        file.close()


def top():
    try:
        with open('scores.txt', 'r') as file:
            scores = [line.strip().split(', ') for line in file]
            sorted_scores = enumerate(sorted(scores, key=lambda x: int(x[1]), reverse=True), 1)
            return '\n'.join([str(score) for score in sorted_scores][:5])
    except FileNotFoundError:
        return 'No scores are set'