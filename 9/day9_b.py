import re


def decompress(s):
    if len(s) == 0:
        return 0

    m = re.search("\(\d+x\d+\)", s)

    if not m:
        return len(s)

    size, rep = m.group()[1:-1].split("x")
    size, rep = int(size), int(rep)

    s1 = s[:m.start()]
    s2 = s[m.end():m.end()+size]
    s3 = s[m.end()+size:]

    ss2 = rep * decompress(s2)
    ss3 = decompress(s3)

    return len(s1) + ss2 + ss3


with open('input.txt', 'r') as f:
    puzzle_input = f.readline().strip().replace(" ", "")

print(decompress(puzzle_input))
