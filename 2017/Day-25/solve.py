import time

def part1(program):
    initial_state, runtime, state_conditions = program
    tape = {}
    pos = 0
    state = initial_state
    for _ in range(runtime):
        value = tape.setdefault(pos, 0)
        procedure = state_conditions[state][value]
        tape[pos] = procedure["write"]
        pos += procedure["move"]
        state = procedure["next"]
    return sum(tape.values())


def part2(data):
    pass

with open("input.txt") as file:
    data = file.read().split("\n\n")

initial_state, diagnostic_step = data[0].split("\n")
initial_state = initial_state.split()[-1][0]
runtime = int(diagnostic_step.split()[-2])
raw_conditions = data[1:]
state_conditions = {}
for condition in raw_conditions:
    lines = condition.split("\n")
    state = lines[0][-2]
    state_conditions[state] = {}
    lines = lines[1:]
    
    for i, line in enumerate(lines):
        if line.strip()[0:2] == "If":
            key = int(line[-2])
            continuation = {}
            write = int(lines[i+1][-2])
            move = lines[i+2].split()[-1]
            new_state = lines[i+3][-2]
            continuation["write"] = write
            continuation["move"] = 1 if move == "right." else -1
            continuation["next"] = new_state
            state_conditions[state][key] = continuation
program = (initial_state, runtime, state_conditions)
            

start = time.perf_counter()
res1 = part1(program)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(program)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")