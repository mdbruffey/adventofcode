import time
from itertools import combinations_with_replacement
import random

def find_indicator_presses(indicator, buttons):
    target = indicator[0]
    min_steps = 0
    state = 0
    while state != target:
        min_steps += 1
        combos = combinations_with_replacement(range(len(buttons)), min_steps)
        for combo in combos:
            state = 0
            for op in combo:
                state ^= buttons[op]
            if state == target:
                break   
    return min_steps

def find_joltage_presses(target, buttons):
    min_steps = 0
    state = [0]*len(target)
    while state != target:
        min_steps += 1
        combos = combinations_with_replacement(range(len(buttons)), min_steps)
        for combo in combos:
            state = [0]*len(target)
            for button in combo:
                for i in buttons[button]:
                    state[i] += 1
                if any([state[i] > target[i] for i in range(len(state))]):
                    break
            if state == target:
                break   
    return min_steps

def part1(data):
    lines = [line.split(" ") for line in data]
    presses = 0
    for line in lines:
        indicator = line[0].strip("][")
        indicator = (sum([2**i if indicator[i]=="#" else 0 for i in range(len(indicator))]), len(indicator))
        buttons = line[1:-1]
        buttons = [sum([2**int(i) for i in button.strip(")(").split(",")]) for button in buttons]
        presses += find_indicator_presses(indicator, buttons)
    return presses

def part2(data):
    lines = [line.split(" ") for line in data]
    presses = 0
    for line in lines:
        joltage = list(map(int,line[-1].strip("}{").split(",")))
        buttons = line[1:-1]
        buttons = [[int(i) for i in button.strip(")(").split(",")] for button in buttons]
        presses += find_joltage_presses(joltage, buttons)
    return presses

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")