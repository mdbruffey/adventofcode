

with open('day3_forest.txt') as file:
    forest = file.readlines()

length = len(forest[0]) - 1
print(forest[0])
print(forest[0][31])
print(f"width of row: {length}")
count = 0
x = 0
for row in forest:
    if x > length-1:
        x -= length
    if row[x] == '#':
        count += 1
    x += 3
print(f"Number of trees: {count}")
