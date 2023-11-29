import time

keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

keypad2 = [
            [" "," ", 1, " "," "],
            [" ", 2,  3,  4, " "],
            [ 5,  6,  7,  8,  9 ],
            [" ","A","B","C"," "],
            [" "," ","D"," "," "]]

def part1(data):
    row = 1
    col = 1
    result = ""
    for line in data:
        for char in line:
            if char =="L":
                col -= 1
                if col < 0:
                    col = 0
            elif char == "R":
                col += 1
                if col > len(keypad[0])-1:
                    col -= 1
            elif char == "U":
                row -= 1
                if row < 0:
                    row = 0
            elif char =="D":
                row += 1
                if row > len(keypad)-1:
                    row -= 1
        result += str(keypad[row][col])
    return result

def part2(data):
    row = 2
    col = 0
    result = ""
    for line in data:
        for char in line:
            if char =="L":
                col -= 1
                if col < 0:
                    col = 0
                if keypad2[row][col] == " ":
                    col += 1
            elif char == "R":
                col += 1
                if col > len(keypad2[0])-1:
                    col -= 1
                if keypad2[row][col] == " ":
                    col -= 1
            elif char == "U":
                row -= 1
                if row < 0:
                    row = 0
                if keypad2[row][col] == " ":
                    row += 1
            elif char =="D":
                row += 1
                if row > len(keypad2)-1:
                    row -= 1
                if keypad2[row][col] == " ":
                    row -= 1
        result += str(keypad2[row][col])
    return result

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")