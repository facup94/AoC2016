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


bots = dict()

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

with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip().split(" ")

        if line[0] == "value":
            chip_num = int(line[1])
            bot_num = int(line[-1])

            bots[bot_num].chips.append(chip_num)

flag = True
while flag:
    for bot in bots.values():
        if len(bot.chips) == 2:
            lower = min(bot.chips)
            higher = max(bot.chips)
            bot.chips = []

            if lower == 17 and higher == 61:
                print("Bot that compares value-61 microchips with value-17 microchips: " + str(bot.number))
                flag = False
                break

            if bot.action_lower.dest_type == "bot":
                bots[bot.action_lower.number].chips.append(lower)
            if bot.action_higher.dest_type == "bot":
                bots[bot.action_higher.number].chips.append(higher)

            break
