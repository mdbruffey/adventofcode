import time
from math import lcm

def extended_gcd(a,b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    while r != 0:
        q = old_r//r
        old_r, r = r, old_r- q*r
        old_s, s = s, old_s - q*s
        old_t, t = t, old_t - q*t

    return old_r, old_s, old_t

def part1(discs):
    T1 = discs[1]["T"]
    phi1 = discs[1]["phi"]
    for i in range(2,len(discs)+1):
        T2 = discs[i]["T"]
        T3 = lcm(T1, T2)
        phi2 = discs[i]["phi"]
        g, s, t = extended_gcd(T1, T2)
        z = (phi1 - phi2)//g
        m = int(z*s)
        phi3 = (-m*T1 + phi1)%T3
        T1 = T3
        phi1 = phi3
    return T1-phi1

def part2(discs):
    discs[len(discs)+1] = {"T": 11,
                          "phi": (len(discs)+1)%11}
    T1 = discs[1]["T"]
    phi1 = discs[1]["phi"]
    for i in range(2,len(discs)+1):
        T2 = discs[i]["T"]
        T3 = lcm(T1, T2)
        phi2 = discs[i]["phi"]
        g, s, t = extended_gcd(T1, T2)
        z = (phi1 - phi2)//g
        m = int(z*s)
        phi3 = (-m*T1 + phi1)%T3
        T1 = T3
        phi1 = phi3
    return T1-phi1

with open("input.txt") as file:
    data = file.readlines()

discs = {}
for line in data:
    line = line.split(" has ")
    num = int(line[0].split("#")[1])
    period = int(line[1].split(" positions")[0])
    phi = (int(line[1].split(" position ")[1].split(".")[0])+num) % period
    disc = {"T": period,
            "phi": phi}
    discs[num] = disc

start = time.perf_counter()
res1 = part1(discs)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(discs)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")