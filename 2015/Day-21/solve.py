import time
import random

weapons = [{"cost" : 8, "damage": 4, "armor" : 0},
           {"cost" : 10, "damage": 5, "armor" : 0},
           {"cost" : 25, "damage": 6, "armor" : 0},
           {"cost" : 40, "damage": 7, "armor" : 0},
           {"cost" : 74, "damage": 8, "armor" : 0}
]

armor = [  {"cost" : 13, "damage": 0, "armor" : 1},
           {"cost" : 31, "damage": 0, "armor" : 2},
           {"cost" : 53, "damage": 0, "armor" : 3},
           {"cost" : 75, "damage": 0, "armor" : 4},
           {"cost" : 102, "damage": 0, "armor" : 5}
]

rings = [  {"cost" : 25, "damage": 1, "armor" : 0},
           {"cost" : 50, "damage": 2, "armor" : 0},
           {"cost" : 100, "damage": 3, "armor" : 0},
           {"cost" : 20, "damage": 0, "armor" : 1},
           {"cost" : 40, "damage": 0, "armor" : 2},
           {"cost" : 80, "damage": 0, "armor" : 3}
]
    
def player_wins(player, boss):
    bhealth = boss["health"]
    while True:
        pdamage = player["damage"] - boss["armor"]
        if pdamage < 1:
            pdamage = 1
        bhealth -= pdamage
        if bhealth <= 0:
            return True
        bdamage = boss["damage"] - player["armor"]
        if bdamage < 1:
            bdamage = 1
        player["health"] -= bdamage
        if player["health"] <= 0:
            return False

def generate_random_player():
    player = {}
    player["health"] = 100
    player["inventory"] = []
    weapon = random.choice(weapons)
    player["inventory"].append(weapon)

    if random.randint(0,1):
        arm = random.choice(armor)
        player["inventory"].append(arm)
    
    num_rings = random.randint(0,2)
    if num_rings:
        rs = random.sample(rings, num_rings)
        player["inventory"].extend(rs)

    ac = 0
    damage = 0
    value = 0
    for item in player["inventory"]:
        ac += item["armor"]
        damage += item["damage"]
        value += item["cost"]
    player["armor"] = ac
    player["damage"] = damage
    player["value"] = value

    return player
    
def part1(boss):
    min_cost = 100000
    for i in range(10000):
        player = generate_random_player()
        if player_wins(player, boss):
            if player["value"] < min_cost:
                min_cost = player["value"]
    return min_cost
    
def part2(data):
    max_cost = 0
    for i in range(10000):
        player = generate_random_player()
        if not player_wins(player, boss):
            if player["value"] > max_cost:
                max_cost = player["value"]
    return max_cost

with open("input.txt") as file:
    data = file.readlines()

boss = {}
boss["health"] = int(data[0].split(": ")[1])
boss["damage"] = int(data[1].split(": ")[1])
boss["armor"] = int(data[2].split(": ")[1])

start = time.perf_counter()
res1 = part1(boss)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")