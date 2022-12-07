class Number:
    def __init__(self, turn):
        self.turn = turn
        self.times = 0

    def called(self, turn):
        if self.times == 0:
            self.times += 1
            self.turn = turn
            return "0"
        else:
            tmp = turn-self.turn
            self.turn = turn
            return str(tmp)

def part1(data):
    start = data.split(",")
    library = {}
    turn = 1
    for number in start[:-1]:
        library[number] = Number(turn)
        library[number].called(turn)
        #print(f"Turn {turn}: {number}")
        turn += 1
    spoken = start[-1]
    #print(f"Turn {turn}: {spoken}")
    turn += 1
    while turn <= 2020:
        if spoken not in library:
            library[spoken] = Number(turn-1)
        spoken = library[spoken].called(turn-1)
        #print(f"Turn {turn}: {spoken}")
        turn += 1
    return spoken

"""
I feel like people who know what they are doing would have
done part 1 differently (aka coded more quickly) but then have to
refactor part 2 to have better time complexity? I made no changes
and part two ran in ~23 seconds-ish
"""
def part2(data):
    start = data.split(",")
    library = {}
    turn = 1
    for number in start[:-1]:
        library[number] = Number(turn)
        library[number].called(turn)
        #print(f"Turn {turn}: {number}")
        turn += 1
    spoken = start[-1]
    #print(f"Turn {turn}: {spoken}")
    turn += 1
    while turn <= 30000000:
        if spoken not in library:
            library[spoken] = Number(turn-1)
        spoken = library[spoken].called(turn-1)
        #print(f"Turn {turn}: {spoken}")
        turn += 1
    return spoken

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)

print(f"Part 1: {res1}\nPart 2: {res2}")
