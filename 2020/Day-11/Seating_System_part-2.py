def count_neighbors(s, location):
    directions = [(-1,0),
                  (-1,1),
                  (0,1),
                  (1,1),
                  (1,0),
                  (1,-1),
                  (0,-1),
                  (-1,-1)]
    count = 0
    for dy,dx in directions:
        y,x = location
        y += dy
        x += dx
        while y >= 0 and y < len(s) and x >= 0 and x < len(s[0]):
            if s[y][x] == '#':
                count += 1
                break
            elif s[y][x] == 'L':
                break
            y += dy
            x += dx
    return count

def simulate_seating(seating):
    new_seating = [row[:] for row in seating]
    for i,row in enumerate(seating):
        for j, seat in enumerate(row):
            if seat == "L":
                if count_neighbors(seating,(i,j)) == 0:
                    new_seating[i][j] = "#"
            elif seat == "#":
                if count_neighbors(seating,(i,j)) >= 5:
                    new_seating[i][j] = "L"
                    
    return new_seating

with open('input.txt') as file:
    data = list(map(list, file.read().split("\n")))


new_seating = simulate_seating(data)
for i in range(100):
    new_seating = simulate_seating(new_seating)
    
count = 0
for row in new_seating:
    count += row.count('#')
print(count)
