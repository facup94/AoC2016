characters = {
    0: dict(),
    1: dict(),
    2: dict(),
    3: dict(),
    4: dict(),
    5: dict(),
    6: dict(),
    7: dict()
}

with open('input.txt', 'r') as f:
    for line in f:
        stripped_line = line.strip()
        for col in range(len(stripped_line)):
            char = stripped_line[col]
            if char not in characters[col]:
                characters[col][char] = 0

            characters[col][char] += 1

message = []
for i in range(8):
    most_used = ''
    most_used_n = 0

    for key, value in characters[i].items():
        if value > most_used_n:
            most_used_n = value
            most_used = key

    message.append(most_used)

print(''.join(message))
