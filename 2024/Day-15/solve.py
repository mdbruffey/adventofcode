import time
import keyboard

directions = {
    "^":(0,-1),
    ">":(1,0),
    "v":(0,1),
    "<":(-1,0)
}

key_dirs = {
    "up":(0,-1),
    "right":(1,0),
    "down":(0,1),
    "left":(-1,0)
}

def move_object(pos, direction, grid):
        x,y = pos
        dx, dy = direction
        nx, ny = x + dx, y + dy
        if grid[ny][nx] == "#": #wall; object doesn't move
            return pos
        elif grid[ny][nx] == "O": #box; might push it, might not be able to
            #all sorts of things we have to figure out here
            move_object((nx,ny),direction, grid)
            if grid[ny][nx] == "O":
                return pos
        grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
        return (nx, ny)

def can_move(pos, direction, grid, connected=False):
    moves = True
    x,y = pos
    dx, dy = direction
    nx, ny = x + dx, y + dy
    curr = grid[y][x]
    if dy !=0 and not connected: #make sure connected half can also move
        if curr == "[":
            moves = can_move((x+1,y),direction,grid,connected=True)
        elif curr == "]":
            moves = can_move((x-1,y),direction,grid,connected=True)
    if not moves: #if the other half can't this one can't either
        return False

    if grid[ny][nx] == "#":#wall -- can't move
        return False
    elif grid[ny][nx] in "[]": #make sure that boxes in front of this can also move
        return can_move((nx,ny),direction,grid)
    return True
    

#There's still a problem, but I don't know what it is yet
def move_object_2(pos, direction, grid, connected=False): 
        x,y = pos
        dx, dy = direction
        nx, ny = x + dx, y + dy
        curr = grid[y][x]
        #first, if the current object is part of a box, check to make sure the other half isn't blocked by a wall
        if curr == "[":
            if not can_move((x+1,y),direction, grid,connected=True):
                return pos
        elif curr == "]":
            if not can_move((x-1,y),direction, grid,connected=True):
                return pos
        #check object in desired direction of motion
        if grid[ny][nx] == "#": #wall; object doesn't move
            return pos
        elif grid[ny][nx] in "[]": #box; might push it
            move_object_2((nx,ny),direction, grid) #attempt to move the blocking object
            if grid[ny][nx] in "[]": #the blocking object didn't move
                return pos
        #if moving vertically need to make sure the other half of the box moves too
        #I added  "connected" boolean to make sure this doesn't just cause an infinite recursion loop
        if dy != 0 and not connected:
            if curr == "[":
                move_object_2((x+1,y),direction,grid,connected=True)
                if grid[y][x+1] == "]":
                    return pos
            elif curr == "]":
                move_object_2((x-1,y),direction,grid,connected=True)
                if grid[y][x-1] == "[":
                    return pos
        grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
        return (nx, ny)

def print_grid(grid):
    for line in grid:
        print("".join(line))

def part1(data, moves):
    grid = [list(line) for line in data]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                pos = (j,i)
                break

    for move in moves:
        pos = move_object(pos, directions[move], grid)

    value = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                value += 100*i + j
    return value

def part2(data, moves):
    grid = []
    #Generating new, expanded grid
    for i,line in enumerate(data):
        new = ""
        for char in line:
            if char == "O":
                new += "[]"
            elif char == "@":
                pos = (len(new), i)
                new += char + "."
            else:
                new += char + char
        grid.append(list(new))
        
    #code for manually controlling the robot; I used this to more easily test edge cases
    """while True:
        print_grid(grid)
        key = keyboard.read_key()
        if key not in key_dirs:
            continue
        elif key == "esc":
            return 0
        pos = move_object_2(pos, key_dirs[key], grid)
        time.sleep(0.1)"""

    for move in moves:
        #print_grid(grid)
        #input(f"Next: {move}")
        pos = move_object_2(pos, directions[move], grid)
    value = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                value += 100*i + j
    return value

with open("input.txt") as file:
    data = file.read()

grid, moves = data.split("\n\n")
grid = grid.splitlines()
moves = moves.replace("\n","")

start = time.perf_counter()
res1 = part1(grid, moves)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(grid, moves)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")