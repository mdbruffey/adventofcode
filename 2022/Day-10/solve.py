import numpy

def part1(data):
    instructions = data.split("\n")
    
    cycle = 1
    x = 1
    break_points = list(range(20,221,40))
    break_vals = []

    for instruction in instructions:
        if "noop" in instruction:
            cycle += 1
            if cycle in break_points:
                break_vals.append(cycle*x)
        else:
            cycle += 1
            if cycle in break_points:
                break_vals.append(cycle*x)
            cycle += 1
            x += int(instruction.split(" ")[1])
            if cycle in break_points:
                break_vals.append(cycle*x)
    return sum(break_vals)


def print_screen(screen):
    for row in screen:
        print("".join(row))

def write_pixel(cycle, screen, x):
    x_j = numpy.fmod(x,40)
    c_i = (cycle-1)//40
    c_j = (cycle-1) % 40
    if abs(x_j - c_j) <= 1:
        screen[c_i][c_j] = "█"

def part2(data):
    instructions = data.split("\n")
    
    cycle = 1
    x = 1
    screen = [["." for x in range(40)] for y in range(6)]
    write_pixel(cycle, screen, x)
    for instruction in instructions:
        if "noop" in instruction:
            cycle += 1
            write_pixel(cycle, screen, x)
            
        else:
            cycle += 1
            write_pixel(cycle, screen, x)
            cycle += 1
            x += int(instruction.split(" ")[1])
            write_pixel(cycle, screen, x)
            
            
    print_screen(screen)
    return "Done"
    
    print_screen(screen)


with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
input("")
