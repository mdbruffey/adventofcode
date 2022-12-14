class Tile:
    def __init__(self, t_id, t_image):
        self.image = t_image
        self.id = t_id
        self.sides = self.get_sides()
        self.is_corner = False
    
    def get_sides(self):
        sides = [self.image[0], self.image[-1]]
        left = ""
        right = ""
        for row in self.image:
            left += row[0]
            right += row[-1]
        sides.extend([left, right])
        return sides

    def find_matches(self, tiles):
        matches = 0
        for tile in tiles:
            if tile.id == self.id:
                continue
            for side in tile.sides:
                if side in self.sides or side[::-1] in self.sides:
                    matches += 1
            if matches >= 3:
                return
        print(f"Tile {self.id}: {matches} matches")
        self.is_corner = True
        return

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
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")