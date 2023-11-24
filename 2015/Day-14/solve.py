class Reindeer:
    def __init__(self, speed, time, rest):
        self.speed = speed
        self.runTime = time
        self.restTime = rest
        self.resting = 0
        self.running = time
        self.position = 0
        self.score = 0

    def update(self):
        if self.running and not self.resting:
            self.position += self.speed
            self.running -= 1
            if not self.running:
                self.resting = self.restTime
        elif self.resting:
            self.resting -= 1
            if not self.resting:
                self.running = self.runTime

    def reset(self):
        self.resting = 0
        self.running = self.runTime
        self.position = 0
        self.score = 0
        
def part1(data):
    for i in range(2503):
        for rd in data:
            rd.update()

    return max([x.position for x in data])

def part2(data):
    max_distance = -1
    for i in range(2503):
        for rd in data:
            if rd.position == max_distance:
                rd.score += 1
            rd.update()
        max_distance = max([x.position for x in data])

    return max(x.score for x in data)
            

with open("input.txt") as file:
    data = file.readlines()

competitors = []
for line in data:
    line = line.split()
    name = line[0]
    speed = int(line[3])
    time = int(line[6])
    rest = int(line[-2])
    reindeer = Reindeer(speed, time, rest)
    competitors.append(reindeer)

res1 = part1(competitors)
for r in competitors:
    r.reset()
res2 = part2(competitors)
print(f"Part 1: {res1}\nPart 2: {res2}")