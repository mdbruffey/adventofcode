def priority(letter):
    value = ord(letter) - 96
    if value < 0:
        value += 58
    return value

with open("input.txt") as file:
    data = file.read().split("\n")

shared = []
for i in range(0,len(data)-2,3):
    for item in data[i]:
        if item in data[i+1] and item in data[i+2]:
            shared.append(item)
            break

print(sum(list(map(priority, shared))))
