import time

def part1(data):
    num = 0
    for line in data:
        words = line.split()
        good = True
        for i, word in enumerate(words):
            if word in words[i+1:]:
                good = False
                break
        if good:
            num += 1
    return num

def has_anagram(word, words):
    word = list(word)
    word.sort()
    for w in words:
        w = list(w)
        w.sort()
        if word == w:
            return True
    return False

def part2(data):
    num = 0
    for line in data:
        words = line.split()
        good = True
        for i, word in enumerate(words):
            if has_anagram(word, words[i+1:]):
                good = False
                break
        if good:
            num += 1
    return num

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")