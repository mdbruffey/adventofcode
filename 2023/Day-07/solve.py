import time

def get_value(hand):
    cards = {"A":.99,"K":.92,"Q":.85,"J":.78,"T":.71,"9":.64,"8":.56,
         "7":.48,"6":.40,"5":.32,"4":.24,"3":.16,"2":.08,}
    value = 0
    unique = list(set(hand))
    if len(unique) == 1:
        value += 70
    elif len(unique) == 2:
        if hand.count(unique[0]) >= 2 and hand.count(unique[1]) >= 2:
            #Full House
            value += 50
        else:
            #Four of a kind
            value += 60
    elif len(unique) == 3:
        for val in unique:
            if hand.count(val) == 3:
                #Three of a kind
                value += 40
                break
        if not value:
            #Two Pair
            value += 30
    elif len(unique) == 4:
        value += 20
    else:
        value += 10
    #trying to make a way to give values for each card in the hand... 
    # a very weird equation that seems to work?
    for i in range(len(hand)):
        value += cards[hand[i]]/50**i
    return value

def get_value_v2(hand):
    cards = {"A":.99,"K":.92,"Q":.85,"J":.01,"T":.71,"9":.64,"8":.56,
         "7":.48,"6":.40,"5":.32,"4":.24,"3":.16,"2":.08,}
    value = 0
    unique = list(set(hand))
    if len(unique) == 1:
        value += 70
    elif len(unique) == 2:
        if "J" in unique:
                value += 70 #Five of a kind
        elif hand.count(unique[0]) >= 2 and hand.count(unique[1]) >= 2:
            #Full House
            value += 50
        else:
            #Four of a kind
            value += 60
    elif len(unique) == 3:
        for val in unique:
            if hand.count(val) == 3:
                if "J" in unique: #Four of a kind
                    value += 60
                #Three of a kind
                else:
                    value += 40
                break
        if not value:
            for val in unique:
                if hand.count(val) == 2:
                    if "J" in unique: 
                        if hand.count("J") == 1:
                            #Full House
                            value += 50
                        else: #Four of a kind
                            value += 60
                    else:
                        #Two Pair
                        value += 30
                    break
    elif len(unique) == 4:
        if "J" in unique: #Three of a kind
            value += 40
        else:
            value += 20 #One pair
    else:
        if "J" in unique: #One pair
            value += 20
        else:
            value += 10
    #trying to make a way to add additional value for each card in the hand
    #for secondary ordering
    for i in range(len(hand)):
        value += cards[hand[i]]/50**i

    return value

def part1(hands):
    hands.sort(key=lambda x: get_value(x[0]))
    count = 0
    for i in range(len(hands)):
        count += (i+1)*hands[i][1]
    return count

def part2(hands):
    hands.sort(key=lambda x: get_value_v2(x[0]))
    count = 0
    for i in range(len(hands)):
        count += (i+1)*hands[i][1]
    return count

with open("input.txt") as file:
    data = file.readlines()

hands = []

for line in data:
    hand, bid = line.strip("\n").split()
    bid = int(bid)
    hands.append([hand, bid])

start = time.perf_counter()
res1 = part1(hands)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(hands)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")