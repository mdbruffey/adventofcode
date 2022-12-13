def process_rules(bags):
    rules = {}
    for bag in bags:
        bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
        bag = bag.split(" contain ")
        rules[bag[0]] = bag[1]
    return rules

with open('rules.txt') as file:
      bags = file.read().split("\n")

rules = process_rules(bags)

#list of lists of each "tier"
allowed_tiered = [['shiny gold']]
i = 0
while True:
    allowed = []
    for key in rules.keys():
            for bag in allowed_tiered[i]:
                if bag in rules[key]:
                    allowed.append(key)
                    break
    if len(allowed) == 0:
        break
    allowed_tiered.append(allowed)
    i += 1

#converting this list of lists into one list
full = []
for tier in allowed_tiered[1:]:
    full.extend(tier)
#removing duplicates (some bags exist in more than one "tier")
allowed_unique = set(full)
print(len(allowed_unique))

