possible_triangles = 0
with open('input.txt', 'r') as f:
    read = 0
    triangles = [[], [], []]
    for line in f:
        sizes = [int(x) for x in list(filter(None, line.strip().split(" ")))]
        read += 1

        triangles[0].append(sizes[0])
        triangles[1].append(sizes[1])
        triangles[2].append(sizes[2])

        if read == 3:
            read = 0

            if (triangles[0][0] + triangles[0][1] > triangles[0][2]) and (triangles[0][0] + triangles[0][2] > triangles[0][1]) and (triangles[0][1] + triangles[0][2] > triangles[0][0]):
                possible_triangles += 1

            if (triangles[1][0] + triangles[1][1] > triangles[1][2]) and (triangles[1][0] + triangles[1][2] > triangles[1][1]) and (triangles[1][1] + triangles[1][2] > triangles[1][0]):
                possible_triangles += 1

            if (triangles[2][0] + triangles[2][1] > triangles[2][2]) and (triangles[2][0] + triangles[2][2] > triangles[2][1]) and (triangles[2][1] + triangles[2][2] > triangles[2][0]):
                possible_triangles += 1

            triangles = [[], [], []]


print(possible_triangles)
