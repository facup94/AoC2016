with open('input.txt', 'r') as f:
    puzzle_input = f.readline().strip().replace(" ", "")

puzzle_output_size = 0
inside_marker = False

while len(puzzle_input) > 0:
    char = puzzle_input[0]

    if char == "(":
        # Get marker
        marker = puzzle_input[:puzzle_input.find(")")+1]
        size, repetitions = marker.split("x")
        size, repetitions = int(size[1:]), int(repetitions[:-1])

        puzzle_input = puzzle_input[len(marker) + size:]

        puzzle_output_size += size * repetitions

    else:
        puzzle_output_size += 1
        puzzle_input = puzzle_input[1:]


print(puzzle_output_size)
