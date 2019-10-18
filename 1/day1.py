print("--- Day 1 ---")

values = []

with open('input.txt', 'r') as f:
    for line in f:
        values = line.strip().split(", ")

pos_x, pos_y = 0, 0
direction = 0  # 0=North, 1=East, 2=South, 3=West

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
    if direction == 0:
        pos_y += length
    elif direction == 1:
        pos_x += length
    elif direction == 2:
        pos_y -= length
    elif direction == 3:
        pos_x -= length


# Result
print(abs(pos_y) + abs(pos_x))
