def count_neighbors(i,j, lights, broken=False):
    if i == 0 and j == 0: #top left corner
        if broken:
            return 3
        neighbors = lights[i+1][j:j+2] + [lights[i][j+1], ]
    elif i == 0 and j == len(lights[0])-1: #top right corner
        if broken:
            return 3
        neighbors = lights[i+1][j-1:j+1] + [lights[i][j-1], ]
    elif j == 0 and i == len(lights)-1: #bottom left corner
        if broken:
            return 3
        neighbors = lights[i-1][j:j+2] + [lights[i][j+1], ]
    elif j == len(lights[0])-1 and i == len(lights)-1: #bottom right corner
        if broken:
            return 3
        neighbors = lights[i-1][j-1:j+1] + [lights[i][j-1], ]
    elif i == 0: #top side
        neighbors = lights[i+1][j-1:j+2] + [lights[i][j-1], lights[i][j+1] ]
    elif j == 0: #left side
        neighbors = lights[i-1][j:j+2] + lights[i+1][j:j+2] + [lights[i][j+1], ]
    elif i == len(lights)-1: #bottom side
        neighbors = lights[i-1][j-1:j+2] + [lights[i][j-1], lights[i][j+1] ]
    elif j == len(lights[0])-1: #right side
        neighbors = lights[i-1][j-1:j+1] + lights[i+1][j-1:j+1] + [lights[i][j-1], ]
    else: #everywhere else
        neighbors = lights[i-1][j-1:j+2] + lights[i+1][j-1:j+2] + [lights[i][j-1], lights[i][j+1] ]

    return neighbors.count("#")

def animate(lights, broken=False):
    new_lights = [["" for i in range(len(lights))] for j in range(len(lights[0]))]
    for i in range(len(lights)):
        for j in range(len(lights[0])):
            on = count_neighbors(i,j, lights, broken)
            if lights[i][j] == "#" and (on != 2 and on != 3):
                new_lights[i][j] = "."
            elif lights[i][j] == "." and on == 3:
                new_lights[i][j] = "#"
            else:
                new_lights[i][j] = lights[i][j]

    return new_lights
def part1(lights):
    for i in range(100):
        lights = animate(lights)

    count = 0
    for row in lights:
        count += row.count("#")
    return count

def part2(lights):
    lights[0][0] = lights[0][len(lights[0])-1] = lights[len(lights)-1][0] = lights[len(lights)-1][len(lights[0])-1]= "#"
    for i in range(100):
        lights = animate(lights, broken=True)

    count = 0
    for row in lights:
        count += row.count("#")
    return count


with open("input.txt") as file:
    data = file.readlines()

lights = []
for line in data:
    line = line.strip("\n")
    line = [c for c in line]
    lights.append(line)

res1 = part1(lights)
res2 = part2(lights)
print(f"Part 1: {res1}\nPart 2: {res2}")