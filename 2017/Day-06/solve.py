import time

def mem_balance(state):
    blocks = max(state)
    index = state.index(blocks)
    banks = len(state)
    state[index] = 0
    while blocks > 0:
        index += 1
        state[index%banks] += 1
        blocks -= 1
    return tuple(state)

def part1(data):
    state = map(int,data[0].split("\t"))
    states = {}
    cycles = 0
    while True:
        state = mem_balance(list(state))
        cycles += 1
        if state not in states:
            states[state] = ""
        else:
            return cycles, state

def part2(state):
    states = {}
    cycles = 0
    while True:
        state = mem_balance(list(state))
        cycles += 1
        if state not in states:
            states[state] = ""
        else:
            return cycles-1

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1, state = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(state)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")