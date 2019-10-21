def split_line(data: str):
    p = data.rfind("-")
    name = data[:p]
    sector_id = int(data[p+1:][:-7])
    checksum = data[p+1:][-6:-1]

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
        if key == "-":
            continue

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


def decrypt_name(name: str, shift: int):
    decrypted_name = []
    for letter in name:
        if letter == "-":
            decrypted_name.append(" ")
            continue

        v = ord(letter)
        v += shift
        while v > ord('z'):
            v -= (ord('z') - ord('a') + 1)

        decrypted_name.append(chr(v))

    return ''.join(decrypted_name)


with open("input.txt", 'r') as f:
    for line in f:
        l_name, l_sector_id, l_checksum = split_line(line.strip())
        most_used_letters = get_most_used_letters(count_letters(l_name))

        if ''.join(most_used_letters) == l_checksum:
            if decrypt_name(l_name, l_sector_id) == "northpole object storage":
                print(l_sector_id)


