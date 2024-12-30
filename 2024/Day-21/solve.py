import time

keypad = {"0":(1,0),
          "A":(2,0),
          "1":(0,1),
          "2":(1,1),
          "3":(2,1),
          "4":(0,2),
          "5":(1,2),
          "6":(2,2),
          "7":(0,3),
          "8":(1,3),
          "9":(2,3)}

dir_pad = {"<":(0,0),
           "v":(1,0),
           ">":(2,0),
           "^":(1,1),
           "A":(2,1)}

def translate(digits, keypad):
    curr = keypad["A"]
    instructions = ""
    for digit in digits:
        next = keypad[digit]
        dx, dy = next[0]-curr[0], next[1]-curr[1]
        if dy > 0:
            vertical = "^"*dy
        else:
            vertical = "v"*-dy
        if dx > 0:
            horizontal = ">"*dx
        else:
            horizontal = "<"*-dx
        if not curr[0]:
            instructions += horizontal + vertical
        else:
            instructions += vertical + horizontal
        instructions += "A"
        curr = next
    return instructions

def part1(data):
    count = 0
    for line in data:
        instructions = translate(line, keypad)
        for i in range(2):
            instructions = translate(instructions, dir_pad)
        print(f"{line}: {instructions}\n{len(instructions)}*{int(line[:-1])}")
        count += len(instructions)*int(line[:-1])
    return count

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")