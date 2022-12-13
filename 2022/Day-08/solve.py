def is_hidden(i, j, trees):
    house = int(trees[i][j])
    #check up
    if all([int(tree) < house for tree in [item[j] for item in trees[:i]]]):
        return False
    #check down
    if all([int(tree) < house for tree in [item[j] for item in trees[i+1:]]]):
        return False
    #check left
    if all([int(tree) < house for tree in trees[i][:j]]):
        return False
    #check right
    if all([int(tree) < house for tree in trees[i][j+1:]]):
        return False
    return True

def view_distance(i, j, trees):
    directions = [(1,0),
                  (-1,0),
                  (0,1),
                  (0,-1)]
    score = 1
    house = int(trees[i][j])
    for direction in directions:
        count = 0
        dy, dx = direction
        x = j + dx
        y = i + dy
        while not any([y < 0,y == len(trees),x < 0,x == len(trees[0])]):
            if int(trees[y][x]) < house:
                count += 1
            else:
                count += 1
                break
            x += dx
            y += dy
        score *= count
    return score

def part1(data):
    trees = data.split("\n")
    count = 0
    for i in range(1,len(trees)-1):
        for j in range(1, len(trees[0])-1):
            if not is_hidden(i,j,trees):
                count += 1
    return count + 2*len(trees) + 2*(len(trees[0])-2)

def part2(data):
    trees = data.split("\n")
    score = 0
    for i in range(0,len(trees)):
        for j in range(0,len(trees[0])):
            new_score = view_distance(i, j, trees)
            if new_score > score:
                score = new_score
    return score

with open("input.txt") as file:
    data = file.read()
    
trees = data.split("\n")

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
