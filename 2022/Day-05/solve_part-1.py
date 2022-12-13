def move(instruction, stack):
    quant, movement = instruction.replace("move","").replace(" ","").split("from")
    start, end = map(int,movement.split("to"))
    for i in range(int(quant)):
        temp = stack[start-1].pop()
        stack[end-1].append(temp)
    return

with open("input.txt") as file:
    crates, moves = file.read().split("\n\n")

crates = crates.split("\n")
backup = crates[:]
moves = moves.split("\n")
num_piles = (len(crates[0]) // 4) + 1
print(num_piles)

stack = [[] for i in range(num_piles)]
for i in range(len(crates)-2,-1,-1):
    for j in range(0,len(crates[i]),4):
        if " " not in crates[i][j+1]:
            stack[j//4].append(crates[i][j+1])

for row in stack:
    print(row)

for instruction in moves:
    move(instruction, stack)

for row in stack:
    print(row)
    
crates = "".join([x[-1] for x in stack])
print(crates)
