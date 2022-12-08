def has_valid_fields(val, rdict):
	for key in rdict.keys():
		if in_range(val, rdict[key]):
			return True
			
	return False
	
def in_range(val, ranges):
	a1, b1 = map(int, ranges[0].split("-"))
	a2, b2 = map(int, ranges[1].split("-"))
	return (val > a1 and val < b1) or (val > a2 and val < b2)

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
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2; {res2}")
