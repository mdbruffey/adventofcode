def thing(string, debug=False):
    g1,g2 = string.split(",")
    r1 = [*range(int(g1[:g1.find("-")]),int(g1[g1.find("-")+1:])+1)]
    r2 = [*range(int(g2[:g2.find("-")]),int(g2[g2.find("-")+1:])+1)]
    intersection = list(set(r1).intersection(r2))
    if debug:
        print(intersection)
    if intersection != []:
        return True
    else:
        return False
    

with open('input.txt') as file:
    data = file.read().split("\n")
wrong = []    
count = 0
for line in data:
    if thing(line):
        count += 1
        wrong.append(line)

print(count)
