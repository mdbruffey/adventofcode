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
        continue
    wait = find_wait_time(depart, int(bus))
    if wait < least[0]:
        least[0] = wait
        least[1] = bus

print(f"You can catch bus #{least[1]} in {least[0]} minutes.")
print(int(least[0])*int(least[1]))

bus_dict = {}
for i, bus in enumerate(buses):
    if bus != "x":
        bus_dict[int(bus)] = i

buses = list(bus_dict.keys())
p1 = buses[0]
phi1 = bus_dict[p1]
for i in range(1,len(buses)):
    p2 = buses[i]
    p3 = lcm(p1,p2)
    phi2 = bus_dict[p2]
    g, s, t = extended_gcd(p1, p2)
    z = (phi1 - phi2)//g
    m = int(z*s)
    phi3 = (-m*p1 + phi1)%p3
    p1 = p3
    phi1 = phi3

print(p1-phi1)




        
