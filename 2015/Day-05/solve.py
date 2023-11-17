def isNice(message):
    vowels ="aeiou"
    forbidden = ["ab","cd", "pq", "xy"]
    count = 0
    for vowel in vowels:
        count += message.count(vowel)
    if count < 3:
        return False
    if not all([x not in message for x in forbidden]):
        return False
    
    for i in range(len(message)-1):
        if message[i] == message[i+1]:
            return True
        
    return False

def isNiceImproved(message):
    paired = False
    for i in range(len(message)-1):
        pair = message[i:i+2]
        for j in range(i+2,len(message)-1):
            if pair == message[j:j+2]:
                paired = True
                break
    
    for i in range(len(message)-2):
        if message[i] == message[i+2]:
            return paired
        
    return False

def part1(data):
    count = 0
    for line in data:
        if isNice(line.lower()):
            count += 1

    return count

def part2(data):
    count = 0
    for line in data:
        if isNiceImproved(line.lower()):
            count += 1

    return count

with open("input.txt") as file:
    data = file.readlines()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")

print(isNiceImproved("xxyxx"))