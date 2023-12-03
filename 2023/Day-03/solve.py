import time

def neighbors(i, j, matrix):
    result = []
    for rowAdd in range(-1, 2):
        newRow = i + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = j + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == j and newRow == i:
                        continue
                    result.append(matrix[newRow][newCol])
    return result

def list_gears(rowNumber, colNumber, matrix):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    if matrix[newRow][newCol] == "*":
                        result.append((newRow,newCol))
    return result

def is_part(i, j, data):
    for neighbor in neighbors(i, j, data):
        if not neighbor.isnumeric() and neighbor != ".":
            return True
    return False

def part1(data):
    nums = []
    for i in range(len(data)):
        j = 0
        while j < len(data[i])-1:
            if data[i][j].isnumeric():
                part = False
                num = data[i][j]
                if is_part(i,j, data):
                    part = True
                try:
                    while data[i][j+1].isnumeric():
                        j += 1
                        num += data[i][j]
                        if is_part(i,j, data):
                            part = True
                except:
                    pass
                if part:
                    nums.append(int(num))
            j += 1
    return sum(nums)
    

def part2(data):
    gear_dict = {}
    for i in range(len(data)):
        j = 0
        while j < len(data[i])-1:
            if data[i][j].isnumeric():
                num = data[i][j]
                gears = set(list_gears(i,j,data))
                try:
                    while data[i][j+1].isnumeric():
                        j += 1
                        num += data[i][j]
                        gears = gears.union(set(list_gears(i,j,data)))
                except:
                    pass
                if len(gears) > 0:
                    for gear in gears:
                        if gear in gear_dict:
                            gear_dict[gear].append(int(num))
                        else:
                            gear_dict[gear] = [int(num)]

            j += 1

    count = 0
    for gear in gear_dict:
        if len(gear_dict[gear]) == 2:
            count += gear_dict[gear][0] * gear_dict[gear][1]
    return count

with open("input.txt") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip("\n")

print(is_part(0,3,data))

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")