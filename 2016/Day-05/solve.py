import time
import hashlib

def part1(data):
    i = 0
    password = ""
    while len(password) < 8:
        result = hashlib.md5(f'{data}{i}'.encode())
        if result.hexdigest()[:5] == "00000":
            password += result.hexdigest()[5]
        i += 1
    return password

def part2(data):
    i = 0
    password = [" "," "," "," "," "," "," "," "]
    while " " in password:
        result = hashlib.md5(f'{data}{i}'.encode())
        if result.hexdigest()[:5] == "00000":
            try:
                idx = int(result.hexdigest()[5])
                if idx < 8:
                    if password[idx] == " ":
                        password[idx] = result.hexdigest()[6]
            except:
                pass
        i += 1
    return "".join(password)

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")