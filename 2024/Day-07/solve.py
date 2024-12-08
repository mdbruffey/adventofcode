import time

def int_to_base(n, base):
    digits = []
    while n:
        digits.append(n%base)
        n //= base
    return "".join(map(str,reversed(digits)))

#The basic approach is generate binary numbers that represent the combinations of 
#operators to test on the list of numbers
def is_solvable(problem):
    result, nums = problem
    num_operators = len(nums)-1
    end = "1"*num_operators
    for ops in range(int(end,base=2)+1):
        ops = bin(ops).replace('0b','').rjust(num_operators,"0")
        calc = nums[0]
        for i,num in enumerate(nums[1:]):
            if ops[i] == "0":
                calc += num
            else:
                calc *= num
            if calc > result: #an attempt to do some process truncation
                break
        if calc == result:
            return result
    return False

#For part 2 and the third operator ||, I generate ternary numbers (lol)
#Is this a good idea? No, I should probably be using Itertools.combinations
#or something. Efficieny? Never met her. Takes like 20s to process Part 2...
def is_solvable_adv(problem):
    result, nums = problem
    num_operators = len(nums)-1
    end = "2"*num_operators
    for ops in range(int(end,base=3)+1):
        ops = int_to_base(ops, 3).rjust(num_operators,"0")
        calc = nums[0]
        for i,num in enumerate(nums[1:]):
            if ops[i] == "0":
                calc += num
            elif ops[i] == "1":
                calc *= num
            else:
                calc = int(str(calc)+str(num))

            if calc > result:
                break
        if calc == result:
            return result
    return False

def part1(problems):
    count = 0
    for problem in problems:
         count+= is_solvable(problem)
    return count

def part2(problems):
    count = 0
    for problem in problems:
         count+= is_solvable_adv(problem)
    return count

with open("input.txt") as file:
    data = file.read().splitlines()

problems = []
for line in data:
        result, nums = line.split(":")
        result = int(result)
        nums = list(map(int,nums.split()))
        problems.append((result,nums))

start = time.perf_counter()
res1 = part1(problems)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(problems)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")