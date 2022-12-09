class Rope:
    def __init__(self, knots):
        if knots < 2:
            knots = 2
        self.knots = [(0,0) for x in range(knots)]
        self.locations = [(0,0)]

    def move_h(self, string):
        direc, dist = string.split(" ")
        x, y = self.knots[0]
        match direc:
            case "U":
                y += int(dist)
            case "R":
                x += int(dist)
            case "D":
                y -= int(dist)
            case "L":
                x -= int(dist)
        self.knots[0] = (x,y)
        self.update_knots()

    def update_knots(self):
        while self.distance(self.knots[1],self.knots[0]) > 1:
            for i in range(1,len(self.knots)):
                x, y = self.knots[i]
                if self.distance((x,y),self.knots[i-1]) > 1:
                    dx = self.knots[i-1][0]-x
                    dy = self.knots[i-1][1]-y
                    if dx != 0:
                        x += (dx)//abs(dx)
                    if dy != 0:
                        y += (dy)//abs(dy)
                    if i == len(self.knots)-1:
                        self.locations.append((x,y))
                self.knots[i] = x, y

    def distance(self, t1, t2):
        x = abs(t2[0]-t1[0])
        y = abs(t2[1]-t1[1])
        if x > y:
            return x
        return y

    def get_num_locations(self):
        return len(set(self.locations))

def part1(data):
    directions = data.split("\n")
    rope = Rope(2)
    for direction in directions:
        rope.move_h(direction)
    return rope.get_num_locations()

def part2(data):
    directions = data.split("\n")
    rope = Rope(10)
    for direction in directions:
        rope.move_h(direction)
    
    return rope.get_num_locations()

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
