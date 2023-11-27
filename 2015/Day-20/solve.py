import math
import itertools
import time

def get_factors(n):
    factors = []
    while n % 2 == 0: 
        factors.append(2), 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            factors.append(i), 
            n = n / i 
    if n > 2: 
        factors.append(int(n))
    return factors 


def calc_presents(n):
    factors = get_factors(n)
    count = 1 + sum(set(factors)) + n
    for i in range(2,len(factors)):
        combos = itertools.combinations(factors, i)
        count += sum(map(lambda x: math.prod(x),set(combos)))
    return count * 10


def part1(data):
    n = 100
    presents = 0
    while presents < data:
        n +=1
        presents = calc_presents(n)
    print(presents)
    return n

def part2(data):
    pass

with open("input.txt") as file:
    data = int(file.read())

start1 = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start1:.4f} s")
start2 = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start2:.4f} s")