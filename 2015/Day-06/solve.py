def operate(operation, subset, lights):
    i1, j1 = subset[0]
    i2, j2 = subset[1]
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            if operation == "toggle":
                lights[i][j] = not lights[i][j]
            elif operation == "on":
                lights[i][j] = True
            else:
                lights[i][j] = False

def operateBrightness(operation, subset, lights):
    i1, j1 = subset[0]
    i2, j2 = subset[1]
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            if operation == "toggle":
                lights[i][j] += 2
            elif operation == "on":
                lights[i][j] += 1
            elif lights[i][j] > 0:
                lights[i][j] -= 1

def countLights(lights):
    count = 0
    for row in lights:
        count += row.count(True)

    return count

def countLightBrightness(lights):
    count = 0
    for i in range(len(lights)):
        for j in range(len(lights[0])):
            count += lights[i][j]

    return count

def part1(data):
    lights = [[False for i in range(1000)] for j in range(1000)]
    for line in data:
        line = line.split()
        operation = line[-4]
        p1 = map(int, line[-3].split(","))
        p2 = map(int, line[-1].split(","))
        operate(operation, [p1,p2], lights)

    return countLights(lights)

def part2(data):
    lights = [[False for i in range(1000)] for j in range(1000)]
    for line in data:
        line = line.split()
        operation = line[-4]
        p1 = map(int, line[-3].split(","))
        p2 = map(int, line[-1].split(","))
        operateBrightness(operation, [p1,p2], lights)

    return countLightBrightness(lights)

with open("input.txt") as file:
    data = file.readlines()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
