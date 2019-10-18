print("--- Day 1 - B ---")

values = []
visited_intersections = {(0, 0): True}

with open('input.txt', 'r') as f:
    for line in f:
        values = line.strip().split(", ")

pos_x, pos_y = 0, 0
direction = 0  # 0=North, 1=East, 2=South, 3=West
flag = False

for step in values:
    # Rotation
    if step[0] == 'R':
        direction += 1
    else:
        direction -= 1

    direction = direction % 4
    while direction < 0:
        direction += 4

    # Forward
    length = int(step[1:])
    for _ in range(length):
        if direction == 0:
            pos_y += 1
        elif direction == 1:
            pos_x += 1
        elif direction == 2:
            pos_y -= 1
        elif direction == 3:
            pos_x -= 1

        if (pos_x, pos_y) in visited_intersections:
            # Result
            print("pos:", pos_y, pos_x)
            print("distance:", abs(pos_y) + abs(pos_x))
            flag = True
            break

        visited_intersections[(pos_x, pos_y)] = True

    if flag:
        break
