def get_aba_parts(ip: str):
    parts = []

    inside_brackets = False

    i = -1
    while i < len(ip)-3:
        i += 1

        if ip[i+2] == '[':
            inside_brackets = True
            i += 2
            continue
        if ip[i+2] == ']':
            inside_brackets = False
            i += 2
            continue

        part = ip[i:i+3]
        if part[0] == part[2] and part[0] != part[1]:
            parts.append((part[:], inside_brackets))

    return parts


def support_ssl(ip: str):
    parts = get_aba_parts(ip)
    for part in parts:
        if part[1]:
            continue

        if (''.join([part[0][1], part[0][0], part[0][1]]), True) in parts:
            return True

    return False


count = 0
with open('input.txt', 'r') as f:
    for line in f:
        if support_ssl(line.strip()):
            count += 1

print(count)
