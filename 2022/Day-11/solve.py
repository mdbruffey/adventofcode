class Monkey:
    def __init__(self, name, div, items, operator, op_val, rule, targets):
        self.name = name
        self.div = div
        self.items = items
        self.rule = rule
        self.operator = operator
        self.op_val = op_val
        self.targets = targets
        self.count = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, monkeys, M):
        for item in self.items:
            tmp = item
            if self.operator == "+":
                if self.op_val == "old":
                    op_val = item
                else:
                    op_val = int(self.op_val)
                tmp += op_val
            else:
                if self.op_val == "old":
                    op_val = item
                else:
                    op_val = int(self.op_val)
                tmp *= op_val
            tmp = tmp // self.div
            tmp = tmp % M
            if tmp % self.rule == 0:
                monkeys[self.targets[0]].add_item(tmp)
            else:
                monkeys[self.targets[1]].add_item(tmp)
            self.count += 1
        self.items = []
            
    def get_count(self):
        return self.count
            

def part1(data):
    data = data.split("\n\n")

    monkeys = []
    M = 1
    for i, monkey in enumerate(data):
        monkey = monkey.split("\n")
        items = list(map(int,monkey[1].split(": ")[1].split(", ")))
        operator, op_val = monkey[2].split("= old ")[1].split(" ")
        rule = int(monkey[3].split("by ")[1])
        M *= rule
        targets = [int(monkey[4].split("monkey ")[1]),int(monkey[5].split("monkey ")[1])]
        monkeys.append(Monkey(i, 3, items, operator, op_val, rule, targets))

    for __ in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys, M)

    interactions = [x.get_count() for x in monkeys]
    interactions.sort(reverse=True)
    return interactions[0]*interactions[1]
    
def part2(data):
    data = data.split("\n\n")

    monkeys = []
    M = 1
    for i, monkey in enumerate(data):
        monkey = monkey.split("\n")
        items = list(map(int,monkey[1].split(": ")[1].split(", ")))
        operator, op_val = monkey[2].split("= old ")[1].split(" ")
        rule = int(monkey[3].split("by ")[1])
        M *= rule
        targets = [int(monkey[4].split("monkey ")[1]),int(monkey[5].split("monkey ")[1])]
        monkeys.append(Monkey(i, 1, items, operator, op_val, rule, targets))
    
    for __ in range(10000):
        for monkey in monkeys:
            monkey.inspect(monkeys, M)

    interactions = [x.get_count() for x in monkeys]
    interactions.sort(reverse=True)
    return interactions[0]*interactions[1]

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
