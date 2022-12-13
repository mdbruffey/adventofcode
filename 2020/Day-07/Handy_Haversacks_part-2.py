def process_rules(bags):
    rules = {}
    for bag in bags:
        bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
        bag = bag.split(" contain ")
        rules[bag[0]] = bag[1]
    return rules

def count_children(parent):
    count = 0
    children = rules[parent].split(", ")
    if children[0] == "no other":
        return 0
    for child in children:
        count += int(child[0])*(count_children(child[2:])+1)
    return count

with open('rules.txt') as file:
      bags = file.read().split("\n")

rules = process_rules(bags)
print(count_children("shiny gold"))
