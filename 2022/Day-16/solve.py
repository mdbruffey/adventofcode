from queue import Queue

def find_d(start, end, paths):
    frontier = Queue()
    comes_from = {}
    comes_from[start] = None
    frontier.put(start)
    while not frontier.empty():
        node = frontier.get()
        if node == end:
            break
        for neighbor in paths[node]:
            if neighbor not in comes_from:
                frontier.put(neighbor)
                comes_from[neighbor] = node
    count = 0
    while node != start:
        node = comes_from[node]
        count += 1
    return count

def get_next(current, paths, rates, on):
    value = {}
    for node in paths:
        d = find_d(current, node, paths)
        rate = rates[node]
        if d != 0 and node not in on:
            value[rate/d] = node
    if len(value) == 0:
        return "AA"
    return value[max(value)]

def part1(data):
    lines = data.split("\n")
    rates = dict()
    paths = dict()
    for line in lines:
        name, info = line.split(" has flow rate=")
        name = name.replace("Valve ","")
        flow, dests = info.split("; ")
        flow = int(flow)
        dests = dests.replace("tunnels lead to valves ","").replace("tunnel leads to valve ","").replace(" ","").split(",")
        paths[name] = dests
        rates[name] = flow
    on = []
    relieved = 0
    time = 30
    current = "AA"
    while time > 0:
        print(f"Node: {current} -- {time}")
        if current not in on:
            relieved += rates[current]*time
            on.append(current)
        nxt = get_next("AA", paths, rates, on)
        time -= find_d(current, nxt, paths) + 1
        current = nxt
        
    return relieved

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
