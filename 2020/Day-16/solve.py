def has_valid_fields(val, rdict):
    for key in rdict.keys():
        if in_range(val, rdict[key]):
            return True
            
    return False

def get_invalid_fields(val, rdict):
    invalid = []
    for key in rdict:
        if not in_range(val, rdict[key]):
            invalid.append(key)
    if len(invalid) == 20:
        return []
    return invalid
    
def in_range(val, ranges):
    a1, b1 = map(int, ranges[0].split("-"))
    a2, b2 = map(int, ranges[1].split("-"))
    return (val >= a1 and val <= b1) or (val >= a2 and val <= b2)

def validate(ticket, rdict):
    ticket = list(map(int,ticket.split(",")))
    errors = 0
    for val in ticket:
        if not has_valid_fields(val, rdict):
            errors += val              
    return errors

def part1(data):
    rules, my_ticket, tickets = data.split("\n\n")
    rules = rules.split("\n")
    rdict = {}
    for line in rules:
        field, ranges = line.split(": ")
        ranges = ranges.split(" or ")
        rdict[field] = ranges
    reference = my_ticket.split("\n")[1].split(",")
    tickets = tickets.split("\n")[1:]
    errors = 0
    for ticket in tickets:
        errors += validate(ticket, rdict)
    
    return errors

def part2(data):
    rules, my_ticket, tickets = data.split("\n\n")
    rules = rules.split("\n")
    rdict = {}
    for line in rules:
        field, ranges = line.split(": ")
        ranges = ranges.split(" or ")
        rdict[field] = ranges
    reference = my_ticket.split("\n")[1].split(",")
    tickets = tickets.split("\n")[1:]
    to_remove = []
    count = 0
    for ticket in tickets:
        error = validate(ticket, rdict)
        if error != 0:
            to_remove.append(ticket)
        count += 1
    for ticket in to_remove:
        tickets.remove(ticket)

    determined = {}
    for ticket in tickets:
        ticket = list(map(int,ticket.split(",")))
        for i,value in enumerate(ticket):
            if i not in determined:
                    determined[i] = []
            invalid = get_invalid_fields(value, rdict)
            if len(invalid) >= 1:
                for field in invalid:
                    if field not in determined[i]:
                        determined[i].append(field)
    
    allowed = {}
    for i in determined:
        allowed[i] = [field for field in rdict if field not in determined[i]]
        #print(f"{i} -- {len(allowed[i])}")
    
    identified = {}
    while len(identified) < len(allowed):
        for i in allowed:
            if len(allowed[i]) == 1:
                field = allowed[i][0]
                break
                
        identified[field] = i
        for j in allowed:
            if field in allowed[j]:
                allowed[j].remove(field)
    count = 1
    for key in identified:
        if "departure" in key:
            count *= int(reference[identified[key]])
            
    return count

with open("input.txt") as file:
    data = file.read()
rules = data.split("\n\n")[0].split("\n")
rdict = {}
for line in rules:
    field, ranges = line.split(": ")
    ranges = ranges.split(" or ")
    rdict[field] = ranges

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
