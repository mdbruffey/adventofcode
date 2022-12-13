def is_ordered(pair):
    left, right = pair
    for i in range(0, min([len(left),len(right)])):
        if left[i] == right[i]:
            continue
        elif type(left[i]) == int and type(right[i]) == int:
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
        elif type(left[i]) == list and type(right[i]) != list:
            return is_ordered((left[i],[right[i]]))
        elif type(left[i]) != list and type(right[i]) == list:
            return is_ordered(([left[i]],right[i]))
        else:
            return is_ordered((left[i],right[i]))
            
    if len(left) > len(right):
        return False
        
    return True

def part1(data):
    data = data.split("\n\n")
    pairs = []
    for i, pair in enumerate(data):
        left, right = pair.split("\n")
        left = eval(left)
        right = eval(right)
        pairs.append((left,right))
        
    ordered = []
    for pair in pairs:
        ordered.append(is_ordered(pair))
    count = 0
    for i in range(len(ordered)):
        if ordered[i]:
            count += i+1
    return count

def part2(data):
    data = data.split("\n\n")
    packets = []
    for pair in data:
        left, right = pair.split("\n")
        left = eval(left)
        right = eval(right)
        packets.append(left)
        packets.append(right)
        
    packets.append([[2]])
    packets.append([[6]])
    swapped = True
    count = 0
    while count < 500:
        swapped = False
        for i in range(len(packets)-1):
            if not is_ordered( (packets[i],packets[i+1]) ):
                packets[i], packets[i+1] = packets[i+1], packets[i]
                swapped = True
        count += 1
    for packet in packets:
        print(packet)
    return (packets.index([[2]])+1)*(packets.index([[6]])+1)

with open("input.txt") as file:
    data = file.read()
res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
