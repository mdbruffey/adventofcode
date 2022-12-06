def thing():
    return

with open("input.txt") as file:
    data = file.read()

count = 0
for i in range(len(data)):
    unique = True
    for letter in data[i:i+4]:
        if data[i:i+4].count(letter) > 1:
            unique = False
    if unique:
        print(i+4)
        break
for i in range(i,len(data)):
    unique = True
    for letter in data[i:i+14]:
        if data[i:i+14].count(letter) > 1:
            unique = False
    if unique:
        print(i+14)
        break
