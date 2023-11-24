import random

def findHappiness(table, people):
    happiness = 0
    for i in range(len(table)):
        if i == 0:
            happiness += people[table[i]][table[-1]] + people[table[i]][table[i+1]]
        elif i == len(table)-1:
            happiness += people[table[i]][table[i-1]] + people[table[i]][table[0]]
        else:
            happiness += people[table[i]][table[i-1]] + people[table[i]][table[i+1]]
    return happiness

def part1(people):
    max_happiness = 0
    table = list(people.keys())
    for i in range(40000):
        random.shuffle(table)
        happiness = findHappiness(table, people)
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness


def part2(people):
    people["me"] = {}
    for key in people:
        people[key]["me"] = 0
        people["me"][key] = 0
    max_happiness = 0
    table = list(people.keys())
    table.append("me")
    for i in range(100000):
        random.shuffle(table)
        happiness = findHappiness(table, people)
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness

with open("input.txt") as file:
    data = file.readlines()

people = {}

for line in data:
    n = line.split()
    name = n[0]
    if name in people:
        neighbors = people[name]
    else:
        neighbors = {}
    neighbor = n[-1][:-1]
    num = int(n[3])
    if n[2] == "lose":
        num *= -1
    neighbors[neighbor] = num
    people[name] = neighbors

res1 = part1(people)
res2 = part2(people)
print(f"Part 1: {res1}\nPart 2: {res2}")