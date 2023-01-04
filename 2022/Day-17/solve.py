rocks = [[[3,0],[4,0],[5,0],[6,0]],
             [[3,1],[4,2],[4,1],[4,0],[5,1]],
             [[3,0],[5,2],[4,0],[5,0],[5,1]],
             [[3,0],[3,3],[3,2],[3,1]],
             [[3,0],[4,1],[3,1],[4,0]]]

class Rock:
    count = 0
    
    def __init__(self, h):
        self.rect = rocks[Rock.count%5]
        for i in range(len(self.rect)):
            self.rect[i][1] = self.rect[i][1] + h + 4
        self.falling = True
        Rock.count += 1

    def move(self, direction, level):
        if direction == ">":
            dx = 1
            dy = 0
        elif direction == "<":
            dx = -1
            dy = 0
        else:
            dx = 0
            dy = -1
        tmp = self.rect[:]
        for i,pos in enumerate(self.rect):
            x = pos[0] + dx
            y = pos[1] + dy
            if (x,y) in level and dy != 0:
                self.falling = False
                return
            elif (x,y) in level and dy == 0:
                return
            elif x < 1 or x > 7:
                return
            else:
                tmp[i] = (x,y)
        self.rect = tmp[:]
        

def part1(data):
    level = {(1,0):1,(2,0):1,(3,0):1,(4,0):1,(5,0):1,(6,0):1,(7,0):1}
    dlen = len(data)
    h = 0
    rock = Rock(h)
    i = 0
    while Rock.count < 2021:
        if i >= dlen:
            i = 0
        if rock.falling:
            #print(rock.rect)
            rock.move(data[i],level)
            rock.move("down",level)
            i += 1
        else:
            if Rock.count % 100 == 0:
                print(Rock.count)
            for pos in rock.rect:
                level[pos] = 1
            #print(level)
            if rock.rect[1][1] > h:
                h = rock.rect[1][1]
            del rock
            rock = Rock(h)
    return h

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
