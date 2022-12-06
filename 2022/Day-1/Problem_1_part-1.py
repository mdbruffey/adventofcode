
with open('file.txt') as file:
    thing = file.readlines()

elfs = []

elf = 0
for line in thing:
    if line == "\n":
        elfs.append(elf)
        elf = 0
    else:
        elf += int(line)

print(max(elfs))
elfs.sort(reverse=True)
print(sum(elfs[:3]))
