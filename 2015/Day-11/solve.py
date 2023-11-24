def increment(password):
    i = len(password)-1
    while True:
        letter = ord(password[i])
        if letter > 121:
            password = password[:i] + chr(97) + password[i+1:]
            i -= 1
        else:
            password = password[:i] + chr(letter + 1) + password[i+1:]
            break
    return password

def isValid(password):
    if "i" in password or "l" in password or "o" in password:
        return False
    
    straight = 0
    for i in range(len(password)-3):
        if ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2:
            straight += 1
    if not straight:
        return False
    
    doubles = set()
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            doubles.add(password[i])

    if len(doubles) < 2:
        return False
    return True

def part1(password):
    while True:
        password = increment(password)
        if isValid(password):
            return password


with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part1(res1)
print(f"Part 1: {res1}\nPart 2: {res2}")