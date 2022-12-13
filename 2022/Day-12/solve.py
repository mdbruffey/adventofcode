from queue import Queue

def get_neighbors(pos, hmap):
        i, j = pos
        d = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []
        for neighbor in d:
                di, dj = neighbor
                x = i + di
                y = j + dj
                if x >= 0 and y >= 0 and x < len(hmap[0]) and y < len(hmap):
                    neighbors.append((x,y))
        return neighbors

def part1(data):
        hmap = data.split("\n")
        for i, row in enumerate(hmap):
                hmap[i] = list(row)
        
        for j in range(len(hmap)):
                for i in range(len(hmap[0])):
                        if hmap[j][i] == "S":
                                hmap[j][i] = "a"
                                start = (i,j)
                        elif hmap[j][i] == "E":
                                hmap[j][i] = "z"
                                end = (i,j)
        frontier = Queue()
        frontier.put(start)
        came_from = dict()
        came_from[start] = None
        
        while not frontier.empty():
                current = frontier.get()
                x,y = current

                if current == end:
                        break

                for neighbor in get_neighbors(current, hmap):
                        i,j = neighbor
                        if ord(hmap[j][i])-ord(hmap[y][x]) <= 1 and neighbor not in came_from:
                                frontier.put(neighbor)
                                came_from[neighbor] = current
        shortest = []
        while current != start:
                shortest.append(current)
                current = came_from[current]
                
        return len(shortest)

def part2(data):
        hmap = data.split("\n")
        for i, row in enumerate(hmap):
                hmap[i] = list(row)
        
        for j in range(len(hmap)):
                for i in range(len(hmap[0])):
                        if hmap[j][i] == "S":
                                hmap[j][i] = "a"
                                start = (i,j)
                        elif hmap[j][i] == "E":
                                hmap[j][i] = "z"
                                end = (i,j)
        paths = []
        for j in range(len(hmap)):
                start = 0,j
                frontier = Queue()
                frontier.put(start)
                came_from = dict()
                came_from[start] = None
                
                while not frontier.empty():
                        current = frontier.get()
                        x,y = current

                        if current == end:
                                break

                        for neighbor in get_neighbors(current, hmap):
                                i,j = neighbor
                                if ord(hmap[j][i])-ord(hmap[y][x]) <= 1 and neighbor not in came_from:
                                        frontier.put(neighbor)
                                        came_from[neighbor] = current
                shortest = []
                while current != start:
                        shortest.append(current)
                        current = came_from[current]
                paths.append(len(shortest))
                
        return min(paths)

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
