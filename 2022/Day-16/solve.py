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

def get_next(current, paths, rates, on, time):
    value = {}
    for node in paths:
        d = find_d(current, node, paths)
        rate = rates[node]
        if d != 0 and node not in on:
            value[rate*(time-d)/(d**1.1)] = node
    if len(value) == 0:
        return "AA"
    return value[max(value)]

def get_next2(current, paths, rates, on, time, dest, e0):
    value = {}
    exp = e0
    for node in paths:
        d = find_d(current, node, paths)
        rate = rates[node]
        if d != 0 and node not in on and node not in dest and d < time-1:
            value[rate*(time-d)/(d**exp+2)] = node
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
        if current not in on:
            relieved += rates[current]*time
            on.append(current)
        nxt = get_next(current, paths, rates, on, time)
        time -= find_d(current, nxt, paths) + 1
        current = nxt
        
    return relieved

def part2(data):
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

    exp = 0.65
        
    on = []
    dest = []
    relieved = 0
    time = 26
    current1 = "AA"
    traveling1 = False
    t1 = 0
    current2 = "AA"
    traveling2 = False
    t2 = 0
    while time > 0:
        if not traveling1:
            print(f"Elephant -- Node: {current1} -- {time}")
            if current1 not in on:
                relieved += rates[current1]*time
                on.append(current1)
            nxt1 = get_next2(current1, paths, rates, on, time, dest, exp)
            print(f"Next: {nxt1}")
            dest.append(nxt1)
            t1 = find_d(current1, nxt1, paths)
            traveling1 = True
        else:
            t1 -= 1
            if t1 == 0:
                traveling1 = False
                current1 = nxt1
        if not traveling2:
            print(f"Me -- Node: {current2} -- {time}")
            if current2 not in on:
                relieved += rates[current2]*time
                on.append(current2)
            nxt2 = get_next2(current2, paths, rates, on, time, dest, exp)
            print(f"Next: {nxt2}")
            dest.append(nxt2)
            t2 = find_d(current2, nxt2, paths)
            traveling2 = True
        else:
            t2 -= 1
            if t2 == 0:
                traveling2 = False
                current2 = nxt2
        time -= 1
        
    return relieved

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
