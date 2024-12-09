import time
import math

class Vec():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def diff(self, pt):
        return Vec(pt.x-self.x, pt.y-self.y)
    
    def add(self, pt):
        return Vec(self.x + pt.x, self.y + pt.y)
    
    def sub(self, pt):
        return Vec(self.x - pt.x, self.y - pt.y)
    
    def in_grid(self, grid):
        return self.x >= 0 and self.x < len(grid[0]) and self.y >=0 and self.y < len(grid)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x,self.y))
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Line():
    def __init__(self, pt1, pt2):
        if pt1.x > pt2.x:
            pt1, pt2 = pt2, pt1
        self.rise = pt2.y-pt1.y
        self.run = pt2.x-pt1.x
        self.pt = pt1
        self.b = pt1.y - self.rise/self.run*pt1.x

    def get_points(self,grid):
        upper_y = len(grid)
        upper_x = len(grid[0])
        points = []
        for x in range(upper_x):
            y = self.rise/self.run*x + self.b
            if y >= upper_y or y < 0:
                continue
            if math.isclose(y,int(y),abs_tol=0.05):
                points.append((x,int(y)))
        return points

    def __str__(self):
        return f"y = {self.rise/self.run}x + {self.b}"

def get_points(pt1, pt2, grid):
    dx = pt2.x-pt1.x
    dy = pt2.y-pt1.y
    x,y = pt1.x, pt1.y
    points = set()
    while x >= 0 and x < len(grid[0]) and y >=0 and y < len(grid):
        points.add((x,y))
        x += dx
        y += dy
    x,y = pt1.x, pt1.y
    while x >= 0 and x < len(grid[0]) and y >=0 and y < len(grid):
        points.add((x,y))
        x -= dx
        y -= dy
    return points

def part1(data):
    frequencies = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            char = data[y][x]
            if char != ".":
                frequencies[char] = frequencies.get(char, []) + [Vec(x,y)]
    antinodes = set()
    for frequency in frequencies:
        ants = frequencies[frequency]
        for i in range(len(ants)):
            for j in range(i+1,len(ants)):
                diff = ants[i].diff(ants[j])
                antinodes.add(ants[i].sub(diff))
                antinodes.add(ants[j].add(diff))
    remove = set()
    for node in antinodes:
        if not node.in_grid(data):
            remove.add(node)

    return len(antinodes)-len(remove) 

def part2(data):
    frequencies = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            char = data[y][x]
            if char != ".":
                frequencies[char] = frequencies.get(char, []) + [Vec(x,y)]

    antinodes = set()            
    for frequency in frequencies:
        ants = frequencies[frequency]
        for i in range(len(ants)):
            for j in range(i+1,len(ants)):
                antinodes.update(get_points(ants[i],ants[j],data))

    """for y in range(len(data)):
        for x in range(len(data[0])):
            char = data[y][x]
            if (x,y) in antinodes:
                print("#",end="")
            else:
                print(data[y][x],end="")
        print()"""
    
    return len(antinodes)

with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")