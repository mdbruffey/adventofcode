def count_trees(forest, slope):
    count = 0
    length = len(forest[0]) - 1
    x = 0
    for i in range(0, len(forest),slope[1]):
        if x > length-1:
            x -= length
        if forest[i][x] == '#':
            count += 1
        x += slope[0]
    return count

with open('day3_forest.txt') as file:
    forest = file.readlines()

slopes = [(1,1),
                  (3,1),
                  (5,1),
                  (7,1),
                  (1,2)]
count = 1
for slope in slopes:
    count *= count_trees(forest, slope)
    
print(count)
