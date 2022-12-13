def operate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "/":
        return num1 // num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    return None

def evaluate(line):
    if type(line[0]) == list:
        line[0] = evaluate(line[0])
    total = line[0]
    for i in range(1,len(line)-1,2):
        if type(line[i+1]) == list:
            line[i+1] = evaluate(line[i+1])
        total = operate(total,line[i+1],line[i])
    return total

def spec_eval(line):
    for i in range(0,len(line),2):
        if type(line[i]) == list:
            line[i] = spec_eval(line[i])
    alter = []
    while "+" in line:
        idx = line.index("+")
        line = line[:idx-1] + [line[idx-1]+line[idx+1]] + line[idx+2:]
    total = line[0]
    for i in range(2,len(line),2):
        total *= line[i]
    return total

def push(item, l, depth):
    while depth:
        l = l[-1]
        depth -= 1
    l.append(item)

def parse_parentheses(line):
    math = []
    depth = 0

    for char in line:
        if char == '(':
            push([], math, depth)
            depth += 1
        elif char ==')':
            depth -= 1
        elif char == ' ':
            continue
        elif char in "+-*/":
            push(char, math, depth)
        else:
            push(int(char), math, depth)

    return math

def part1(data):
    lines = data.split("\n")
    maths = []
    for line in lines:
        maths.append(parse_parentheses(line))

    return sum(list(map(evaluate, maths)))

def part2(data):
    lines = data.split("\n")
    maths = []
    for line in lines:
        maths.append(parse_parentheses(line))

    return sum(list(map(spec_eval, maths)))

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
