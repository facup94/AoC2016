screen = [[False for i in range(50)] for j in range(6)]

with open('input.txt', 'r') as f:
    for line in f:
        action = line.strip().split(" ")[0]

        if action == "rect":
            w, h = line.strip().split(" ")[1].split("x")
            for i in range(int(w)):
                for j in range(int(h)):
                    screen[j][i] = True

        elif action == "rotate":
            direction = line.strip().split(" ")[1]
            row_col, _, amount = line.strip().split(" ")[2:]
            row_col = int(row_col.split("=")[1])
            amount = int(amount)

            if direction == "row":
                screen[row_col] = screen[row_col][-amount:] + screen[row_col][:-amount]

            elif direction == "column":
                col_as_row = []
                for i in range(6):
                    col_as_row.append(screen[i][row_col])

                col_as_row = col_as_row[-amount:] + col_as_row[:-amount]

                for i in range(6):
                    screen[i][row_col] = col_as_row[i]

on_pixels = 0
for row in screen:
    for c in row:
        print("#" if c else "·", end="")
        if c:
            on_pixels += 1
    print()

print("ON PIXELS:", on_pixels)
