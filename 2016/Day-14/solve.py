import time
import hashlib

def stretch_hash(hash, num):
    for _ in range(num):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def part1(salt, window_size):
    keys = []
    window = [hashlib.md5((salt + str(i)).encode()).hexdigest() for i in range(window_size)]
    i = window_size
    while True:
        current = window.pop(0)
        window.append(hashlib.md5((salt + str(i)).encode()).hexdigest())
        candidate = None
        for j in range(len(current)-2):
            if current[j] == current[j+1] and current[j] == current[j+2]:
                candidate = current[j]*5
                break
        if candidate:
            for j in range(len(window)):
                if candidate in window[j]:
                    keys.append(current)
                    if len(keys) == 64:
                        return i-window_size
        i += 1


def part2(salt, window_size, stretch):
    keys = []
    window = [stretch_hash(hashlib.md5((salt + str(i)).encode()).hexdigest(), stretch) for i in range(window_size)]
    i = window_size
    while True:
        current = window.pop(0)
        window.append(stretch_hash(hashlib.md5((salt + str(i)).encode()).hexdigest(),stretch))
        candidate = None
        for j in range(len(current)-2):
            if current[j] == current[j+1] and current[j] == current[j+2]:
                candidate = current[j]*5
                break
        if candidate:
            for j in range(len(window)):
                if candidate in window[j]:
                    keys.append(current)
                    if len(keys) == 64:
                        return i-window_size
        i += 1

salt = "zpqevtbw"
window_size = 1000
stretch_length = 2016

start = time.perf_counter()
res1 = part1(salt, window_size)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(salt, window_size, stretch_length)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")