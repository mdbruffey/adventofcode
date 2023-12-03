import time

def part1(games, limits):
    count = 0
    for id in games:
        valid = True
        for round in games[id]:
            if not valid:
                break
            for item in round.split(", "):
                number, color = item.split()
                if int(number) > limits[color]:
                    valid = False
                    break
        if valid:
            count += id

    return count


def part2(games):
    power = 0
    for id in games:
        counts = {"red": 0,
                  "green":0,
                  "blue":0}
        for round in games[id]:
            for item in round.split(", "):
                number, color = item.split()
                if int(number) > counts[color]:
                    counts[color] = int(number)

        mult = 1
        for color in counts:
            mult *= counts[color]
        power += mult
    return power

with open("input.txt") as file:
    data = file.readlines()

games = {}
for line in data:
    line = line.strip("\n").split(": ")
    id = int(line[0].split()[1])
    rounds = line[1].split("; ")
    games[id] = rounds

limits = {"red": 12,
          "green": 13,
          "blue": 14}

start = time.perf_counter()
res1 = part1(games, limits)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(games)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")