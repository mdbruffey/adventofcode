import time
import os
import keyboard

class Robot():
    def __init__(self, pos, vel, room_size):
        self.x, self.y = pos
        self.vx, self.vy = vel
        self.room_size = room_size

    def move(self, steps):
        nx,ny = self.x + self.vx*steps, self.y + self.vy*steps
        nx,ny = nx%self.room_size[0], ny%self.room_size[1]
        if nx < 0:
            nx += self.room_size[0]
        if ny < 0:
            ny += self.room_size[1]
        self.x, self.y = nx, ny

    def get_quadrant(self):
        if self.x < self.room_size[0]//2 and self.y < self.room_size[1]//2:
            return 1
        if self.x < self.room_size[0]//2 and self.y > self.room_size[1]//2:
            return 2
        if self.x > self.room_size[0]//2 and self.y < self.room_size[1]//2:
            return 3
        if self.x > self.room_size[0]//2 and self.y > self.room_size[1]//2:
            return 4
        return 0
    
def print_robots(robots,room_size, show=True):
    if show:
        os.system('cls')
    room = [[" " for __ in range(room_size[0])] for _ in range(room_size[1])]
    for robot in robots:
        x,y = robot.x, robot.y
        room[y][x] = "■"
    for i in range(room_size[1]):
        line = "".join(room[i])
        if show:
            print(line)
        else:
            if "■■■■■■■■■■■■■■■■■■■■■■■■" in line:
                return True
    return False

def part1(robots):
    counts = [0,0,0,0,0]
    steps = 100
    for robot in robots:
        robot.move(steps)
        counts[robot.get_quadrant()] += 1
    return counts[1]*counts[2]*counts[3]*counts[4]

def part2(robots):
    i = 100
    while True:
        for robot in robots:
            robot.move(1)
        i += 1
        if print_robots(robots,(101,103),False):
            break
    vel = 1
    #print_robots(robots,(101,103))
    #print(f"Seconds elapsed: {i}")
    return i
    #code to display and step through frames
    while True:
        print("Press right to advance. Left to go back. Esc to quit")
        key = keyboard.read_key()
        if key == "left":
            if i == 0:
                continue
            vel = -1
        elif key == "right":
            vel = 1
        elif key == "esc":
            return i
        else:
            continue
        for robot in robots:
            robot.move(vel)
        i += vel
        print_robots(robots,(101,103))
        print(f"Seconds elapsed: {i}")

with open("input.txt") as file:
    data = file.read().splitlines()

robots = []
room_size = (101,103)
for line in data:
    pos,vel = line.split()
    pos = tuple(map(int,pos.split("=")[1].split(",")))
    vel = tuple(map(int,vel.split("=")[1].split(",")))
    robots.append(Robot(pos,vel,room_size))




start = time.perf_counter()
res1 = part1(robots)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(robots)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")