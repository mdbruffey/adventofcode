import time

def rotate_on_letter(password, letter):
    dist = 1 + password.index(letter)
    if dist > 4:
        dist += 1
    dist = dist%len(password)
    password = password[-dist:] + password[:-dist]
    return password

def rotate_left(s, n):
    return s[n%len(s):] + s[:n%len(s)]

def manipulate(password, ins):
    ins = ins.split()
    per = ins[0]
    if per == "swap":
        if ins[1] == "position":
            idx1 = int(ins[2])
            idx2 = int(ins[5])
        else:
            idx1 = password.index(ins[2])
            idx2 = password.index(ins[5])
        password[idx1], password[idx2] = password[idx2], password[idx1]
    elif per == "rotate":
        if ins[1] == "left":
            dist = int(ins[2])
            password = password[dist:] + password[:dist]
        elif ins[1] == "right":
            dist = int(ins[2])
            password = password[-dist:] + password[:-dist]
        else:
            dist = 1 + password.index(ins[-1])
            if dist > 4:
                dist += 1
            dist = dist%len(password)
            password = password[-dist:] + password[:-dist]
    elif per == "reverse":
        a = int(ins[2])
        b = int(ins[4])
        if a == 0:
            password = password[:a] + password[b:a:-1] + [password[0]] + password[b+1:]
        else:
            password = password[:a] + password[b:a-1:-1] + password[b+1:]
    else:
        item = password.pop(int(ins[2]))
        target = int(ins[5])
        password = password[:target] + [item] + password[target:]
    return password

def undo(password, ins):
    ins = ins.split()
    per = ins[0]
    if per == "swap":
        if ins[1] == "position":
            idx1 = int(ins[2])
            idx2 = int(ins[5])
        else:
            idx1 = password.index(ins[2])
            idx2 = password.index(ins[5])
        password[idx1], password[idx2] = password[idx2], password[idx1]
    elif per == "rotate":
        if ins[1] == "left":
            dist = int(ins[2])
            password = password[-dist:] + password[:-dist]
        elif ins[1] == "right":
            dist = int(ins[2])
            password = password[dist:] + password[:dist]
        else:
            #########NOT READY###########
            for i in range(len(password)):
                unscrambled = rotate_left(password, i)
                if rotate_on_letter(unscrambled, ins[-1]) == password:
                    password = unscrambled
                    break
    elif per == "reverse":
        a = int(ins[2])
        b = int(ins[4])
        if a == 0:
            password = password[:a] + password[b:a:-1] + [password[0]] + password[b+1:]
        else:
            password = password[:a] + password[b:a-1:-1] + password[b+1:]
    else:
        item = password.pop(int(ins[5]))
        target = int(ins[2])
        password = password[:target] + [item] + password[target:]
    return password


def part1(password, instructions):
    for instruction in instructions:
        password = manipulate(password, instruction)
    return ''.join(password)

def part2(password, instructions):
    for instruction in instructions[::-1]:
        password = undo(password, instruction)
    return ''.join(password)

with open("input.txt") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip("\n")

password = list("abcdefgh")

password2 = list("fbgdceah")

start = time.perf_counter()
res1 = part1(password, data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(password2, data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")