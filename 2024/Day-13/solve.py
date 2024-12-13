import time
from decimal import Decimal

class PrizeMachine():
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def find_cost(self): #need to re-write this to be more deterministic
        ax, ay = Decimal(self.a[0]), Decimal(self.a[1])
        bx, by = Decimal(self.b[0]), Decimal(self.b[1])
        px, py = Decimal(self.prize[0]), Decimal(self.prize[1])
        na = (px - (px+py)/(bx+by)*bx)/(ax - (ax+ay)/(bx+by)*bx)
        nb = (px+py-na*(ax+ay))/(bx+by)
        na = round(na,5)
        nb = round(nb, 5)
        if na%1 == 0 and nb%1 == 0:
            return int(3*na + nb)
        else:
            return 0

def part1(machines):
    cost = 0
    for machine in machines:
        cost += machine.find_cost()
    return cost

def part2(machines):
    cost = 0
    shift = 10000000000000
    for machine in machines:
        machine.prize = (machine.prize[0] + shift, machine.prize[1] + shift)
        cost += machine.find_cost()
    return cost

with open("input.txt") as file:
    data = file.read().split("\n\n")
machines = []
for item in data:
    lines = item.split("\n")
    ax,ay = lines[0].split(": ")[1].split(", ")
    a = (int(ax.split("+")[1]), int(ay.split("+")[1]))
    bx,by = lines[1].split(": ")[1].split(", ")
    b = (int(bx.split("+")[1]), int(by.split("+")[1]))
    px, py = lines[2].split(": ")[1].split(", ")
    p = (int(px.split("=")[1]), int(py.split("=")[1]))
    machines.append(PrizeMachine(a,b,p))

start = time.perf_counter()
res1 = part1(machines)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(machines)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")