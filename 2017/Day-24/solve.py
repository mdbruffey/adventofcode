import time

class Component:
    def __init__(self, port1, port2, id):
        self.port1 = port1
        self.port2 = port2
        self.id = id

    def get_open(self, connected_port):
        if connected_port == self.port1:
            return self.port2
        if connected_port == self.port2:
            return self.port1
        else:
            return None

    def get_ports(self):
        return (self.port1, self.port2)

    def find_free_matching_components(self, open_port, bridge, components): 
        matching = []
        for component in components.values():
            if open_port in component.get_ports() and component not in bridge:
                matching.append(component)
        return matching

    def __repr__(self):
        return f"{self.port1}/{self.port2}"

def find_free_port(bridge):
    connected_port = 0
    for component in bridge:
        connected_port = component.get_open(connected_port)
    return connected_port

def part1(components):
    seen = set()
    queue = [(c,) for c in components.values() if 0 in c.get_ports()]
    while len(queue):
        curr = queue.pop()
        if curr not in seen:
            seen.add(curr)
            end = curr[-1]
            open_port = find_free_port(curr)
            for option in end.find_free_matching_components(open_port, curr, components):
                queue.append(curr + (option,))
    return max([sum([c.port1 + c.port2 for c in bridge]) for bridge in seen])

def part2(components):
    seen = set()
    queue = [(c,) for c in components.values() if 0 in c.get_ports()]
    while len(queue):
        curr = queue.pop()
        if curr not in seen:
            seen.add(curr)
            end = curr[-1]
            open_port = find_free_port(curr)
            for option in end.find_free_matching_components(open_port, curr, components):
                queue.append(curr + (option,))
    max_length = 0
    for bridge in seen:
        if len(bridge) > max_length:
            max_length = len(bridge)
    longest = [bridge for bridge in seen if len(bridge) == max_length]
    return max([sum([c.port1 + c.port2 for c in bridge]) for bridge in longest])

with open("input.txt") as file:
    data = file.read().split("\n")

components = {}
for i,line in enumerate(data):
    port1, port2 = list(map(int,line.split("/")))
    components[i] = Component(port1, port2, i)

start = time.perf_counter()
res1 = part1(components)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(components)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")