from math import lcm, gcd

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

def find_wait_time(depart, bus_id):
    i = 1
    while i*bus_id < depart:
        i += 1
    return i*bus_id - depart

with open("input.txt") as file:
    data = file.read().split("\n")
    depart = int(data[0])
    buses =data[1].split(',')
    
least = [1000,0]
for i, bus in enumerate(buses):
    if bus == "x":
        buses[i] = 1
        continue
    wait = find_wait_time(depart, int(bus))
    if wait < least[0]:
        least[0] = wait
        least[1] = bus

print(f"You can catch bus #{least[1]} in {least[0]} minutes.")
print(int(least[0])*int(least[1]))

print(extended_gcd(5,11))
"""
buses = list(map(int, buses))
time = 0
inc = max(buses)
while True:
    if all([(time + i)%bus == 0 for i, bus in enumerate(buses)]):
        break
    time += buses[0]

print(time)
"""
