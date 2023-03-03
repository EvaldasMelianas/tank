def draw_map(tank, target, size):
    print("  " + " ".join(str(i) for i in reversed(range(1, size + 1))))
    for y in reversed(range(1, size + 1)):
        row = []
        for x in reversed(range(1, size + 1)):
            if tank.x == x and tank.y == y:
                row.append("T")
            elif target.x == x and target.y == y:
                row.append("X")
            else:
                row.append("-")
        print(f"{y} {' '.join(row)}")
