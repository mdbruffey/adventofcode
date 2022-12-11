import copy

def is_active(i,j,k,grid):
    count = 0
    for z in range(k-1,k+2):
        for y in range(i-1,i+2):
            count += grid[z][y][j-1:j+2].count("#")
    if grid[k][i][j] == "#":
        count -= 1
    if grid[k][i][j] == "#" and (count == 2 or count ==3):
        return True
    elif grid[k][i][j] == "." and count == 3:
        return True
    else:
        return False

def simulate(x0,y0,z0,grid):
    reference = copy.deepcopy(grid)
    for k in range(1,z0-1):
        for i in range(1,y0-1):
            for j in range(1,x0-1):
                if is_active(i,j,k, reference):
                    grid[k][i][j] = "#"
                else:
                    grid[k][i][j] = "."
    return

def part1(data):
    init = data.split("\n")
    space = 10
    z0 = 13
    x0 = len(init[0]) + space*2
    y0 = len(init) + space*2
    grid = []
    for k in range(z0):
            grid.append([["." for _j in range(x0)] for _y in range(y0)])
    for i in range(len(init)):
        for j in range(len(init[0])):
            grid[6][i+space][j+space] = init[i][j]

    for __ in range(6):
        simulate(x0,y0,z0,grid)

    count = 0
    for z, level in enumerate(grid):
        #print(f"Level: {z-6}")
        for row in level:
            #print(row)
            count += row.count("#")
        #print("\n")

    return count


def is_active_w(i,j,k,l,grid):
    count = 0
    for w in range(l-1,l+2):
        for z in range(k-1,k+2):
            for y in range(j-1,j+2):
                count += grid[w][z][y][i-1:i+2].count("#")
    if grid[l][k][j][i] == "#":
        count -= 1
    if grid[l][k][j][i] == "#" and (count == 2 or count ==3):
        return True
    elif grid[l][k][j][i] == "." and count == 3:
        return True
    else:
        return False

def simulate_w(x0,y0,z0,w0,grid):
    reference = copy.deepcopy(grid)
    for w in range(1,w0-1):
        for z in range(1,z0-1):
            for y in range(1,y0-1):
                for x in range(1,x0-1):
                    if is_active_w(x,y,z,w,reference):
                        grid[w][z][y][x] = "#"
                    else:
                        grid[w][z][y][x] = "."
    return            

def part2(data):
    init = data.split("\n")
    space = 10
    w0 = 21
    z0 = 21
    x0 = len(init[0]) + space*2
    y0 = len(init) + space*2
    grid = []
    for w in range(w0):
            grid.append([[["." for _j in range(x0)] for _y in range(y0)]for _z in range(z0)])
    for i in range(len(init)):
        for j in range(len(init[0])):
            grid[w0//2][z0//2][i+space][j+space] = init[i][j]
    
    for __ in range(6):
        simulate_w(x0,y0,z0,w0,grid)

    count = 0
    for w,space in enumerate(grid):
        #print(f"Space: {w-2}")
        for k,level in enumerate(space):
            #print(f"Level: {k-2}")
            for row in level:
                #print(row)
                count += row.count("#")

    return count

with open('input.txt') as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
