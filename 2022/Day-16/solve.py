from queue import PriorityQueue

def part1(data):
    lines = data.split("\n")
    rates = dict()
    paths = dict()
    for line in lines:
        name, info = line.split(" has flow rate=")
        name = name.replace("Valve ","")
        flow, dests = info.split("; ")
        flow = int(flow)
        dests = dests.replace("tunnels lead to valves ","").replace("tunnel leads to valve ","").split(",")
        paths[name] = dests
        rates[name] = flow
    print(rates)
    

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
