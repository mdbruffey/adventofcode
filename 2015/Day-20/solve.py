import math

def get_factors(n):
    factors = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        factors.append(2), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i and divide n 
        while n % i== 0: 
            factors.append(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n)
    return factors 


def calc_presents(n):
    factors = get_factors(n)
    print(factors)
    presents = 10
    for num in set(factors):
        for i in range(1,factors.count(num)+1):
            presents += 10*num**i
    return presents


def part1(data):
    print(calc_presents(6))

def part2(data):
    pass

with open("input.txt") as file:
    data = int(file.read())

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")