class Destination:
    def __init__(self, dest_type, number):
        self.dest_type = dest_type
        self.number = number
        self.chips = []

    def __repr__(self):
        return self.dest_type + " " + str(self.number)


class Bot:
    def __init__(self, number, lower: Destination, higher: Destination):
        self.number = number
        self.action_lower = lower
        self.action_higher = higher
        self.chips = []

    def __repr__(self):
        return "BOT " + str(self.number) +\
               " - lower: " + str(self.action_lower) +\
               " - higher: " + str(self.action_higher) +\
               " - chips: " + repr(self.chips)


class Output:
    def __init__(self, number):
        self.number = number
        self.chips = []

    def __repr__(self):
        return str(self.number) + " " + repr(self.chips)


bots = dict()
outputs = dict()

with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip().split(" ")

        if line[0] == "bot":
            num = int(line[1])
            low_type = line[5]
            low_num = int(line[6])
            high_type = line[10]
            high_num = int(line[11])

            new_bot = Bot(num, Destination(low_type, low_num), Destination(high_type, high_num))

            bots[num] = new_bot

            if low_type == "output" and low_num not in outputs:
                    outputs[low_num] = Output(low_num)
            if high_type == "output" and high_num not in outputs:
                    outputs[high_num] = Output(high_num)

with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip().split(" ")

        if line[0] == "value":
            chip_num = int(line[1])
            bot_num = int(line[-1])

            bots[bot_num].chips.append(chip_num)

while True:
    changed = False

    for bot in bots.values():
        if len(bot.chips) == 2:
            changed = True

            lower = min(bot.chips)
            higher = max(bot.chips)
            bot.chips = []

            if bot.action_lower.dest_type == "bot":
                bots[bot.action_lower.number].chips.append(lower)
            elif bot.action_lower.dest_type == "output":
                outputs[bot.action_lower.number].chips.append(lower)

            if bot.action_higher.dest_type == "bot":
                bots[bot.action_higher.number].chips.append(higher)
            elif bot.action_higher.dest_type == "output":
                outputs[bot.action_higher.number].chips.append(higher)

            break

    if not changed:
        break

print(outputs[0].chips[0] * outputs[1].chips[0] * outputs[2].chips[0])
