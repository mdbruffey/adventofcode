def parse_rules(data):
    rules = {}
    for line in data:
        alts = []
        rid, raw = line.split(": ")
        print(raw)
        if raw.strip('"') in "ab":
            rules[rid] = raw.strip('"')
            continue
        raw = raw.split(" | ")
        for alt in raw:
            alts.append(alt.split())
        rules[rid] = alts
    return rules

def matches_rule(m, rule, rules):
    if isinstance(rules[rule], str):
        return m[0] == rules[rule]
    
    for alt in rules[rule]:
        i = 0
        for sub in alt:
            if not matches_rule(m[i:], sub, rules):
                i += len(sub)
            else:
                return True
    return False
        

def part1(data):
    rules, messages = data.split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")
    rules = parse_rules(rules)
    print(rules)
    count = 0
    for message in messages:
        if matches_rule(message, "0", rules):
            count += 1
    return count
	
def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()
	
res1= part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
