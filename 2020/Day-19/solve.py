def push(item, container, depth):
    while depth:
        container= container[-1]
        depth -= 1
    container.append(item)

def parse_parentheses(line):
    container = []
    depth = 0
    for char in line:
        if char == "(":
            push([], container, depth)
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == " ":
            continue
        else:
            push(char, container, depth)
    return container

def part1(data):
    rules, messages = data.split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")
    rdict = {}
    for rule in rules:
            rid, r = rule.split(": ")
            rdict[rid] = r.strip('"')
    
    rstring = rdict["0"]
    i = 0
    while i < len(rstring):
        if rstring[i] not in "ab |()":
            sub = f"({rdict[rstring[i]]})"
            if len(sub) == 3:
                sub = sub.strip(")(")
            rstring = f"{rstring[:i]}{sub}{rstring[i+1:]}"
        else:
            i += 1
    rlist = parse_parentheses(rstring)
    print(rlist)
	
def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()
	
res1= part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
