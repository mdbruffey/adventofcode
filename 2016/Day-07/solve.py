import time

def contains_abba(string):
    for i in range(len(string)-3):
        if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
            return True
    return False

def supports_tls(raw):
    raw = raw.strip("\n")
    while "[" in raw:
        idx1 = raw.find("[")
        idx2 = raw.find("]")
        hypernet = raw[idx1+1:idx2]
        if contains_abba(hypernet):
            return False
        raw = raw[:idx1] + " " + raw[idx2+1:]

    return contains_abba(raw)
    
def supports_ssl(raw):
    raw = raw.strip("\n")
    hypers = []
    while "[" in raw:
        idx1 = raw.find("[")
        idx2 = raw.find("]")
        hypers.append(raw[idx1+1:idx2])
        raw = raw[:idx1] + " " + raw[idx2+1:]

    abas = []
    for i in range(len(raw)-2):
        if raw[i] == raw[i+2] and raw[i] != raw[i+1]:
            abas.append(raw[i:i+3])
    for aba in abas:
        for hyper in hypers:
            if aba[1:]+aba[1] in hyper:
                return True
    return False

def part1(data):
    count = 0
    for ip in data:
        if supports_tls(ip):
            count += 1

    return count

def part2(data):
    count = 0
    for ip in data:
        if supports_ssl(ip):
            count += 1

    return count

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")