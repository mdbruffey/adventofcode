def get_rocks(line, rocks):
    points = line.split(" -> ")
    for i in range(len(points)-1):
        x1 = int(points[i].split(",")[0])
        y1 = int(points[i].split(",")[1])
        x2 = int(points[i+1].split(",")[0])
        y2 = int(points[i+1].split(",")[1])
        if x1 > x2 or y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for i in range(x2-x1+1):
            for j in range(y2-y1+1):
                rocks.add((x1+i,y1+j))

def part1(data):
    lines = data.split("\n")
    rocks = set()
    for line in lines:
        get_rocks(line, rocks)
    screen = []
    minx = min([x[0] for x in rocks])
    maxx = max([x[0] for x in rocks])
    maxy = max([y[1] for y in rocks])
    for j in range(maxy + 2):
        screen.append([" " for __ in range(maxx-minx + 3)])

    sand = set()
    done = False
    while not done:
        x = 500
        y = 0
        falling = True
        while falling:
            if (x, y +1) not in rocks.union(sand):
                y += 1
            else:
                if (x-1, y+1) not in rocks.union(sand):
                    x -= 1
                    y += 1
                elif (x+1, y+1) not in rocks.union(sand):
                    x += 1
                    y += 1
                else:
                    falling = False
            if y >= maxy:
                done = True
                break
        sand.add((x,y))
    for j in range(len(screen)):
        for i in range(len(screen[0])):
            if (i+minx-1,j) in sand:
                screen[j][i] = "O"
            elif (i + minx-1,j) in rocks:
                screen[j][i] = "#"
            print(screen[j][i],end="")
        print("\n",end="")
    print(maxy)
    return len(sand)-1
        

def part2(data):
    lines = data.split("\n")
    rocks = set()
    for line in lines:
        get_rocks(line, rocks)
    screen = []
    minx = min([x[0] for x in rocks])
    maxx = max([x[0] for x in rocks])
    maxy = max([y[1] for y in rocks])
    for j in range(maxy + 2):
        screen.append([" " for __ in range(maxx-minx + 3)])

    sand = set()
    done = False
    while not done:
        x = 500
        y = 0
        falling = True
        while falling:
            
            if y == maxy + 1:
                falling = False
            elif (x, y +1) not in rocks.union(sand):
                y += 1
            else:
                if (x-1, y+1) not in rocks.union(sand):
                    x -= 1
                    y += 1
                elif (x+1, y+1) not in rocks.union(sand):
                    x += 1
                    y += 1
                else:
                    falling = False
        if (x,y) == (500,0):
            done = True
        sand.add((x,y))
    """
    for j in range(len(screen)):
        for i in range(len(screen[0])):
            if (i+minx-1,j) in sand:
                screen[j][i] = "O"
            elif (i + minx-1,j) in rocks:
                screen[j][i] = "#"
            print(screen[j][i],end="")
        print("\n",end="")
        """
    return len(sand)

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
#res2 = part2(data)
print(f"Part 1: {res1}\nPart 2 {res2}")
