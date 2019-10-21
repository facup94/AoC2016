import hashlib


puzzle_input = "ojvtpuvg"
i = 0
password = dict()
while len(password) < 8:
    string = puzzle_input + str(i)
    result = hashlib.md5(string.encode()).hexdigest()

    if result[:5] == "00000":
        if result[5] in ['0', '1', '2', '3', '4', '5', '6', '7'] and not result[5] in password:
            password[result[5]] = result[6]
            print("decrypting password... ", len(password)*100/8.0, "%", sep="")

    i += 1


print("password:", ''.join([password['0'], password['1'], password['2'], password['3'], password['4'], password['5'], password['6'], password['7']]))
