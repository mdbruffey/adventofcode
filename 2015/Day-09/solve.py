import random

def get_distance(city1, city2, distances):
    if city1 > city2:
        return distances[(city2, city1)]
    else:
        return distances[(city1, city2)]

def find_shortest_path(cities, distances):
    min_distance = 10000
    for i in range(1000000):
        distance = find_path_length(cities, distances, min_distance)
        if distance < min_distance:
            min_distance = distance
        random.shuffle(cities)

    return min_distance

def find_longest_path(cities, distances):
    max_distance = 0
    for i in range(1000000):
        distance = find_path_length(cities, distances, min=False)
        if distance > max_distance:
            max_distance = distance
        random.shuffle(cities)

    return max_distance

def find_path_length(path, distances, limit=0, min=True):
    distance = 0
    for i in range(len(path)-1):
        distance += get_distance(path[i], path[i+1], distances)
        if min and distance > limit:
            break
    return distance

def part1(data):
    cities = set()
    distances = {}
    for line in data:
        path, distance = line.split(" = ")
        distance = int(distance.strip("\n"))
        pair = path.split(" to ")
        pair.sort()
        cities.update(pair)
        distances[tuple(pair)] = distance
    cities = list(cities)
    return find_shortest_path(cities, distances)

def part2(data):
    cities = set()
    distances = {}
    for line in data:
        path, distance = line.split(" = ")
        distance = int(distance.strip("\n"))
        pair = path.split(" to ")
        pair.sort()
        cities.update(pair)
        distances[tuple(pair)] = distance
    cities = list(cities)
    return find_longest_path(cities, distances)

with open("input.txt") as file:
    data = file.readlines()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")