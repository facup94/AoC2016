import hashlib


puzzle_input = "ojvtpuvg"
i = 0
password = []
while len(password) < 8:
    string = puzzle_input + str(i)
    result = hashlib.md5(string.encode())

    if result.hexdigest()[:5] == "00000":
        password.append(result.hexdigest()[5])
        print("decrypting password... ", len(password)*100/8.0, "%", sep="")

    i += 1


print("password:", ''.join(password))
