import random
import time

spell_costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}

class Player:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self.effects = []
        self.spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
        self.base_armor = 0
        self.mana_spent = 0

    def update(self, debug=False):
        self.armor = 0
        for effect in self.effects:
            effect.update(self, debug)
        for effect in self.effects:
            if effect.duration == 0:
                self.effects.remove(effect)

    def cast_spell(self, target, debug=False):
        if self.mana < 53:
            self.health = 0
            return
        
        spell = random.choice(self.spells)
        while spell_costs[spell] > self.mana or spell in [x.name for x in self.effects]:
            spell = random.choice(self.spells)
        '''
        if "Shield" not in [x.name for x in self.effects] and self.mana > spell_costs["Shield"] + spell_costs["Recharge"]:
            spell = "Shield"
        elif "Recharge" not in [x.name for x in self.effects]:
            spell = "Recharge"
        elif "Poison" not in [x.name for x in self.effects]:
            spell = "Poison"
        else:
            spell = "Magic Missile"
        '''

        if spell == "Magic Missile":
            self.mana -= spell_costs[spell]
            self.mana_spent += spell_costs[spell]
            target["health"] -= 4
        elif spell == "Drain":
            self.mana -= spell_costs[spell]
            self.mana_spent += spell_costs[spell]
            target["health"] -= 2
            self.health += 2
        elif spell == "Shield":
            self.mana -= spell_costs[spell]
            self.mana_spent += spell_costs[spell]
            self.effects.append(Effect("Shield", 6))
        elif spell == "Poison":
            self.mana -= spell_costs[spell]
            self.mana_spent += spell_costs[spell]
            self.effects.append(Effect("Poison", 6, target))
        elif spell == "Recharge":
            self.mana -= spell_costs[spell]
            self.mana_spent += spell_costs[spell]
            self.effects.append(Effect("Recharge", 5))
        if debug:
            print(f"Player cast {spell}")

class Effect:
    def __init__(self, name, duration, target=None):
        self.name = name
        self.duration = duration
        self.target = target

    def update(self, player, debug=False):
        self.duration -= 1
        if debug:
            print(f"{self.name} procs. {self.duration} turns remaining.")
        if self.name == "Shield":
            player.armor = player.base_armor + 7
        elif self.name == "Poison":
            if self.target:
                self.target["health"] -= 3
        elif self.name == "Recharge":
            player.mana += 101

def battle(player, boss, debug=False, difficulty="easy"):
    while True:
        #player's turn
        if difficulty == "hard":
            player.health -= 1
            if player.health < 0:
                return 0
        player.update(debug)
        if debug:
            print(f"Player: {player.health} -- Boss: {boss['health']}")
            time.sleep(1)
        if boss["health"] < 1:
            return player.mana_spent
        player.cast_spell(boss, debug)
        if debug:
            print(f"Player: {player.health} -- Boss: {boss['health']}")
            time.sleep(1)
        if player.health < 1:
            return 0
        if boss["health"] < 1:
            return player.mana_spent
        #boss's turn
        player.update(debug)
        if debug:
            print(f"Player: {player.health} -- Boss: {boss['health']}")
            time.sleep(1)
        if boss["health"] < 1:
            return player.mana_spent
        bdamage = boss["damage"] - player.armor
        if bdamage < 1:
            bdamage = 1
        player.health -= bdamage
        if debug:
            print(f"Boss deals {bdamage} damage.")
            print(f"Player: {player.health} -- Boss: {boss['health']}")
            time.sleep(1)
        if player.health < 1:
            return 0
        if boss["health"] < 1:
            return player.mana_spent

def part1(data):
    min_mana = 1000000
    for i in range(1):
        player = Player(50, 500)
        boss = {"health": data["health"],
                "damage": data["damage"]}
        mana_spent = battle(player, boss, debug=False)
        if mana_spent:
            #print("Player Won")
            if mana_spent < min_mana:
                min_mana = mana_spent
        #else:
            #print("Player Lost")
    return min_mana

def part2(data):
    min_mana = 1000000
    for i in range(10000000):
        player = Player(50, 500)
        boss = {"health": data["health"],
                "damage": data["damage"]}
        mana_spent = battle(player, boss, debug=False, difficulty="hard")
        if mana_spent:
            #print("Player Won")
            if mana_spent < min_mana:
                min_mana = mana_spent
        #else:
            #print("Player Lost")
    return min_mana

with open("input.txt") as file:
    data = file.readlines()

boss = {}
boss["health"] = int(data[0].split(": ")[1])
boss["damage"] = int(data[1].split(": ")[1])

res1 = part1(boss)
res2 = part2(boss)
print(f"Part 1: {res1}\nPart 2: {res2}")