def execute(direction, status):
    d = direction[0]
    q = int(direction[1:])
    match d:
        case 'N':
            status[1] += q
        case 'E':
            status[0] += q
        case 'S':
            status[1] -= q
        case 'W':
            status[0] -= q
        case 'F':
            match status[2]:
                case 0:
                    status[1] += q
                case 90:
                    status[0] += q
                case 180:
                    status[1] -= q
                case 270:
                    status[0] -= q
        case 'L':
            status[2] -= q
            if status[2] < 0:
                status[2] += 360
        case 'R':
            status[2] += q
            if status[2] >= 360:
                status[2] -= 360

with open('input.txt') as file:
    data = file.read().split("\n")

status = [0,0,90] #[X,Y,THETA]

for direction in data:
    execute(direction, status)

print(f"Manhattan Distance: {abs(status[0]) + abs(status[1])}")
