import random

def score_cookie(cookie, ingredients):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingredient in cookie:
        capacity += cookie[ingredient]*ingredients[ingredient]["capacity"]
        durability += cookie[ingredient]*ingredients[ingredient]["durability"]
        flavor += cookie[ingredient]*ingredients[ingredient]["flavor"]
        texture += cookie[ingredient]*ingredients[ingredient]["texture"]
        calories += cookie[ingredient]*ingredients[ingredient]["calories"]
    
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0   

    return capacity*durability*flavor*texture

def generate_cookie(ingredients):
    amounts = []
    for i in range(len(ingredients)-1):
        amounts.append(random.randint(0,100-sum(amounts)))
    amounts.append(100-sum(amounts))
    cookie = {}
    for i, ingredient in enumerate(ingredients):
        cookie[ingredient] = amounts[i]
    return cookie

def generate_cookie_lite(ingredients):
    while True:
        amounts = []
        for i in range(len(ingredients)-1):
            amounts.append(random.randint(0,100-sum(amounts)))
        amounts.append(100-sum(amounts))
        cals = 0
        for i, ingredient in enumerate(ingredients):
            cals += ingredients[ingredient]["calories"]*amounts[i]
        if cals == 500:
            break

    cookie = {}
    for i, ingredient in enumerate(ingredients):
        cookie[ingredient] = amounts[i]
    return cookie

def part1(ingredients):
    max_score = 0
    for i in range(100000):
        cookie = generate_cookie(ingredients)
        score = score_cookie(cookie, ingredients)
        if score > max_score:
            max_score = score
    return max_score

def part2(ingredients):
    max_score = 0
    for i in range(100000):
        cookie = generate_cookie_lite(ingredients)
        score = score_cookie(cookie, ingredients)
        if score > max_score:
            max_score = score
    return max_score

with open("input.txt") as file:
    data = file.readlines()

ingredients = {}
for line in data:
    name, stats = line.split(": ")
    stats = stats.split()
    entry = {}
    entry["capacity"] = int(stats[1].strip(","))
    entry["durability"] = int(stats[3].strip(","))
    entry["flavor"] = int(stats[5].strip(","))
    entry["texture"] = int(stats[7].strip(","))
    entry["calories"] = int(stats[9])
    ingredients[name] = entry
    

res1 = part1(ingredients)
res2 = part2(ingredients)
print(f"Part 1: {res1}\nPart 2: {res2}")