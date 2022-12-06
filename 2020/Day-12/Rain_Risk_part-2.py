def execute(direction, ship, nav):
    d = direction[0]
    q = int(direction[1:])
    match d:
        case 'N':
            nav[1] += q
        case 'E':
            nav[0] += q
        case 'S':
            nav[1] -= q
        case 'W':
            nav[0] -= q
        case 'F':
            ship[0] += q*nav[0]
            ship[1] += q*nav[1]
        case 'L':
            rotate(nav, q//90, False)
        case 'R':
            rotate(nav, q//90, True)

def rotate(nav, n, clockwise):
    for i in range(n):
        t_x = nav[0]
        t_y = nav[1]
        if clockwise:
            nav[0] = t_y 
            nav[1] = -t_x
        else:
            nav[0] = -t_y
            nav[1] = t_x
        
    

with open('input.txt') as file:
    data = file.read().split("\n")

ship_status = [0,0] #[X,Y]
nav_status = [10,1] #[X,Y]


for direction in data:
    execute(direction, ship_status, nav_status)

print(f"Manhattan Distance: {abs(ship_status[0]) + abs(ship_status[1])}")

