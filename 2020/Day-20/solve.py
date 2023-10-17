import numpy

class Tile:
    def __init__(self, t_id, t_image):
        self.image = t_image
        self.id = t_id
        self.get_sides()
        self.is_corner = False
    
    def get_sides(self):
        self.sides = {"top" : self.image[0], 
                      "bottom" :self.image[-1]}
        left = ""
        right = ""
        for row in self.image:
            left += row[0]
            right += row[-1]
        self.sides["left"]= left
        self.sides["right"] = right

    def find_matches(self, tiles):
        self.neighbors = {"top": None,
                          "right": None,
                          "bottom": None,
                          "left": None}
        matches = 0
        for tile in tiles:
            if tile.id == self.id:
                continue
            for dir, side in tile.sides.items():
                for d, s in self.sides.items():
                    if side == s or side[::-1] == s:
                        self.neighbors[dir] = tile
                        matches += 1
                        break
        if matches >= 3:
            return
        print(f"Tile {self.id}: {matches} matches")
        self.is_corner = True
        return
    
    def transpose(self, direction="left", flip=False):
        new_neighbors = {}
        if direction == "left":
            new_neighbors["top"] = self.neighbors["right"]
            new_neighbors["right"] = self.neighbors["bottom"]
            new_neighbors["bottom"] = self.neighbors["left"]
            new_neighbors["left"] = self.neighbors["top"]
            if flip:
                self.image = [[row[i] for row in self.image[::-1]] for i in range(len(self.image[0])-1,-1, -1)]
                new_neighbors["left"], new_neighbors["right"] = new_neighbors["right"], new_neighbors["left"]
            else:
                self.image = [[row[i] for row in self.image] for i in range(len(self.image[0])-1, -1, -1)]
        elif direction =="right":
            new_neighbors["top"] = self.neighbors["left"]
            new_neighbors["right"] = self.neighbors["top"]
            new_neighbors["bottom"] = self.neighbors["right"]
            new_neighbors["left"] = self.neighbors["bottom"]
            if flip:
                self.image = [[row[i] for row in self.image] for i in range(len(self.image[0]))]
                new_neighbors["left"], new_neighbors["right"] = new_neighbors["right"], new_neighbors["left"]
            else:
                self.image = [[row[i] for row in self.image[::-1]] for i in range(len(self.image[0]))]
        elif direction == "none" and flip:
            new_neighbors["top"] = self.neighbors["top"]
            new_neighbors["right"] = self.neighbors["left"]
            new_neighbors["bottom"] = self.neighbors["bottom"]
            new_neighbors["left"] = self.neighbors["right"]
            self.image = [[row[i] for i in range(len(self.image[0])-1,-1,-1)] for row in self.image]

        self.neighbors = new_neighbors
        return
    
    def __str__(self):
        string = f"Tile: {self.id}"
        for row in self.image:
            string += "\n" + "".join(row)
        return string

def assemble_row(start):
    row = [start]
    curr = start
    next = start.neighbors["right"]
    while next != None:
        for dir, side in next.sides.items():
            if curr.sides["right"] == side:
                if dir == "top":
                    next.transpose("right", True)
                elif dir == "right":
                    next.transpose("none", True)
                elif dir == "bottom":
                    next.transpose("right")
            elif curr.sides["right"] == side[::-1]:
                if dir == "top":
                    next.transpose("left")
                elif dir == "right":
                    next.transpose("left")
                    next.transpose("left")
                elif dir == "bottom":
                    next.transpose("left", True)
                elif dir == "left":
                    next.transpose("right", True)
                    next.tranpose("left")

        row.append(next)
        curr = next
        next = curr.neighbors["right"]
    return row

def part1(data):
    raw = data.split("\n\n")
    tiles = []
    for tile in raw:
        t_id, info = tile.split(":")
        t_id = int(t_id.split()[1])
        t_image = info.split("\n")[1:]
        tiles.append(Tile(t_id,t_image))
    value = 1
    for tile in tiles:
        tile.find_matches(tiles)
        if tile.is_corner:
            value *= tile.id

    return value

def part2(data):
    raw = data.split("\n\n")
    tiles = []
    for tile in raw:
        t_id, info = tile.split(":")
        t_id = int(t_id.split()[1])
        t_image = info.split("\n")[1:]
        tiles.append(Tile(t_id,t_image))
    corners = []
    for tile in tiles:
        tile.find_matches(tiles)
        if tile.is_corner:
            corners.append(tile)
    for corner in corners:
        if corner.neighbors["top"] == None and corner.neighbors["left"] == None:
            start = corner
    row = assemble_row(start)
    print(len(row))

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")