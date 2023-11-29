import time
import math

class Bot:
    bots = {}
    outputs = {}
    def __init__(self, id):
        self.id = id
        Bot.bots[self.id] = self
        self.chips = []

    def add_chip(self, chip):
        if len(self.chips) < 2:
            self.chips.append(chip)
        else:
            return False
        return True
    
    def add_rules(self, high, low):
        self.rules = {"high": high,
                      "low": low}
        
    def give_chips(self):
        if len(self.chips) == 2:
            self.chips.sort()
            id = self.rules["low"]
            if "bot" in id:
                if Bot.bots[id].add_chip(self.chips[0]):
                    self.chips.pop(0)
            else:
                if id not in Bot.outputs:
                    Bot.outputs[id] = [self.chips.pop(0)]
                else:
                    Bot.outputs[id].append(self.chips.pop(0))
            id = self.rules["high"]
            if "bot" in id:
                if Bot.bots[id].add_chip(self.chips[-1]):
                    self.chips.pop(-1)
            else:
                if id not in Bot.outputs:
                    Bot.outputs[id] = [self.chips.pop(-1)]
                else:
                    Bot.outputs[id].append(self.chips.pop(-1))



def part1(chips):
    a, b = chips
    target = None
    outputs = ["output 0", "output 1", "output 2"]
    while any([x not in Bot.outputs for x in outputs]) or not target:
        for bot in Bot.bots.values():
            if a in bot.chips and b in bot.chips:
                print(bot.id, bot.chips, bot.rules)
                target = bot.id.split()[1]
            #print(f"{bot.id}: {bot.chips}")
            bot.give_chips()
    return target
def part2():
    return Bot.outputs["output 0"][0]*Bot.outputs["output 1"][0]*Bot.outputs["output 2"][0]

with open("input.txt") as file:
    data = file.readlines()

for line in data:
    if "value" in line:
        line = line.strip("\n").split(" goes to ")
        id = line[1]
        if id not in Bot.bots:
            bot = Bot(id)
        else:
            bot = Bot.bots[id]
        value = int(line[0][6:])
        bot.add_chip(value)
    else:
        line = line.strip("\n").split(" gives low to ")
        id = line[0]
        low, high = line[1].split(" and high to ")
        if id in Bot.bots:
            Bot.bots[id].add_rules(high, low)
        else:
            bot = Bot(id)
            bot.add_rules(high, low)

start = time.perf_counter()
res1 = part1([61,17])
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2()
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")