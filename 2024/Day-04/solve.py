import time

def diagonalize(data):
    diagonal = ["".join([data[i][j+i] for i in range(len(data)-j)]) for j in range(len(data))][-1::-1]
    diagonal += ["".join([data[j+i][i] for i in range(len(data)-j)]) for j in range(1,len(data))]
    return diagonal

def has_x(data, i, j):
    d1 = data[i-1][j-1] + data[i+1][j+1]
    d2 = data[i-1][j+1] + data[i+1][j-1]
    if (d1 == "MS" or d1 == "SM") and (d2 == "MS" or d2 == "SM"):
        return True
    return False

def part1(data):
    print(f"{len(data)}x{len(data[0])}")
    key = "XMAS"
    count = 0
    for line in data:
        count += line.count(key) + line[::-1].count(key)
    #Transpose word grid
    transpose = ["".join([line[x] for line in data]) for x in range(len(data[0]))]
    for line in transpose:
        count += line.count(key) + line[::-1].count(key)
    #Create forward diagonal \
    diagonal = diagonalize(data)
    for line in diagonal:
        count += line.count(key) + line[::-1].count(key)
    #Create backward diagonal /
    diagonal = diagonalize(data[::-1])
    for line in diagonal:
        count += line.count(key) + line[::-1].count(key)
    return count

def part2(data):
    count = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            if data[i][j] == "A":
                if has_x(data, i, j):
                    count += 1
    return count

with open("input.txt") as file:
    data = file.read()
    data = data.splitlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")