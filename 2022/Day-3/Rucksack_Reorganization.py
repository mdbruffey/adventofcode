def priority(letter):
    value = ord(letter) - 96
    if value < 0:
        value += 58
    return value
with open("input.txt") as file:
    data = file.read().split("\n")

shared = []
for pack in data:
    pack_1 = pack[:len(pack)//2]
    pack_2 = pack[len(pack)//2:]
    for item in pack_1:
        if item in pack_2:
            shared.append(item)
            break

print(sum(list(map(priority, shared))))
print(priority('p'))

