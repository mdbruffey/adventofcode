def mdistance(pos, end):
        x1, y1 = pos
        x2, y2 = end
        return abs(x2-x1) + abs(y2-y1)
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
        dist = {}
        for j in range(len(hmap)):
                for i in range(len(hmap[0])):
                        if hmap[j][i] == "S":
                                hmap[j][i] = "a"
                                start = (i,j)
                                dist[(i,j)] = 0
                        elif hmap[j][i] == "E":
                                hmap[j][i] = "z"
                                end = (i,j)
                                dist[(i,j)] = 10000
                        else:
                                dist[(i,j)] = 10000
        print("Done initializing dist")
        cur = start
        nxt = start
        prev = start
        visited = set()
        while cur != end:
                x,y = cur
                neighbors = get_neighbors(cur, hmap)
                print(f"{cur} has neighbors: {neighbors}")
                min_d = 100000
                for neighbor in neighbors:
                        i,j = neighbor
                        if dist[(i,j)] < dist[cur] and ord(hmap[y][x]) - ord(hmap[j][i]) <= 1:
                                dist[cur] = dist[(i,j)] + 1
                        if hmap[y][x] == "z" and hmap[j][i] == "E":
                                nxt = (i,j)
                                dist[(i,j)] = dist[(x,y)] + 1
                                print(dist[(x,y)])
                                break
                        elif ord(hmap[j][i]) - ord(hmap[y][x]) <= 1:
                                d = dist[(x,y)] + 1
                        else:
                                d = dist[(x,y)] + 10000
                        if d < min_d and (i,j) not in visited:
                                min_d = d
                                nxt = (i, j)
                        elif d == min_d:
                                if ord(hmap[j][i]) - ord(hmap[y][x]) == 1:
                                        nxt = (i,j)
                                elif hmap[j][i] == hmap[y][x]:
                                        nxt = (i,j)
                                elif mdistance((i,j), end) < mdistance(nxt, end):
                                        nxt = (i, j)
                        if d < dist[(i,j)]:
                                dist[(i,j)] = d
                visited.add(cur)
                if cur != nxt:
                        prev, cur = cur, nxt
                else:
                        cur = prev
        return dist[end]

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
