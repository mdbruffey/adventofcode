def find_neighbors(s, location):
    i,j = location
    if(i == 0 and j == 0):
        return [s[i][j+1], s[i+1][j], s[i+1][j+1]]
    elif(i == 0 and j == len(s[i])-1):
        return [s[i][j-1], s[i+1][j], s[i+1][j-1]]
    elif(i == len(s)-1 and j == 0):
        return [s[i][j+1], s[i-1][j], s[i-1][j+1]]
    elif(i == len(s)-1 and j == len(s[i])-1):
        return [s[i][j-1], s[i-1][j], s[i-1][j-1]]
    elif(i == 0):
        return [s[i][j-1], s[i][j+1], s[i+1][j-1], s[i+1][j], s[i+1][j+1]]
    elif(i == len(s)-1):
        return [s[i][j-1], s[i][j+1], s[i-1][j-1], s[i-1][j], s[i-1][j+1]]
    elif(j == 0):
        return [s[i-1][j], s[i+1][j], s[i-1][j+1], s[i][j+1], s[i+1][j+1]]
    elif(j == len(s[i])-1):
        return [s[i-1][j], s[i+1][j], s[i-1][j-1], s[i][j-1], s[i+1][j-1]]
    else:
        return [s[i][j-1], s[i][j+1], s[i-1][j-1], s[i-1][j], s[i-1][j+1],
                s[i+1][j-1], s[i+1][j], s[i+1][j+1]]

def simulate_seating(seating):
    new_seating = [row[:] for row in seating]
    for i,row in enumerate(seating):
        for j, seat in enumerate(row):
            adjacent_seats = find_neighbors(seating, (i,j))
            if seat == "L":
                if adjacent_seats.count("#") == 0:
                    new_seating[i][j] = "#"
            elif seat == "#":
                if adjacent_seats.count("#") >= 4:
                    new_seating[i][j] = "L"
                    
    return new_seating

with open('input.txt') as file:
    data = list(map(list, file.read().split("\n")))


new_seating = simulate_seating(data)
for i in range(1000):
    new_seating = simulate_seating(new_seating)
    
count = 0
for row in new_seating:
    count += row.count('#')
print(count)
