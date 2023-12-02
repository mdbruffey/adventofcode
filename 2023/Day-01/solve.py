import time

num_dict = {"one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"}

def part1(data):
    count = 0
    for line in data:
        nums = ""
        for char in line:
            if char.isnumeric():
                nums += char
        count += int(nums[0]+nums[-1])

    return count

def part2(data):
    count = 0
    for line in data:
        line = line.strip("\n")
        nums = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                nums += line[i]
            else:
                for num in num_dict:
                    if line[i:i+len(num)] == num:
                        nums += num_dict[num]

        num = int(nums[0]+nums[-1])
        count += int(nums[0]+nums[-1])
    return count

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")