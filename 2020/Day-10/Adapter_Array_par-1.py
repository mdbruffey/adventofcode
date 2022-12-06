
with open('input.txt') as file:
    data = file.read().split("\n")
adapters = list(map(int, data))
adapters.sort()

one = 0
two = 0
three = 0
if adapters[0] == 1:
    one += 1
if adapters [0] == 2:
    two += 1
if adapters[0] == 3:
    three += 1
for i in range(0, len(adapters)-1):
    dif = adapters[i+1]-adapters[i]
    if dif == 1:
        one += 1
    elif dif == 2:
        two += 1
    elif dif == 3:
        three += 1
            
three += 1
print(one*three)

print(f"One: {one}\nTwo: {two}\nThree: {three}")
