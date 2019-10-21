def has_abba(ip: str):
    for i in range(len(ip)-3):
        part = ip[i:i+4]
        if part[0] == part[3] and part[1] == part[2] and part[0] != part[1]:
            return True
    return False


def has_abba_inside_bracket(ip: str):
    inside_brackets = False
    for i in range(len(ip)-3):
        if ip[i] == '[':
            inside_brackets = True
            continue

        if ip[i] == ']':
            inside_brackets = False
            continue

        if not inside_brackets:
            continue

        part = ip[i:i+4]
        if part[0] == part[3] and part[1] == part[2] and part[0] != part[1]:
            return True
    return False


def support_tls(ip: str):
    return has_abba(ip) and not has_abba_inside_bracket(ip)


count = 0
with open('input.txt', 'r') as f:
    for line in f:
        if support_tls(line.strip()):
            count += 1

print(count)
