def part1(data):
    data = data.split('\n')
    sensor_ranges = {}
    beacons = list()
    targ_y = 2000000

    for line in data:
        sensor, beacon = line.split(": closest beacon is at ")
        sensor = sensor.replace("Sensor at ","").replace("x=","").replace(" y=","")
        x1, y1 = map(int,sensor.split(","))
        beacon = beacon.replace("x=","").replace(" y=","")
        x2, y2 = map(int,beacon.split(","))
        sensor_ranges[(x1,y1)] = abs(x2-x1) + abs(y2-y1)
        beacons.append((x2,y2))

    detected = set()
    for sensor in sensor_ranges:
        x,y = sensor
        width = 2*(sensor_ranges[sensor] - abs(y-targ_y))+1
        if width > 0:
            detected = detected.union(set(range(x-width//2, x+width//2 +1)))
    for beacon in beacons:
        x, y = beacon
        if x in detected and y == targ_y:
            detected.remove(x)
    return len(detected)

def part2(data):
    data = data.split('\n')
    sensor_ranges = {}
    beacons = list()
    targ_y = 2000000
    
    for line in data:
        sensor, beacon = line.split(": closest beacon is at ")
        sensor = sensor.replace("Sensor at ","").replace("x=","").replace(" y=","")
        x1, y1 = map(int,sensor.split(","))
        beacon = beacon.replace("x=","").replace(" y=","")
        x2, y2 = map(int,beacon.split(","))
        sensor_ranges[(x1,y1)] = abs(x2-x1) + abs(y2-y1)
        beacons.append((x2,y2))
    
    for i in range(4000001):
        if i%10000:
            print(f"{i}/4,000,001")
        detected = set()
        for sensor in sensor_ranges:
            x,y = sensor
            width = 2*(sensor_ranges[sensor] - abs(y-i))+1
            if width > 0:
                detected = detected.union(set(range(x-width//2, x+width//2 +1)))
        detected.difference_update(list(range(min(detected),max(detected)+1)))
        if detected:
            return detected[0], i
	    

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
