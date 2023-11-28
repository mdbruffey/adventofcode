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

def calc_presents_2(n):
    factors = get_factors(n)
    new_factors = []
    for i in range(2,len(factors)):
        combos = itertools.combinations(factors, i)
        new_factors.extend(list(map(lambda x: math.prod(x),set(combos))))
    factors.extend(new_factors)
    factors = set(factors)
    count = 1 + n
    for factor in factors:
        if 50 * factor > n:
            count += factor
    return count*11


def part1(data):
    n = 786200
    presents = 0
    while presents < data:
        n +=1
        presents = calc_presents(n)
    return n

def part2(data):
    n = 1000
    presents = 0
    while presents < data:
        n +=1
        presents = calc_presents_2(n)
    return n

with open("input.txt") as file:
    data = int(file.read())

start1 = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start1:.4f} s")
start2 = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start2:.4f} s")