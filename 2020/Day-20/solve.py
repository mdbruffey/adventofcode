import numpy
import time

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
                        self.neighbors[d] = tile
                        matches += 1
                        break
        if matches >= 3:
            return
        self.is_corner = True
        return
    
    def transpose(self, direction="left", flip=False):
        new_neighbors = {}
        if direction == "left":
            #print("Rotating Left")
            new_neighbors["top"] = self.neighbors["right"]
            new_neighbors["right"] = self.neighbors["bottom"]
            new_neighbors["bottom"] = self.neighbors["left"]
            new_neighbors["left"] = self.neighbors["top"]
            if flip:
                #print("and flipping...")
                self.image = [[row[i] for row in self.image[::-1]] for i in range(len(self.image[0])-1,-1, -1)]
                new_neighbors["left"], new_neighbors["right"] = new_neighbors["right"], new_neighbors["left"]
            else:
                self.image = [[row[i] for row in self.image] for i in range(len(self.image[0])-1, -1, -1)]
        elif direction =="right":
            #print("Rotating Right")
            new_neighbors["top"] = self.neighbors["left"]
            new_neighbors["right"] = self.neighbors["top"]
            new_neighbors["bottom"] = self.neighbors["right"]
            new_neighbors["left"] = self.neighbors["bottom"]
            if flip:
                #print("and flipping...")
                self.image = [[row[i] for row in self.image] for i in range(len(self.image[0]))]
                new_neighbors["left"], new_neighbors["right"] = new_neighbors["right"], new_neighbors["left"]
            else:
                self.image = [[row[i] for row in self.image[::-1]] for i in range(len(self.image[0]))]
        elif direction == "none" and flip:
            #print("Just Flipping")
            new_neighbors["top"] = self.neighbors["top"]
            new_neighbors["right"] = self.neighbors["left"]
            new_neighbors["bottom"] = self.neighbors["bottom"]
            new_neighbors["left"] = self.neighbors["right"]
            self.image = [[row[i] for i in range(len(self.image[0])-1,-1,-1)] for row in self.image]

        self.neighbors = new_neighbors
        self.get_sides()
        return
    
    def find_next(self):
        next = self.neighbors["right"]
        if next == None:
            return None
        
        for dir, side in next.sides.items():
            if self.sides["right"] == side:
                if dir == "top":
                    next.transpose("right", True)
                elif dir == "right":
                    next.transpose("none", True)
                elif dir == "bottom":
                    next.transpose("right")
                return next
            elif self.sides["right"] == side[::-1]:
                if dir == "top":
                    next.transpose("left")
                elif dir == "right":
                    next.transpose("left")
                    next.transpose("left")
                elif dir == "bottom":
                    next.transpose("left", True)
                elif dir == "left":
                    next.transpose("right", True)
                    next.transpose("left")
                return next
 
        print("Something has gone wrong. There are no matching sides?")
        print(self)
        print(next)
        next.print_neighbors()

    def find_bottom(self):
        bottom = self.neighbors["bottom"]
        if bottom == None:
            return None
        while bottom.neighbors["left"] != None:
            bottom.transpose("left")
        if bottom.neighbors["top"]:
            t_id = bottom.neighbors["top"] .id
        else:
            t_id = None
        if t_id != self.id:
            bottom.transpose("right", True)
            bottom.transpose("left")
        return bottom
    
    def print_neighbors(self):
        for dir, tile in self.neighbors.items():
            if tile:
                id = tile.id
            else:
                id = None
            print(f"{dir}: {id}")

    def __str__(self):
        string = f"Tile: {self.id}"
        for row in self.image:
            string += "\n" + "".join(row)
        return string


def assemble_row(start):
    row = []
    curr = start
    while curr:
        row.append(curr)
        curr = curr.find_next()
    return row

def assemble_image(image):
    comp = []
    for row in image:
        for i in range(1,len(row[0].image[0])-1):
            line = []
            for tile in row:
                line.extend(tile.image[i][1:-1])
            comp.append(line)

    return comp


                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

def count_dragons(image):
    count = 0
    for i in range(1,len(image)-1):
        for j in range(0, len(image[0])-20):
            l1 = image[i-1][j+19]
            l2 = image[i][j] + image[i][j+5] + image[i][j+6] + image[i][j+11] + image[i][j+12] + image[i][j+17] + image[i][j+18] + image[i][j+19] + image[i][j+20]
            l3 = image[i+1][j+1] + image[i+1][j+4] + image[i+1][j+7] + image[i+1][j+10] + image[i+1][j+13] + image[i+1][j+16]
            if "." not in l1 and "." not in l2 and "." not in l3:
                count += 1
    return count

def rotate(image):
    image = [[row[i] for row in image] for i in range(len(image[0])-1, -1, -1)]
    print(f"Image dimensions: {len(image[0])}x{len(image)}")
    return image

def part1(tiles):
    value = 1
    for tile in tiles:
        tile.find_matches(tiles)
        if tile.is_corner:
            value *= tile.id

    return value

def part2(tiles):
    corners = []
    for tile in tiles:
        tile.find_matches(tiles)
        if tile.is_corner:
            corners.append(tile)
    for corner in corners:
        if corner.neighbors["top"] == None and corner.neighbors["left"] == None:
            start = corner
    image = []
    while start != None:
        row = assemble_row(start)
        image.append(row)
        start = start.find_bottom()

    print(f"{len(image)*len(image[0])} tiles in the image")
    image = assemble_image(image)
    dragons = count_dragons(image)
    if dragons == 0:
        for i in range(3):
            image = rotate(image)
            dragons += count_dragons(image)
    image = [[row[i] for i in range(len(image[0])-1,-1,-1)] for row in image]
    print(f"Image dimensions: {len(image[0])}x{len(image)}")
    for i in range(4):
        dragons += count_dragons(image)
        image = rotate(image)

    roughness = 0
    for row in image:
        roughness += row.count("#")
    return roughness - dragons*15

with open("input.txt") as file:
    data = file.read()
raw = data.split("\n\n")
tiles = []
for tile in raw:
    t_id, info = tile.split(":")
    t_id = int(t_id.split()[1])
    t_image = list(info.split("\n")[1:])
    tiles.append(Tile(t_id,t_image))

res1 = part1(tiles)
res2 = part2(tiles)
print(f"Part 1: {res1}\nPart 2: {res2}")