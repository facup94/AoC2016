possible_triangles = 0
with open('input.txt', 'r') as f:
    for line in f:
        sizes = []
        for num in filter(None, line.strip().split(" ")):
            sizes.append(int(num))

        if (sizes[0] + sizes[1] <= sizes[2]) or (sizes[0] + sizes[2] <= sizes[1]) or (sizes[1] + sizes[2] <= sizes[0]):
            continue

        possible_triangles += 1

print(possible_triangles)
