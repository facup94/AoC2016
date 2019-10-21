def split_line(data: str):
    parts = data.split("-")

    name = ''.join(parts[:-1])
    sector_id = int(parts[-1][:-7])
    checksum = parts[-1][-6:-1]

    return name, sector_id, checksum


def count_letters(name: str):
    count = dict()

    for letter in name:
        if letter not in count:
            count[letter] = 0

        count[letter] += 1

    return count


def get_most_used_letters(letters):
    top_1, top_2, top_3, top_4, top_5 = '', '', '', '', ''
    top_1_n, top_2_n, top_3_n, top_4_n, top_5_n = 0, 0, 0, 0, 0

    for key, value in letters.items():
        if value > top_1_n or (value == top_1_n and key < top_1):
            top_1_n, top_2_n, top_3_n, top_4_n, top_5_n = value, top_1_n, top_2_n, top_3_n, top_4_n
            top_1, top_2, top_3, top_4, top_5 = key, top_1, top_2, top_3, top_4

        elif value > top_2_n or (value == top_2_n and key < top_2):
            top_2_n, top_3_n, top_4_n, top_5_n = value, top_2_n, top_3_n, top_4_n
            top_2, top_3, top_4, top_5 = key, top_2, top_3, top_4

        elif value > top_3_n or (value == top_3_n and key < top_3):
            top_3_n, top_4_n, top_5_n = value, top_3_n, top_4_n
            top_3, top_4, top_5 = key, top_3, top_4

        elif value > top_4_n or (value == top_4_n and key < top_4):
            top_4_n, top_5_n = value, top_4_n
            top_4, top_5 = key, top_4

        elif value > top_5_n or (value == top_5_n and key < top_5):
            top_5_n = value
            top_5 = key

    return [top_1, top_2, top_3, top_4, top_5]


sum_sectors_id = 0
with open("input.txt", 'r') as f:
    for line in f:
        l_name, l_sector_id, l_checksum = split_line(line.strip())
        most_used_letters = get_most_used_letters(count_letters(l_name))

        if ''.join(most_used_letters) == l_checksum:
            sum_sectors_id += l_sector_id

print(sum_sectors_id)
